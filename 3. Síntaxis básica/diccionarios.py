diccionario = {
	"clave":"valor",
	"clave_2":"valor_2",
	"clave_3":"valor_3"
}	# Se le asigna un nombre clave a un valor para poder llamarlo más adelante
print(type(diccionario))

print(diccionario["clave_2"])	# Esta es la forma de llamar a un valor dentro
# de un diccionario

diccionario["clave_4"]="valor_4" # Añadiendo un nuevo par clave:valor

print(diccionario)

# No pueden haber dos claves iguales, en cambio python sobreescribe

diccionario["clave_4"]="nuevo_valor_4"	# Reasignando valores
print(diccionario["clave_4"])

del diccionario["clave_4"]	# Eliminando un elemento del diccionario
# palabra reservada "del"
print(diccionario)

tupla = (1,2,3,4)	# Puedes usar tanto listas como tuplas para asignar
# claves a los valores dentro del diccionario
diccionario = {
	tupla[0]: "Uno",
	tupla[1]: "Dos",
	tupla[2]: "Tres",
	tupla[3]: "Cuatro"
}
print(diccionario[1])
# o
print(diccionario[tupla[0]])

diccionarioPrincipal = {
	"diccionario":{
		1	:	[1,2,3,4,5]
	}
}	# Almacenando un diccionario dentro de otro diccionario
print(diccionarioPrincipal["diccionario"])

print(diccionario.keys())	# Imprimiento claves
print(diccionario.values())	# Imprimiendo valores
print(len(diccionario))	# Numero de pares dentro del diccionario