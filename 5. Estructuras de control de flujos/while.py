# Bucle while (indeterminado)
i = 0			# Imprimiendo los numeros del 0 al 9
while i <= 9:	# Mientras que i sea MENOR O IGUAL QUE 9
	print(i)	# Imprime el valor de i
	i+=1 		# Y aumenta su valor
# En caso de que el valor de i que es el contador no aumente se puede crear
# un bucle infinito, debes tener mucho cuidado, la condición debe de cumplirse 
# en algún momento

print("Terminó el bucle\n")

numero = int(input("Introduce un numero: "))
intentos = 2

if(numero < 0):
	while intentos < 4:

		numero = int(input("Por favor introduce un número mayor que 0: "))

		if numero > 0:
			print("\nPerfecto, gracias")
			break
		elif numero < 0:
			intentos +=1

		if intentos == 4:
			print("\nHa realizado muchos intentos, el programa ha finalizado")