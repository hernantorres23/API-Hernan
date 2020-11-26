from flask import Flask, render_template, jsonify
from requests import request
import json

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Encuentre peliculas o series desde un solo lugar</h1>'

@app.route('/movies/<string:entrada>', methods=['GET'])
def show_movies(entrada):
    if entrada == '':
        return "Debe completar el parametro con algun valor tipo texto"
    else:
        # procesar series(que tiene temporadas, capitulos, etc.) desde TVMaze
        url = "http://api.tvmaze.com/singlesearch/shows"
        querystring = {"q":entrada,"embed":"episodes"}
        tvmaze_series = request("GET", url, params=querystring)
  
        # procesar series(que tiene temporadas, capitulos, etc.) desde iTunes
        url = "https://itunes.apple.com/search"
        querystring = {"term":entrada,"entity":["movie,tvSeason","tvEpisode"]}
        itunes_series = request("GET", url, params=querystring)

        '''
        Para procesar solo las peliculas, segunda parte de la API. Por razones 
        de tiempo no puedo terminar el proceso aca en Python, pero lo hare luego,
        sin embargo aca dejo la analogia del API para poder realizar el proceso 
        que es es bastante similar a este

        # procesar peliculas(un solo evento) desde TVMaze
        # url = "http://api.tvmaze.com/search/shows"
        # querystring = {"q":entrada}
        # tvmaze_films = request("GET", url, params=querystring)     

        # procesar peliculas(un solo evento) desde iTunes
        # url = "https://itunes.apple.com/search"
        # querystring = {"term":entrada,"entity":"movie"}
        # itunes_films = request("GET", url, params=querystring)
        '''
  
        a = itunes_series.json()
        b = tvmaze_series.json()
        print(type(itunes_series))

        itunes_sel = []
        print(a['results'][0].keys())
        print(a[''])
        for pelicula in a['results']:
            new_item = [[pelicula['trackId'], pelicula['trackName'], pelicula['kind']]]
            itunes_sel.extend(new_item)
            # print(itunes_sel)
            # print(type(a))
            # return json.dumps(a, indent=4, separators=(",", ":"), sort_keys=True)
            return a

#$.results[2].trackName
#$.results[:].trackName todos a la vez

if __name__ == '__main__':
    app.run(debug=True, port='5300')