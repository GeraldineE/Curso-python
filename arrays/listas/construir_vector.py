#Reto 1 variante 1

import random

def construir_vector(largo_del_vector):
    V = []
    for _ in range(largo_del_vector):
        V.append(random.randint(1, 99))
    return V
print(construir_vector(5))

def es_capicua(numero):
    numero_en_texto = str(numero)
    return numero_en_texto == numero_en_texto[::-1]

def comienza_con_digito_par(numero):
    primer_digito = int(str(numero)[0])
    return primer_digito % 2 == 0

# se genera un numero entre 15 y 30
largo_del_vector = random.randint(15, 30)

vector_de_numeros = []
for _ in range(largo_del_vector):
    vector_de_numeros.append(random.randint(1, 99999))

total = 0
vector_capicuas_o_primer_digito_par = []
for numero in vector_de_numeros:
    if es_capicua(numero) or comienza_con_digito_par(numero):
        vector_capicuas_o_primer_digito_par.append(numero)
total = sum(vector_capicuas_o_primer_digito_par)

print("Vector de numeros:")
print(vector_de_numeros)
print("Vector de numeros capicuas o que comienzan con par:")
print(vector_capicuas_o_primer_digito_par)
print("Total de la sumatoria del vector de numeros capicuas o que comienzan con par:")
print(total)