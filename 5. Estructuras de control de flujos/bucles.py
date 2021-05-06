# Bucles determinados: son aquellos en los cuales
# solo leyendo el código podemos saber cuantas veces
# se va a ejecutar el bucle

# Bucles indeterminados: aquellos que dependen de variables
# externas y por ende no podemos saber de primera mano cuantas
# veces se va a ejecutar


# Bucle for (determinado)
y = ["Carlos", "Daniela", "Bernado"]
for i in y:	# Por cada elemento en el array "y"
	print("Nombre:", i, "\n") # Imprime en consola

for i in range(0,10):
	print(i)