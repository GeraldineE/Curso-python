import numpy as np


matriz_empty = np.empty((2, 3)) # Matriz vacía, con valores residuales de la memoria
matriz_de_ceros = np.zeros((3, 1)) # Matriz de ceros
matriz_de_unos = np.ones((3, 2)) # Matriz de unos
matriz_de_identididad = np.identity(3)
matriz_parametro_diagonal = np.eye(4, 3, k=-1) # Con el parámetro k podemos controlar qué diagonal está llena de unos

print(matriz_empty)
print(matriz_de_ceros)
print(matriz_de_unos)
print(matriz_de_identididad)
print(matriz_parametro_diagonal)