import random


lista_numeros = []
for elemento in range(1,11):
    lista_numeros.append(random.randint(1,10))
for i in lista_numeros:
    print(i)

    
numeros = []
lista = []

for i in range(0,100):
    numeros.append(i)
    if i%2 != 0:
        lista.append(i)
print(lista)