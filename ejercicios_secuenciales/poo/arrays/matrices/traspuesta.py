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