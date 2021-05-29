tupla = ("Juan", 1, False)	# Las tuplas son listas inmutables
print(tupla[0])

lista = list(tupla)	# Para convertir una tupla en una lista
lista.append("Nuevo elemento de mi lista")	# Verificamos que es
# Una lista porque podemos añadir elementos
print(lista)

tupla = tuple(lista)	# Convirtiendo lista en tupla
print(tupla)

if("Juan" in tupla):	# Verificando si un elemento
# Está dentro de una lista
	print("Juan está en la tupla")
else:
	print("Juan no está en la tupla")

print(tupla.count("Juan"))	# Contar cuantos elementos hay
# dentro de la tupla

tupla_unitaria = ("Juan",) #Una tupla unitaria siempre lleva
# una coma despues de su único elemento

tupla = "Juan", "Alberto", "Chris"
# Al declarar una tupla sin los parentesis el interprete procede
# a hacer el empaquetado de tupla

print(tupla)
print(type(tupla))	# Verificamos que es una tupla

per1, per2, per3 = tupla # Desempaquetado de tupla
# Asigna a cada variable un valor de la tupla en el orden en el que aparecen
# per1 = "Juan"
# per2 = "Alberto"
# per3 = "Chris"
print(per1, per2, per3)

print(tupla.index("Juan"))	# Buscar index de un elemento
# Dentro de un array