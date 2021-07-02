import json

data = {"Usuario": [{"Empleado": [{"Nombre": "Ricardo", "Edad": 30}, {"Nombre": "Peralta", "Edad": 20}, {"Nombre": "Maria", "Edad": 31}]}, {"Empleador": [{"Nombre": "Lucia", "Edaf": 32}, {"Nombre": "Teresa", "Edad": 25}, {"Nombre": "Federico", "Edad": 50}]}]}

data_string = json.dumps(data)
print('ENCODED:', data_string)

decoded = json.loads(data_string)
print('DECODED:', decoded)