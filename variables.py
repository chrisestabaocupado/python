# Variables

"""Comentario de
varias líneas"""
constante = 10

# Comentario de una sola línea

otra_constante = 20  # Otro comentario

# TODO esto es algo por hacer
# FIXME esto es algo que debe corregirse
# XXX esto también, es algo que debe corregirse

string = "Hola, soy un string"
print (string)

string = "Y yo otro string"
# El valor de una variable puede cambiar a lo largo del programa
print (string)

a, b, c = 1, 2, 3 # Distintas variables en una misma linea
print ('Los valores de las variables "a", "b" y "c":', a, b, c)

del a, b, c, string # Eliminando variables

string = "Cadena de Texto"
integer = 12
float = 3.14
PI = 3.1415 # Los nombres de los valores que nunca van a cambair se escriben en mayúsculas
# -----

concatenar = string + " " + str(integer) + " " + str(float) # El método srt() convierte cualquier tipo de dato 
# En un string
print (concatenar)

# -----
string = "1"
integer = 1

total = int(string) + integer # El método int() convierte un string en un entero
print ("El total es:", total)

cadena_multilineal = """
Esta
Es
Una
Cadena
Multilineal
"""  # Texto que se compone de más de una fila
print (cadena_multilineal)