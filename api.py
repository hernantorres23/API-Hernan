from flask import Flask, jsonify
from flask_restful import Resource, Api
from requests import request
import json


app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return '<h1>Welcome to the joined series API</h1>'

class WorkApi(Resource):
    def get(self, titulo):
        #devuelve los detalles de la serie encontrada en el API de tvMaze
        url = "http://api.tvmaze.com/singlesearch/shows"
        querystring = {"q":titulo,"embed":"episodes"}
        tvmaze = request("GET", url, params=querystring)

        #devuelve los detalles de la serie encontrada en el API de iTunes
        url = "https://itunes.apple.com/search"
        querystring = {"term":titulo,"entity":["movie,tvSeason","tvEpisode"],"limit":"200"}
        itunes = request("GET", url, params=querystring)
 
        # en mis tests el servicio de iTunes devuelve una lista vacia cuando no encuentra datos
        # print('Respuesta itunes',itunes.status_code, itunes.text)
        data_itunes = itunes.json() 
        
        # manejar un error si el cliente envia un valor que no se pudo encontrar en tvMaze
        if tvmaze.status_code == 404:
            return {"message": "No hay datos para su criterio de busqueda"}
        else:
            data_tvmaze = tvmaze.json()
            # buscamos el diccionario que tiene lo que me interesa evaluar
            # y capturamos los datos que queremos asignar luego de la modificacion
            for clave, datos in data_tvmaze.items():
                # el diccionario '_embedded' tiene los capitulos en el API de tvMaze
                if clave == '_embedded':
                    tvmaze_episodes = datos['episodes'] # guardamos los episodios en una variable
            # borramos el diccionario completo
            data_tvmaze['_embedded'].clear()
            # este print para validar que borramos lo correcto
            # print('Tipo de objeto despues de borrar: ', type(data_tvmaze['_embedded']))
            # agregamos episodes pero ahora como un diccionario (recuerden que episodes era originalmente una lista)
            # como es un diccionario estandar podemos crearlo antes
            embedded_dict = dict({"episodes": {}}) # entonces lo creamos
            data_tvmaze['_embedded'] = embedded_dict # aca lo asignamos
            # este print para verificar que hemos asignado correctamente el dicccionario
            # print('Tipo de objeto despues de agregar el diccionario episodes: ', type(data_tvmaze['_embedded']["episodes"]))

            # ahora agregamos las dos listas que guardaran los valores de ambas API's
            data_tvmaze['_embedded']["episodes"]['tvmaze'] = tvmaze_episodes
            data_tvmaze['_embedded']["episodes"]['itunes'] = data_itunes['results'][:]

            # tambien podemos exportarlo para evaluar mejor en caso de que la salida sea muy extensa,
            # yo siempre lo hago porque me sirve para Power BI o similares
            # busqueda = titulo + '.json' # una variable para el nombre
            # with open(busqueda,'w') as f:
                # json.dump(data_tvmaze, f)


            return data_tvmaze # valor retornado en el body

api.add_resource(Home, '/')
api.add_resource(WorkApi,'/serie/<string:titulo>', endpoint="serie")

servidor_ip = '127.0.0.1'
puerto = 5810

if __name__ == '__main__':
    app.run(servidor_ip, puerto, debug=True)