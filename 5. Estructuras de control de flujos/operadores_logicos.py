x = 98
if x > 0 and x < 99: # SI x ES MENOR que 0 Y ES MENOR que 99
	print(True)	# Entonces imprime esto
else:	# Si no se cumple ambas condiciones
	print(False)

if x == 100 or x < 0:	# SI x ES IGUAL a 100 o MENOR QUE 0
	print(True)	# Entonces imprime esto
else:	# Si no se cumple al menos una de las dos condiciones
	print(False)	# Entonces has esto

# Se pueden colocar tantos operadores lógicos como necesites

tupla = (1, 2)

if None in tupla:	# Si el elemento none está en la tupla
# Entonces ejecuta el código
	print("Sí está")
else:
	print("No está")