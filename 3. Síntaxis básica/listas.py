lista = [
	1,	# 0
	True, # 1
	None,	# 2
	"Hola mundo",	# 3
	{"key":"value"},	# 4
	(1,2,3,4,5)	# 5
]	# Las listas son dinámicas por lo que puedes
	# reasignar, añadir o eliminar los valores que la componen

print(lista)

# Para escoger elemento en específico solo debes colocar su indice
print(lista[3])	# El primer elemento siempre va a tener indice 0

print(len(lista))	# No debes confundir los indices con el número de elementos

print(lista[3:5])	# Puedes escoger elementos en un rango de indices
# En este caso imprimimos desde el indice 3 hasta el indice 5

lista[3:]	# Desde el tercer elemento hasta el final
lista[:3]	# Desde el primer elemento hasta el tercero

print(lista[-1])	# Si colocas un índice negativo va a contar los elementos
# Desde el último, en este caso imprime el último elemento


lista.append("Nuevo elemento") # El método append integra un elemento al final de la lista
# Puede ser cualquier tipo de elemento
print(lista)

lista.insert(2, "Introduciendo elemento en un índice en específico")
print(lista) # Con insert integras el elemento en un índice en especifico

lista.extend([False, 3.1415]) # Con este método podrás añadir varios elementos 
# al final de la lista
print(lista)

print(lista.index(3.1415))	# Nos devuelve el indice de un elemento en especifico
print(lista[lista.index(3.1415)])

print(3.1415 in lista) # Verificar si un elemento existe dentro de una lista

lista.remove(3.1415) # Eliminando un elemento
print(3.1415 in lista)

print(lista)
lista.pop()	# Elimina el último elemento de la lista
print(lista)

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3= lista1 + lista2
# Uniendo dos listas diferentes
print(lista3)

repetidor = [1,2,3] * 3 #Repite esta lista 3 veces
# Dentro de una misma lista
print(repetidor)