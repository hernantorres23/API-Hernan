from flask import Flask
from requests import request
from requests import get
import json
import time

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bienvenido al buscador de series</h1>'

@app.route('/serie/<string:titulo>', methods=['GET'])
def show_series(titulo):
    url = 'http://127.0.0.1:5100/movies/' + titulo
    series = get(url).json()
    return series['_embedded']['episodes']['itunes'][0]['trackCensoredName']   

@app.route('/movies/<string:titulo>', methods=['GET'])
def unir_datos(titulo):

    #devuelve los detalles de la serie si la encuentra en TVMaze
    url = "http://api.tvmaze.com/singlesearch/shows"
    querystring = {"q":titulo,"embed":"episodes"}
    tvmaze = request("GET", url, params=querystring)

    #devuelve los detalles de la serie si la encuentra en iTunes
    url = "https://itunes.apple.com/search"
    querystring = {"term":titulo,"entity":["movie,tvSeason","tvEpisode"],"limit":"200"}
    itunes = request("GET", url, params=querystring) 

    data_tvmaze = tvmaze.json()
    data_itunes = itunes.json()    

    # buscamos el diccionario que tiene lo que me interesa evaluar
    # y tomamos los datos que deseo asignar luego de la modificacion
    for clave, datos in data_tvmaze.items():
        # el diccionario '_embedded' tiene los capitulos
        if clave == '_embedded':
            tvmaze_episodes = datos['episodes'] # los guardamos en una variables
    # borramos el diccionario completo
    data_tvmaze['_embedded'].clear()
    # este print para validar que borramos lo correcto
    #print('Tipo de objeto despues de borrar: ', type(data_tvmaze['_embedded']))
    # agregamos episodes pero ahora como un diccionario (recuerden que episodes era originalmente una lista)
    # como es un diccioanorio estandar podemos crearlo antes
    embedded_dict = dict({"episodes": {}}) # entonces lo creamos
    data_tvmaze['_embedded'] = embedded_dict # aca lo asignamos
    # este print para verificar que hemos asignado correctamente el dicccionario
    # print('Tipo de objeto despues de agregar el diccionario episodes: ', type(data_tvmaze['_embedded']["episodes"]))

    # ahora agregamos las dos listas que guardaran los valores de ambas API's
    data_tvmaze['_embedded']["episodes"]['tvmaze'] = tvmaze_episodes
    # time.sleep(2)
    data_tvmaze['_embedded']["episodes"]['itunes'] = data_itunes['results'][:]

    # tambien podemos exportarlo para evaluarlo mejor si el archivo es muy extenso,
    # yo siempre lo haria porque me sirve para Power BI o similares
    busqueda = titulo + '.json' # una variable para el nombre
    with open(busqueda,'w') as f:
        json.dump(data_tvmaze, f)
    
    return data_tvmaze

if __name__ == '__main__':
    app.run(debug=True, port='5100')