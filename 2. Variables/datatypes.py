# Strings 
# "String", 'String', """String""", '''String'''
print(type("""
Este es un 
string multilinea
"""))
# La función type nos devulve el tipo de dato del
# parámetro que le enviamos
print("Hola"+ " " + "mundo") # Concatenación


# Números

# Integer (Enteros)
print(type(100))
# Float (Decimales o punto flotante)
print(type(3.1415))

# Booleans (Tipo de dato lógico)
print(type(True))
print(type(False))

# Listas
# [1,2,3,4,...,n]
print(type([1,2,3,4]))

# Tuplas: los elementos que conforman a 
# las tuplas son inmutables a diferencia de las listas
# (1,2,3,4,...,n)
print(type((1,2,3,4)))

# Diccionarios
# "key" : "value"
print(type({
	"nombre" : "Ryan",
	"apellido" : "Gómez",
	"apodo" : "Alex"
}))

# None
print(type(None))