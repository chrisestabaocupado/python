# La programación funcional, como dice el nombre es aquella que se basa en funciones
# existen dos tipos de funciones, las puras y las no puras
# las funciones puras son aquellas que van a retornar un valor que solo depende de los
# argumentos requeridos por la función misma
# un ejemplo de funciones puras son las funciones a continuación

def func(f, x):	# Esta funcion es una función de orden superior
# las funciones de orden superior son aquellas que reciben a otras funciones como parámetro
# o las retornan como resultado
	return f(x)	
def suma(x):
	return x + x
print(func(suma, 2))

# sin embargo las funciones que son puras son aquellas que por ejemplo modifiquen el 
# estado de otro elemento
# como por ejemplo
lista = []
def añadir(x,y):
	x.append(y)
añadir(lista, "Hola mundo")
print(lista)