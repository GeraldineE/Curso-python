# Abrimos un archivo en modo r+ y usando with open

with open ("Curso_python/archivos/archivo.txt", "r+") as f:
    contenido = f.read() 
    print(contenido)

  