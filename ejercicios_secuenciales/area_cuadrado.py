# EJERICIO: Dado un lado hallar el area de un cuadrado
# ANALISIS: 
# En este ejercicio vamos a calcular el area del cuadrado
# como el cuadrado tiene lados iguales, no importa si tienes la base o altura 
# las dos tienen el mismo valor
# ¿COMO VAMOS A CALCULAR EL AREA DE UN CUADRADO?
# SOLUCIÓN
# Segun la formula matematica el area de un cuadrado se calcula:
# area = lado * lado

# Creamos una funcion llamada area_cuadrado, esta recibe el tamaño del lado
# Dentro de esta funcion implementamos el analisis que hicimos previamente, es decir;
# area = lado * lado
# Y retornamos(devolvemos) el resultado, con el return podemos devolver el valor

def area_cuadrado(lado):
    area = lado * lado
    return area

# aca llamamos la funcion imprimiendo su resultado
print(area_cuadrado(4))
