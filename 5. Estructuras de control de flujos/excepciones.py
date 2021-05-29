def division(num1, num2):
	try:	# Intenta realizar la divisón
		return num1/num2
	except ZeroDivisionError:	# Si ocurre este error en especifico
		print("No se puede dividir entre 0")
		return "Operación erronea"	# Haz esto
	except TypeError:
		return "Tipo de dato incorrecto"

print(division(1,"2"))

try:
	word = "foo"
	print(word/0)
except:	# Si no indidcas un error en específico
	print("Manejando excepciones")	# Reaccionará de esta forma a cualquier
	# error que se produzca

try:
	print(10/2)
except:
	print("Ha ocurrido un error")
finally:	# El código dentro de una sentencia finally
	print("Todo listo")	# se ejecutará luego del bloque try
	# y si ocurre una excepción se ejecutará luego del bloque except

print(1)
# raise TypeError("Ha ocurrido un error") con raise se puede levantar un error en especifico
# a su vez se le puede pasar un argumento detallando el error
print(2)

assert 2+1 == 3 # si la expresión es falsa entonces se levantará un error
assert 1<3, "Uno no es mayor que tres" # También se le puede enviar un segundo argumento
# el cual es enviado junto con el assertion error

# Si la expresión es verdadera se seguirá ejecutando el código normalmente