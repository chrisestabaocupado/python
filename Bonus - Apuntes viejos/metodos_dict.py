# Métodos de eliminación


# Vaciar un diccionario
# Método: clear()
diccionario = {
    "color":"violeta",
    "talla":"XS",
    "precio":174.25
}
print (diccionario)

diccionario.clear()
print(diccionario)
diccionario = {"color": "violeta", "talle": "XS", "precio": 174.25}

print ("----")


# Métodos de agregado y creación


#Copiar un diccionario
# Método: copy()
copia = diccionario.copy()
diccionario.clear()
print (copia)

copia2 = copia
copia.clear()
print (copia2)

print ("----")

# Crear un nuevo diccionario desde las claves de una secuencia
# Método: dict.fromkeys(secuencia, 'valor por defecto)

secuencia = ["color", "talla", "marca"]
diccionario1 = dict.fromkeys(secuencia)
print (diccionario1)

diccionario2 = dict.fromkeys(secuencia, "Value by default")
print (diccionario2)

print ("----")

# Concadenar diccionarios
# Método: update(diccionario)
diccionario1 = {"color": "verde", "precio": 45}
diccionario2 = {"talla": "M", "marca": "Lacoste"}
diccionario1.update(diccionario2)
print (diccionario1)

print ("----")

# Establecer una clave y valor por defecto
# Método: setdefault("clave", "valor")
franela = {"color": "rosa", "marca": "Zara"}
clave = franela.setdefault("talla", "U")
print ("Value: " + clave)
print (franela)

print ("----")


# Métodos de retorno


# Obtener el valor de una clave
# Método: get(clave, "valor por defecto si la clave no existe")
print (franela.get("color"))
print (franela.get("stock"))

print ("----")

# Obtener las claves de un diccionario
# Método: keys()
claves = franela.keys()
print (claves)

print ("----")

# Obtener los valores de un diccionario
# Método: values()
valores = franela.values()
print (valores)

print ("----")
