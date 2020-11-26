import json

# trabajando el json de iTunes
file_itunes = 'game_of_thrones_itunes.json'
with open(file_itunes, "r") as read_file:
    data_itunes = json.load(read_file)
# print("El tipo de datos es %s " % (type(data_itunes)))
# print(data_itunes)
# print("-----------------------------")
# itunes_sel = []
# for pelicula in data_itunes['results']:
    # new_item = [[pelicula['trackId'], pelicula['trackName'], pelicula['kind']]]
    # itunes_sel.extend(new_item)
# print(itunes_sel)

# trabajando el json de TVMAZE
file_tvmaze = 'game_of_thrones.json'
with open(file_tvmaze, "r") as read_file:
    data_tvmaze = json.load(read_file)
print(type(data_tvmaze))
print('Capitulos en el diccionario antes de borrar: ', len(data_tvmaze['_embedded']['episodes']))
for clave, datos in data_tvmaze.items():
    # print(datos['episodes'][:]['name'])
    # print(clave) # para ver todas las claves del root
    # print(datos['_embedded'])
    if clave == '_embedded':
        tvmaze_episodes = datos['episodes']
        for item in datos['episodes']:
            # imprimir una lista de capitulos
            # print('Capitulo: ', item['name'])
            pass

        # print(datos['episodes'][:]['name'])
        # print(len(datos['episodes']))
# borramos el diccionario
data_tvmaze['_embedded'].clear()
print('Tipo de objeto despues de borrar: ', type(data_tvmaze['_embedded']))
# agregamos episodes pero ahora como un diccionario (recuerden que episodes era una lista en el origen)
# como es estandar podemos crearlo antes
embedded_dict = dict({"episodes": {}}) # entonces lo creamos
data_tvmaze['_embedded'] = embedded_dict # aca lo asignamos
print('Tipo de objeto despues de agregar el diccionario episodes: ', type(data_tvmaze['_embedded']["episodes"]))

# ahora agregamos las dos listas que guardaran los valores de ambas API's
data_tvmaze['_embedded']["episodes"]['tvmaze'] = tvmaze_episodes
data_tvmaze['_embedded']["episodes"]['itunes'] = data_itunes['results'][:]

# seguido podemos agregar un valor de ejemplo para ver si todo va bien
# data_tvmaze['_embedded']["episodes"]['tvmaze'].append(1979) 

# ahora imprimimos en formato JSON para ver como se vera en el body
# print(json.dumps(data_tvmaze, indent=4))

# tambien podemos exportarlo para evaluarlo mejor si el archivo es muy extenso
with open('def_file_hernan.json','w') as f:
    json.dump(data_tvmaze, f)

# imprimir valores para medir lo que venimos realizando
# print('Tipo de objeto despues de actualizar la forma del root: ', type(data_tvmaze['_embedded']["episodes"]))
# print('Lstas/Fuentes disponibles en el diccionario episodes: ', len(data_tvmaze['_embedded']['episodes']))
# print('Primera lista en episodes: ', type(data_tvmaze['_embedded']['episodes']['tvmaze']))
# print('Segunda lista en episodes: ', type(data_tvmaze['_embedded']['episodes']['tvmaze']))
# print('Primer valor de la lista en episodes desde tvmaze: ', data_tvmaze['_embedded']['episodes']['tvmaze'][0])

# for clave, datos in data_tvmaze.items():
#     if clave == '_embedded':
#         print(datos['episodes']['name'])

# read_tvmaze = data_tvmaze['genres']
# print(type(read_tvmaze))
# print(len(read_tvmaze), read_tvmaze)
# data_tvmaze['genres'].append('Terror')
# print(len(read_tvmaze), read_tvmaze)
# i = 0


        # for item in datos['episodes']:
            # # print('Diccionario # ', i)
            # # print(json.dumps(item, indent=4) + (","))
            # separator = ","
            # myfile = myfile + (json.dumps(item, indent=4)) + separator
            # myfile = myfile + (item)
            # myfile = list(item).append
            # myfile = str(item) + separator
            # print(myfile)
            # with open('new.json','a') as f:
            #     json.dump(item, f)
            # print(myfile)
            # print(json.dumps(item),',',end="")

            # for k, v in item.items():
                # if k == 'id':
                #     print(v)
                # pass
                # print(k)
            # i += 1
        #print('i vale ', i)
    # if clave == '_embedded':
    #     print(episodes[2])
# print('i vale ', i)
# b = data_itunes['results']
# for claves in b:
#     if clave == 

# with open("update_json.json", "w") as write_file:
#     json.dump(myfile, write_file)

# for k, v in data:
#     print({} {}.format(k ,v))

# $._embedded.episodes[:].name
if __name__ == '__main__':
    print('Archivo JSON escrito en el directorio actual')    

