# Este generador genera numeros pares hasta el limite que se le de
def pares(limite):
	num = 2
	while num < limite:
		yield num
		num+=2

# Para poder utilizarlo debemos guardarlo en un objeto
devuelvePares = pares(12)	# Solo se van a poder generar numeros 5 veces

# Y luego llamarlo con la función next
print(next(devuelvePares))	# 2
print("")
print(next(devuelvePares))	# 4
print("")
print(next(devuelvePares))	# 6
print("")
print(next(devuelvePares))	# 8
print("")
print(next(devuelvePares))	# 10: A partir de aqui no se pueden generar más numeros

# Es útil a la hora de generar valores infinitos
# cuando es necesario devolver un valor se puede utilizar
# una función tradicional