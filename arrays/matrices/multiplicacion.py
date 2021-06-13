# from ..matrices.definir_matriz import crear_matriz_2

def crear_matriz_2(cantidad_filas, cantidad_columnas):
    return [[0 for _c in range(cantidad_columnas)] for _f in range(cantidad_filas)]

def multiplicar_matrices(matriz_a, matriz_b):
    cantidad_filas_matriz_a = len(matriz_a)
    cantidad_columnas_matriz_b = len(matriz_b[0]) 

    matriz_resultante = crear_matriz_2(
        cantidad_filas_matriz_a, cantidad_columnas_matriz_b
    )
   
    for i in range(cantidad_filas_matriz_a):
        for j in range(cantidad_columnas_matriz_b):
            for k in range(len(matriz_b)):
                matriz_resultante[i][j] +=  matriz_a[i][k] * matriz_b[k][j]
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


#suma 2 matrices

def crear_matriz_2(cantidad_filas, cantidad_columnas):
    return [[0 for _c in range(cantidad_columnas)] for _f in range(cantidad_filas)]

def sumamatrix(mat1,mat2):                                      #función suma
    cantidad_filas = len(mat1)                                  #define longitud de fila
    cantidad_columnas = len(mat2[0])                            #define longitud columna
    matriz_resultante = crear_matriz_2(cantidad_filas,cantidad_columnas) #matriz resultado de la suma
    for i in range(cantidad_filas):                             #recorrer filas
        for j in range(cantidad_columnas):                      #recorrer columnas
            matriz_resultante[i][j] = mat1[i][j] + mat2[i][j]   #suma de matrices
    #for _ in matriz_resultante:
    print(matriz_resultante)

# 3x3 matrix
matriz_a = [[4,12,7,3],
    [4,6,5,6],
    [7,6,8,9]]

# 3x4 matrix
matriz_b = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

sumamatrix(matriz_a,matriz_b)

m = [[1,2], [3,4], [5,6]]
for f in range(3):
    for c in range(2):
        result = m[f][c]
        print(result)
    print("otracosa")
    print()