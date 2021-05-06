# Las variables son un nombre símbolico para un dato reutilizable
nombre = "Ryan"
print(nombre) # Para referencia una variable solo debes escribir su nombre

# Las variables pueden contener cualquier tipo de dato
diccionario = {
	"key" : "value"
}

# Python tiene case sensitive, por lo que las variables a continuación
# son variables completamente diferentes
libro =	"Shogun"
Libro = "Hunger games"

# Puedes declarar varias variables en una misma linea
nombre, apellido = "Ryan", "Guerra"
print(nombre, apellido) # Tambien las puedes imprimir de esta forma
# La coma (",") cuenta como un espacio

# Las constantes deben escribirse en mayúsculas
# Esto no significa nada para el interprete pero es una buena práctica
MY_NAME = "Chris"

# Al ser un lenguaje de tipado dinamico el valor de las 
# variables puede ser reasignado facilmente
MY_NAME = "Jake"

print(f"Mi nombre es: {MY_NAME}") # Esta es una forma de mostrar una variable dentro de un string
print("Mi nombre es: {MY_NAME}") # Si no colocas la f antes del string va a tomar el texto literal
print("Mi nombre es: {0}".format(MY_NAME)) # Utilizando el método format también se puede introducir
# Variables dentro de un string
print("Mi nombre es", MY_NAME)