try:
	archivo = open("./files/archivo.txt", "r+")
	print(archivo.read())
finally:
	archivo.close()
# Una buena practica para ahorrar recursos es asergurarse de que
# los archivos siempre se cierren

# otra forma de hacerlo es creando una variable provicional
# la cual será eliminada al ejecutarse el código en el interior del bloque

with open("./files/multilinea.txt", "r") as f:
	print(f.readlines())