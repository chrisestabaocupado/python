x = 19
y = 5

if x > y:	# Si x > y = True
	print(x, "es mayor que", y)	# Entonces haz esto
else:	# Si x < y = True
	print(x, "es menor que", y) # Entonces haz esto


# Ejemplo
print("---")
print("Bienvenido al programa de valoración en Python\n")

nota = input("Inserte la nota obtenida en el exámen: ")
nota = int(nota) # La función input nos permite almacenar datos enviados por consola
# en una variable, pero el elemento recibido es un string
# por ende debemos convertirlo al respectivo tipo de dato que necesitemos

def valoracion(nota):
	if nota < 10:	# Si la nota es menor que 10
		print("Usted reprobó el exámen\n") # El alumno reprobó
	elif nota == 10:	# Sino es menor que 10, verifica Si la nota es igual a 10
		print("Usted casi reprueba, debe esforzarse más\n")	# Si eso es verdad, dale una advertencia
	elif nota == 20:	# Si no es igual a 10, verifica si la nota es igual a 20
		print("Excelente trabajo, siga así\n")	# Si eso es verdad fecilitalo
	else:	# Si no se cumple ninguna de las condiciones anteriores entonces el alumno aprobó
		print("Usted aprobó el exámen\n")	# Haz esto

valoracion(nota)

# Otro ejemplo

edad = -7
# Concatenación de operadores de comparación
if 0<edad<1==10==-10: # Si la edad es mayor que 0 o si es mayor que 1
	print("Edad correcta")
else:# Este código no tiene sentido pero es un ejemplo de que se pueden colocar tantos
# operadores como necesites
	print("Edad incorrecta")