from flask import Flask
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
        #devuelve los detalles de la serie si la encuentra en TVMaze
        url = "http://api.tvmaze.com/singlesearch/shows"
        querystring = {"q":titulo,"embed":"episodes"}
        tvmaze = request("GET", url, params=querystring)

        #devuelve los detalles de la serie si la encuentra en iTunes
        url = "https://itunes.apple.com/search"
        querystring = {"term":titulo,"entity":["movie,tvSeason","tvEpisode"],"limit":"200"}
        itunes = request("GET", url, params=querystring) 

        data_tvmaze = tvmaze.json()
        
        # en mis tests el servicio de iTunes devuelve una lista vacia cuando no encuentra datos
        data_itunes = itunes.json()

        # buscamos el diccionario que tiene lo que me interesa evaluar
        # y tomamos los datos que deseamos asignar luego de la modificacion
        for clave, datos in data_tvmaze.items():
            # el diccionario '_embedded' tiene los capitulos
            if clave == '_embedded':
                tvmaze_episodes = datos['episodes'] # los guardamos en una variable
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

        # tambien podemos exportarlo para evaluarlo mejor si el archivo es muy extenso,
        # yo siempre lo haria porque me sirve para Power BI o similares
        busqueda = titulo + '.json' # una variable para el nombre
        with open(busqueda,'w') as f:
            json.dump(data_tvmaze, f)
        
        return data_tvmaze

api.add_resource(Home, '/')
api.add_resource(WorkApi,'/serie/<string:titulo>', endpoint="serie")

if __name__ == '__main__':
    app.run(debug=True, port='5800')