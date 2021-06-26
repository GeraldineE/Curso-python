# import csv

# with open('example.csv', newline='') as File:
#     reader = csv.reader(File) 

# for row in reader:
#     print(row) 


# import csv
# with open('name.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
# for row in reader:
#       print(row['first_name'], row['last_name'])




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





import pandas as pd
s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'],
                 dtype='string')
print(s)


import pandas as pd
df = pd.DataFrame([['María', 18], ['Luis', 22], ['Carmen', 20]], columns=['Nombre', 'Edad'])
print(df)