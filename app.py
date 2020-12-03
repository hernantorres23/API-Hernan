from flask import Flask, render_template, request
from requests import get
import json
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(Exception)
def exception_handler(error):
    # Manejar caidas del servicio
    return "El API esta en mantenimiento, por favor intente mas tarde!!!!"  # con repr muestra el error de Flask

@app.errorhandler(500)
def internal_error(error):
    return "500 error capturado", 500

@app.errorhandler(404)
def not_found(error):
    return "404 error capturado", 404

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/series')
@app.route('/series', methods=['POST'])
def series():
    titulo = request.form.get('search')
    # raise Exception("Servidor esta caido") # si quiero mostrar el error personalizado, desconectar el servicio
    url = 'http://127.0.0.1:5810/serie/' + titulo
    serie = get(url).json()
    print(f'La serie es del tipo {type(serie)}')
    i = 0
    dict_tvmaze = {}
    encabezado = {}

# ----- INICIO: procesar los datos de la cabecera para la vista web -----
    try:
        inicio = serie['id'] # si esta llave da error es que no hay datos para mostrar
    except KeyError:
        inicio = 0
    # print(inicio)

    if inicio == 0: # no hago mas nada ya que mi base no tiene registros para llenar los diccionarios
        nombre = titulo
        if titulo != "": # esta buscando algo ya que la variable titulo tiene valores
            return render_template('404_a.html', nombre = titulo)
        # else: # pendiente de programar si hiciiera falta
            # return render_template('404_b.html')
    else: 
        nombre = serie['name']
        # print(nombre)
        if serie['officialSite'] is None:
            weboficial = 'No especificado'
        else:
            weboficial = serie['officialSite']
        print(weboficial)
        # crear una lista de generos y pasarla limpia para no hacerlo en el Jinja
        generos = ' - '.join(serie['genres'])
        # print(generos)
        # crear los horarios reportados
        # print(type(serie['schedule']['time']))
        calendario = ' - '.join(serie['schedule']['days'])
        print(calendario)
        if serie['schedule']['time'] is None:
            hora = 'Horario no especificado'
        elif serie['schedule']['time'] == '':
            hora = 'Horario no especificado'
        else:
            hora = serie['schedule']['time']
        # print(hora)

        if serie['rating']['average'] is None:
            rating = 'No especificado'
        else:
            rating = serie['rating']['average']
        # print(rating)

        # validar el canal
        if serie['network'] == '' or serie['network'] is None:
            if serie['webChannel']['name'] == '' or serie['webChannel']['name'] is None:
                canal = 'No especificado'
            else:
                canal = serie['webChannel']['name']   
        else:
            canal = serie['network']['name']
        # print(canal)

        # validar el pais
        if serie['network'] == '' or serie['network'] is None:
            if serie['webChannel']['country'] == '' or serie['webChannel']['country'] is None:
                pais = 'No especificado'
            else:
                pais = serie['webChannel']['country']   
        else:
            pais = serie['network']['country']['name']
        # print(pais)

        # validar el huso horario
        if serie['network'] == '' or serie['network'] is None:
            if serie['webChannel']['country']['timezone'] == '' or serie['webChannel']['country']['timezone'] is None:
                husohorario = 'No especificada'
            else:
                husohorario = serie['webChannel']['country']['timezone'] 
        else:
            husohorario = serie['network']['country']['timezone']
        # print(husohorario)

        if serie['premiered'] is None:
            comenzo = 'No especificado'
        else:
            comenzo = serie['premiered']
        # print(comenzo)   


        valores = {
            'termino':titulo,
            'nombre':nombre, 
            'comenzo':comenzo, 
            'status':serie['status'],
            'weboficial':weboficial, 
            'trasmision':serie['schedule'], 
            'pais':pais,
            'canal':canal,
            'husohorario':husohorario,
            'imagen':serie['image']['medium'], 
            'rating':rating, 
            'idioma':serie['language'],
            'tipo':serie['type'],
            'generos':generos,
            'calendario':calendario,
            'horario': hora,
            'resumen':serie['summary']
            } 
        encabezado['cabecera'] = valores
        # print(encabezado)
        # print(f'El encabezado es del tipo {type(encabezado)}')
        # print("Registros en tvMaze: %s" % (len(serie['_embedded']['episodes']['tvmaze'])))
        # print("Registros en iTunes: %s" % (len(serie['_embedded']['episodes']['itunes'])))
