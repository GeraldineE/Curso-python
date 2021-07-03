import json


with open('Curso_python/archivos/archivo_json.json') as file:
    data = json.load(file)
    print(data)

    