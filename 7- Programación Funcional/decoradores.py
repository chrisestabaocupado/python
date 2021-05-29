# los decoradores ofrecen maneras de modificar una función
# utilizando otras funciones, esto sirve para añadir funcionalidades
# a otras funciones sin tener que modificarlas

def decor(func):
	def wrap():
		print("====")
		func()
		print("====")
	return wrap

def decor2(func):
	def wrap():
		func()
		print("Hola mundo")
	return wrap

@decor
@decor2
# Esta es la sintaxis para decorar la función que le pasas abajo
# es como decor(saludo)
# una sola función puede tener varios decoradores
def saludo():
	print("Hello world")

saludo()