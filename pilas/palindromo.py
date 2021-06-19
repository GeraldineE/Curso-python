palabra = input("Ingrese la palabra a operar:")
#se crea una lista, pero se utilizará como una pila con las funciones pop() y append()
pila1 = list(palabra) #se usa la funcion list() para convertir cada letra de la palabra en un elemento de la pila
#se declaran las listas vacias para poder despues introducir valores en ellas sin problemas
pila2 = []
pila3 = []
#se utiliza la lógica de asumir que SI es un palindromo hasta que se demuestre lo contrario en caso de no serlo
palindromo = True
#primero, toma la pila1 original y la copia de forma invertida a pila2 y pila3
for i in range(len(pila1)):
    aux = pila1.pop() #guarda el valor del tope de "pila1" en "aux" y a la vez retira el valor de dicha pila
    pila2.append(aux) #asigna el valor de "aux" en el final de la "pila2"
    pila3.append(aux) #guarda el mismo valor ahora en "pila3"
'''regresa los valores de "pila2" a "pila1"
ahora existiran "pila1" con los valores originales y "pila3" con los valores invertidos'''
for i in range(len(pila2)):
    aux = pila2.pop()   
    pila1.append(aux)
'''Ahora se comparara letra por letra con la función pop() de las pilas 1 y 3
si resulta que todas las palabras son iguales al sacarlas de las pilas
entonces es un palindromo, si falla en una o mas, entonces no lo es'''
for i in range(len(pila3)):
    aux = pila1.pop()
    aux2 = pila3.pop()
    if (aux != aux2): #Este if anidado compara la igualdad entre "aux1" y "aux2"
        palindromo = False
if (palindromo == True): #Se muestra al usuario el resultado final
    print("La palabra indroducida SI es un palindromo")
else:
    print("La palabra indroducida NO es un palindromo")