# ----- FIN proceso de datos para la cabecera web -----        
        
# ----- INICIO: procesar los registros de tvMaze -----
        # i = 0
        # dict_tvmaze = {}

        for each in serie['_embedded']['episodes']['tvmaze']:
            descripcion = str(each['summary'])
            descripcion = descripcion[3:-4]

            clave = each['id']
            valores = {
                'id' : each['id'],
                'origen':'TVmaze',
                'temporada':each['season'],
                'capitulo':each['number'],
                'nombre':each['name'],
                'estreno':each['airdate'],
                'precio':'No especificado',
                'descripcion':descripcion,
                'url': each['url']
                }
            dict_tvmaze[clave] = valores
            i += 1
        # print(dict_tvmaze)

    # print(f'Al finalizar la revision de TVMAZE el bucle va por {i}')
    # inicializo z con el ultimo valor del bucle

# ----- FIN proceso de registros TVMAZE ----- 
    print("finalice TVmaze")

    z = i - 1 # continuar el contador anterior
   

# ----- INICIO: procesar los registros de iTunes -----

    # Informar al usuario sobre una busqueda que devuelve el maximo de registros permitidos por el API
    # y la vez verficar que el API haya retornado registros
    i = 0
    dict_itunes = {}
    max_value = ''
    clave = ''
    if len(serie['_embedded']['episodes']['itunes']) == 200:
        search_message = 'Es posible que la busqueda excede el maximo permitido, \
                          solo se mostraran los primeros 200 registros'
        max_value = 200

    elif len(serie['_embedded']['episodes']['itunes']) == 0:    
        max_value = 0

    if max_value == 0:
        pass
    else:
        estructura_itunes = serie['_embedded']['episodes']['itunes']
        # print(f'La estructura de datos a recorrer es {type(estructura_itunes)}')
        # print(f'Cantidad de registros encontrados para iTunes: {max_value}')    
        # i = 0
        # print(f'Al iniciar la revision de iTunes el contador del bucle va por {z} y la letra i vale {i}')
        # dict_itunes = {}
        for each in serie['_embedded']['episodes']['itunes']:
            # serie['_embedded']['episodes']['itunes']
            # print(f'El registro {i} en itunes es {each}')
            if each['trackPrice'] <= 0:
                # id_free = each['trackId']
                # el_precio = each['trackPrice']
                # el_nombre = each['trackName']
                # la_season = each['collectionCensoredName']
                # la_season = [int(i) for i in la_season.split() if i.isdigit()]
                # print(f'El id del trailer free es {id_free} ya que muestra{el_precio} y se llama {el_nombre} y la temporada es {la_season}')
                pass
            else:
                try:
                    season = each['collectionCensoredName']
                    season = [int(i) for i in season.split() if i.isdigit()]
                    temporada = season[0]
                except IndexError:
                    temporada = 'No especificado'
                # print(temporada)

                try:
                    precio = each['currency'] + ' ' + str(each['trackHdPrice'])
                except KeyError:
                    precio = 'No especificado'
                # print(precio)

                try:
                    descripcion = each['longDescription']
                except KeyError:
                    descripcion = 'No especificado'

                try:
                    descripcion = each['longDescription']
                except KeyError:
                    descripcion = 'No especificado'    
    
                    
                fecha = each['releaseDate']
            
                clave = each['trackId']
                valores = {
                    'id' : each['trackId'],
                    'origen' : 'iTunes',
                    'temporada' : temporada,
                    'capitulo' : each['trackNumber'],
                    'nombre' : each['trackCensoredName'],
                    'estreno' : fecha[:10],
                    'precio' : precio,
                    'descripcion' : descripcion,
                    'url':each['previewUrl']
                    }
            i += 1
            # print(valores)
            z += 1
            # dict_itunes[z] = valores
            dict_itunes[clave] = valores
        # print(f'el valor de Z es {z}')
        # print(dict_itunes)

# ----- FIN proceso de registros iTunes ----- 

#     print(f'Se procesaron {z} registros')
#     return serie
#     return f'<h1>Datos procesados!!! {datetime.now()}</h1>'

    resultados = ({**dict_tvmaze, **dict_itunes})

    # print(resultados)
    # return resultados
    return render_template('results.html', results = resultados, headers = encabezado)


servidor_ip = '127.0.0.1'
puerto = 5710

if __name__ == '__main__':
    app.run(servidor_ip, puerto, debug=True)