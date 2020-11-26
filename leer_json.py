import json

file_tvmaze = 'game_of_thrones.json'
with open(file_tvmaze, "r") as read_file:
    data_tvmaze = json.load(read_file)
print(type(data_tvmaze))

file_itunes = 'game_of_thrones_itunes.json'
with open(file_itunes, "r") as read_file:
    data_itunes = json.load(read_file)
# print(type(data_itunes))

# read_tvmaze = data_tvmaze['genres']
# print(type(read_tvmaze))
# print(len(read_tvmaze), read_tvmaze)
# data_tvmaze['genres'].append('Terror')
# print(len(read_tvmaze), read_tvmaze)
i = 0
myfile =""
for clave, datos in data_tvmaze.items():
    if clave == '_embedded':
        # print(datos['episodes'])
        print(len(datos['episodes']))
        print(datos['episodes'])

        # with open('new.json','w') as f:
        #     json.dump(datos['episodes'], f)

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
if __name__ == '__main__':
    print('Archivo JSON escrito en el directorio actual')    

