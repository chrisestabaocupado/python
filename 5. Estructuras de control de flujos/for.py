# Bucles determinados: son aquellos en los cuales
# solo leyendo el código podemos saber cuantas veces
# se va a ejecutar el bucle

# Bucles indeterminados: aquellos que dependen de variables
# externas y por ende no podemos saber de primera mano cuantas
# veces se va a ejecutar


# Bucle for (determinado)
y = ["Carlos", "Daniela", "Bernado"]

for i in y:	# Por cada elemento en el array "y"
	print("Nombre:", i) # Imprime en consola

print("")

for i in range(0,3):	# Imprimiendo elementos especificos de un array
	print(y[i])			# dentro de un rango en específico

print("")

string = "Juan"

for i in string:	# Imprimiendo letra por letra el string
	print(i)


for i in y:
	print(i, end=" ")	# En vez de imprimir linea por linea imprime todo al final
						# El valor de end se muestra entre cada uno de los elementos
						# en este caos entre cada elemento se coloca un espacio

print("")

for i in range(5, 25, 5):	# El tercer argumento dicta de cuanto en cuanto
	print(i)				# se lleva el conteo, en este caso de 5 en 5
							# El 25 es excluido

for i in range(0,5):
	if i == 4:
		continue		# Si el numero es igual a 4 entonces saltalo y continua con el bucle
	else:
		print(i)