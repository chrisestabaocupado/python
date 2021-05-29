def fact(x):
	if x == 1:	# Si no le envia un caso base, esta función podría ser infinita
		return 1
	else:
		return x * fact(x-1) # Al referenciar la propia función, como parámetro se envia el caso base
# que vendría siendo la versión más simple del problema

print(fact(5))

# La recursión también puede ser indirecta, por lo que una función
# podría llamar a otra