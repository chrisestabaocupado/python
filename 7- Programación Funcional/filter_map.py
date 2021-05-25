# map es una función de orden superior que recibe un iterable y una función
# y aplica la función a cada uno de los elementos del iterable
# podemos convertir el resultado con list y tuple en otro iterable
x = ["chris", "alex"]
y = list(map(lambda x: x.upper(), x)) # para facilitar las cosas se puede utilizar la sintaxis lambda

print(y)

# filter es otra función de orden superior que lo que hace es filtrar
# un iterable según una una función que devuelva un booleano

# una forma de verlo es que a la función filter le envias una función pura que evalua algo como
# x == "hola"
# y le proporcionas un array ["hola", "mundo"]
# la función filter va a pasar por cada uno de los elementos dentro del array y si la función del comienzo
# devuelve false al pasar por alguno de los elementos entonces este será eliminado
# en este caso solo va a devolver el primer elemento

# aquí otro ejemplo con la lista que creamos al principio
y = list(filter(lambda x: x.startswith("c"), x))

print(y)