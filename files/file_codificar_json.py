import json

data = {
    "Usuario": [
        {
            "Empleados": [
                {"Nombre": "Ricardo", "Edad": 30},
                {"Nombre": "Peralta", "Edad": 20},
                {"Nombre": "Maria", "Edad": 31},
            ]
        },
        {
            "Empleadores": [
                {"Nombre": "Lucia", "Edad": 32},
                {"Nombre": "Teresa", "Edad": 25},
                {"Nombre": "Federico", "Edad": 50},
            ]
        },
    ]
}
# Nos imprime en pantalla data como un tipo de dato nativo.
print("DATOS:", repr(data))
# Lo convierte en cadena formato JSON
# encoded
data_string = json.dumps(data)
print(type(data_string))
print("JSON:", data_string)

print("Tenemos " + str(len(data["Usuario"][0]["Empleados"])), "empleados")
