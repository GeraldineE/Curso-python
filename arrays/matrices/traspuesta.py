matriz = [[i]*2 for i in range(3)]
 
def print_r(matriz):
    for fila in matriz:
        print(fila)
 
def transpuesta(matriz):
    rows = len(matriz)
    cols = len(matriz[0])
    return [[matriz[j][i] for j in range(rows)] for i in range(cols)]
 
print("Original")
print_r(matriz)
print("TRANSPUESTA")
print_r(transpuesta(matriz))


def transpuesta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
mat_1= [[1,2,3],[4,5,6]]

print("Esta es la matriz original",mat_1)
matriz_resultado=transpuesta(mat_1)
print("Esta es la transpuesta",matriz_resultado)