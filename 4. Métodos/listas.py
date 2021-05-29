

# Métodos de Agregado

print ('----')

# Agregar un elemento al final de la lista
nombres_masculinos = ["Alvaro", "Jacinto", "Edgardo", "David"]
nombres_masculinos.append("Jose")
print (nombres_masculinos)
# ['Alvaro', 'David', 'Edgardo', 'Jacinto', 'Jose', 'Ricky', 'Jose']
# Método: append(“nuevo elemento”)

print ('----')

#Agregar varios elementos al final de la lista
nombres_masculinos.extend(["Jose", "Gerardo"])
print (nombres_masculinos)
#['Alvaro', 'David', 'Edgardo', 'Jacinto', 'Jose', 'Ricky', 'Jose', 'Jose','Gerardo']
# Método: extend(otra_lista)

print ('----')

# Agregar un elemento en una posición determinada
nombres_masculinos.insert(0, "Ricky")
print (nombres_masculinos)
# Método: insert(posición, “nuevo elemento”)
# ['Ricky', 'Alvaro', 'David', 'Edgardo', 'Jacinto', 'Jose', 'Ricky', 'Jose', 'Jose', 'Gerardo']

print ('----')

# Métodos de eliminación:

print ('----')

# Eliminar el último elemento de la lista
nombres_masculinos.pop() # 'Gerardo'
# Retorna: el elemento eliminado
print (nombres_masculinos)
# ['Ricky', 'Alvaro', 'David', 'Edgardo', 'Jacinto', 'Jose', 'Ricky', 'Jose', 'Jose']
# Método: pop()

print ('----')

# Eliminar un elemento por su índice
nombres_masculinos.pop(3) # 'Edgardo'
# Retorna: el elemento eliminado
print (nombres_masculinos)
# ['Ricky', 'Alvaro', 'David', 'Jacinto', 'Jose', 'Ricky', 'Jose', 'Jose']
# Método: pop(índice)

print ('----')

# Eliminar un elemento por su valor
# Método: remove(“valor”)
nombres_masculinos.remove("Jose")
print (nombres_masculinos)
# ['Ricky', 'Alvaro', 'David', 'Jacinto', 'Ricky', 'Jose']

print ('----')

# Ordenar una lista en reversa (invertir orden)
# Método: reverse()
nombres_masculinos.reverse()
print (nombres_masculinos)
# ['Jose', 'Jose', 'Ricky', 'Jacinto', 'David', 'Alvaro', 'Ricky']

print ('----')

# Ordenar una lista en forma ascendente
# Método: sort()
nombres_masculinos.sort()
print (nombres_masculinos)
# ['Alvaro', 'David', 'Jacinto', 'Jose', 'Ricky']

print ('----')

# Ordenar una lista en forma descendente
# Método: sort(reverse=True)
nombres_masculinos.sort(reverse=True)
print (nombres_masculinos)
# ['Ricky', 'Jose', 'Jacinto', 'David', 'Alvaro']

print ('----')


# Métodos de búsqueda


# Contar la canditad de apariciones de elementos
# Método: count(element)
nombres_masculinos = ["Alvaro", "Miguel", "Edgardo", "David", "Miguel"]
print (nombres_masculinos.count('Miguel'))
# 2

print ('----')

# Obtener número de índice
# Método: index(elemento[indice_incio, indice_fin])
print (nombres_masculinos.index("Miguel"))
print (nombres_masculinos.index("Miguel", 2, 5))

print ('----')