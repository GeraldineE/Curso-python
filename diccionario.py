
diccionario = {
                'nombre' : 'Carlos', 
                'edad' : 22, 
                'cursos': ['Python','Django','JavaScript'] 
            }
print(diccionario['nombre'])

print(diccionario['cursos'][0])#Python
print(diccionario['cursos'][1])#Django
print(diccionario['cursos'][2])#JavaScript


for key in diccionario:
  print(key, ":", diccionario[key])


