# Listas


lista = ["Manuel", 23, "Hola Mundo", 3.14, True]

print (lista[0])

lista[0] = "Christopher"
lista.append("Nuevo dato") # Agregar un nuevo valor a la lista

print (lista[0]) # En las listas puedes cambiar el valor de cualquier elemento
# Eso es lo que diferencia las tuplas de las listas


lista_1 = ['uno', 'dos', 'tres']
lista_2 = ['cuatro', 'cinco', 'seis']

lista_concatenada = lista_1 + lista_2 # Concatenación de listas
# También aplica para tuplas
print (lista_concatenada)


#Tuplas


tupla = ("Manuel", "Rosa", "Pepito", 45, 3.14) # Las tuplas son inmutables
# tupla[0] = "NO SE PUEDE HACER ESTO"
print (tupla)

# Esto de abajo también aplica con las listas
print (tupla[1:4]) # Desde un index hasta la posición indicada menos 1
print (tupla[1:]) # Desde un index hasta el final
print (tupla[:4])
print (tupla * 2) # Repetirlo una cantidad de veces


# Diccionarios

diccionario = {
    "1": "Manuel",
    2: "Fernando",
    "3": "Mario"
}
print (diccionario[2])

diccionario[2] = "Christopher" # Puedes cambiar el valor de cualquier clave
print (diccionario[2])

# keys()
print ("Obtener las claves de un diccionario:", diccionario.keys())
# values()
print ("Obtener los valores de un diccionario:", diccionario.values())