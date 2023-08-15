# Funciones para operar sobre una lista
'''
Generar una lista con 10 valores enteros aleatorios entre 1 y 20 (se puede usar randint() del módulo random). Luego:

1-Muestre la lista
2-El usuario ingresa debe ingresar un valor un valor. El programa debe informar cuántos valores de la lista son mayores a dicho valor, para eso debe utilizar una función. La función debe recibir como argumentos la lista y un entero, y debe retornar la cantidad de valores de la lista mayores a dicho entero.
3-Crear una función que calcule el promedio de la lista y utilizarla.
4-Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne.
'''
# Informar valores mayores
def informar_cant_mayores (min,lista):
    cant_mayores=0
    for elem in lista:
        if elem>min:
            cant_mayores+=1
    return cant_mayores

# Promedio lista
def promediar_lista (lista):
    suma=0
    for elem in lista:
        suma=suma+elem
    prom=suma/len(lista)
    return prom    

# Encontrar min y max de lista
def encontrar_min_max(lista):
    max=lista[0]
    min=lista[0]
    for elem in lista:
        if max<elem:
            max=elem
        if min>elem:
            min=elem 
    return {
        "maximo" : max,
        "minimo" : min
        }


import random
# Genero la lista
lista=[]
# Cargo la lista
for i in range (0,10):
    lista.append(random.randint(1,20))

# Muesto la lista
print(lista)

# Ingresar valor
valor=int(input("Ingrese un valor: "))

# LLamar funciones

print(f"La cantidad de números en la lista mayores a {valor} son {informar_cant_mayores(valor,lista)}")
print(f"El promedio de los valores de la lista es: {promediar_lista(lista)}")

min_max=encontrar_min_max(lista)
print(f'El valor maximo de la lista es {min_max["maximo"]} y el valor minimo es {min_max["minimo"]}')







