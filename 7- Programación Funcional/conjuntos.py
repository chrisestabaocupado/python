conjunto = {1,2,3,4,5}
otro_conjunto = set([1,2,3,4,5])
# los conjuntos comparten elementos con las listas, por ejemeplo el len
print(3 in otro_conjunto)
print("culo" not in conjunto)

# pero no están ordenados, por lo que no pueden ser indexados
# no pueden contener elementos duplicados
# por la forma en la que son almacenados es más rapido verificar si un
# elemento forma parte del conjunto
conjunto.add("culo")
print(conjunto)
conjunto.remove(1)
print(conjunto)
conjunto.pop()	# pop elimina un elemento arbitrariamente
print(conjunto)


x = set([1,2,3,4,5])
y = set([6,7,8,9,10])

print(x | y) # (unión) une los dos conjuntos
print(x - y) # (diferencia) devuelve los elementos que están en el primero pero no en el segundo
print(x ^ y) #(diferencia simétrica)
# devuelve los elementos que están en cualquiera de los dos pero no en ambos