from ..matrices.definir_matriz import crear_matriz_2


def multiplicar_matrices(matriz_a, matriz_b):
    cantidad_filas_matriz_a = len(matriz_a)
    cantidad_columnas_matriz_b = len(matriz_b[0]) 

    matriz_resultante = crear_matriz_2(
        cantidad_filas_matriz_a, cantidad_columnas_matriz_b
    )
   
    for i in range(cantidad_filas_matriz_a):
        for j in range(cantidad_columnas_matriz_b):
            for k in range(len(matriz_b)):
                matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]
    for r in matriz_resultante:
        # matriz rsultante 3x4
        print(r)

# 3x3 matrix
matriz_a = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix
matriz_b = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
print("matriz resultante")
print(multiplicar_matrices(matriz_a, matriz_b))