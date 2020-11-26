from flask import Flask
from requests import get
import json


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bienvenido al buscador de series</h1>'

@app.route('/serie/<string:titulo>', methods=['GET'])
def show_series(titulo):
    url = 'http://127.0.0.1:5800/series/' + titulo
    serie = get(url).json()
    cabecera = [serie['name'],serie['premiered'],serie['officialSite'],\
                serie['schedule'], serie['network'],serie['image']['medium'],\
                serie['summary']]
    print(cabecera)
    print("Capitulos en tvMaze: %s" % (len(serie['_embedded']['episodes']['tvmaze'])))
    print("Capitulos en tvMaze: %s" % (len(serie['_embedded']['episodes']['itunes'])))
    i = 0
    for each in serie['_embedded']['episodes']['tvmaze']:
        serie['_embedded']['episodes']['tvmaze']
        # organized[]
        # serie['_embedded']['episodes']['tvmaze'][i]['name']
        # print('iTunes:', serie['_embedded']['episodes']['itunes'][i]['trackCensoredName'] )
        i += 1
    return serie 


if __name__ == '__main__':
    app.run(debug=True, port='5700')