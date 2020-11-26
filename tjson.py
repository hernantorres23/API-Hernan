import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
        "owner":"Hernan"
    }
}
print('El objeto pasado pertenece a %s ' % (type(data)))

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)
print(json_string)

# Otra forma de crear el JSON
# a = {'name':'Sarah', 'age': 24, 'isEmployed': True }
# # a python dictionary
# def retjson():
#     python2json = json.dumps(a)
#     print(python2json)

# retjson()

if __name__ == '__main__':
    print('Archivo JSON creado a partir del diccionario')