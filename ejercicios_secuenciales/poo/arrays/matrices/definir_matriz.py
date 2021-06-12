# Crear una matriz


def crear_matriz_problema_de_referencia_1(cantidad_filas, cantidad_columnas):
    return [[0] * cantidad_columnas] * cantidad_filas


print("crear_matriz_problema_de_referencia_1")
mi_matriz = crear_matriz_problema_de_referencia_1(3, 4)
print("antes")
print(mi_matriz)
mi_matriz[0][0] = 3
mi_matriz[1][2] = 2
print("despues")
print(mi_matriz)
print("")


def crear_matriz_1(cantidad_filas, cantidad_columnas):
    return [[0] * cantidad_columnas for _ in range(cantidad_filas)]


print("crear_matriz_1")
mi_matriz = crear_matriz_1(3, 4)
print("antes")
print(mi_matriz)
mi_matriz[0][0] = 2
mi_matriz[1][2] = 3
print("despues")
print(mi_matriz)
print("")


def crear_matriz_2(cantidad_filas, cantidad_columnas):
    return [[0 for _c in range(cantidad_columnas)] for _f in range(cantidad_filas)]


print("crear_matriz_2")
mi_matriz = crear_matriz_2(3, 4)
print("antes")
print(mi_matriz)
mi_matriz[0][0] = 2
mi_matriz[1][2] = 3
print("despues")
print(mi_matriz)
print("")
