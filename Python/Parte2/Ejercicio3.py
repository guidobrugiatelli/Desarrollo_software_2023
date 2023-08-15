"""
Utilizar la función anterior para generar y almacenar una lista de atletas
Escribir una función que reciba la lista de atletas e imprima una línea por cada atleta respetando el siguiente formato: "<num_atleta> - : (<tiempo_llegada> segundos)", donde <num_atleta> es el número del atleta, su nombre y <tiempo_llegadad> su tiempo de llegada.
Escribir una función que devuelva el número del atleta que resultó ganador.
Escribir una función que, recibiendo el número de atleta de un competidor, devuelva todos sus datos (nombre, número y tiempo de llegadad).
OPCIONAL: Escribir una función que devuelva una tupla con los números de los 3 atletas que entraron al podio de ganadores en orden de llegada.
"""

import random

def buscar_atleta(num):
	for atleta in atletas:
		if num==atleta['numero']:
			return atleta

def mostrar_ganador():
	ganador=atletas[0]
	for atleta in atletas:
		if ganador['tiempo_llegada']>atleta['tiempo_llegada']:
			ganador=atleta
	return ganador['numero']

def mostrar_lista():
	for atleta in atletas:
		print(f"<{atleta['numero']}> - : (<{atleta['tiempo_llegada']:.2f}> segundos)")

def generar_lista_de_atletas():
	"""
	Esta función genera aleatoriamente los datos de 20 atletas que participaron de una maratón.
	Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
		- nombre: el nombre del atleta
		- numero: el número con el que participó en la maratón
		- tiempo_llegada: la cantidad de segundos que tardó en llegar
	"""
	lista_atletas = []
	nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
	apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')	
	for i in range(1, 21):
		atleta = {
			"nombre": random.choice(nombres)+" "+random.choice(apellidos),
			"numero": i,
			"tiempo_llegada": random.random()*120
		}
		lista_atletas.append(atleta)
	return lista_atletas

atletas= generar_lista_de_atletas()
mostrar_lista()
print(f"El atleta ganador fue {mostrar_ganador()}")
num_atleta=int(input("Ingresar el numero de un atleta: "))
print(buscar_atleta(num_atleta))

