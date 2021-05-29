# los lambdas son funciones que podemos crear sobre la marcha y no se asocian a una variable
def x(y):	# Este es un ejemplo de una función normal
	return y

def func(x, y):
	return x(y)

print(func(lambda x: x+x, 2)) # Este es un ejemplod de una lambda
# la función se creó en la misma llamada pero no podrá ser reutilizada a posterior
# se suelen utilizar más que nada cuando otra función recibe una función como parámetro
# y no suelen pasar de una línea de código

# una forma de poder llamar estas funciones a posterior es asignandolas a una variable
a = lambda x: x*x
print(a(2))
# también se le pueden asignar valores por defecto a los parámetros
a = (lambda x: x+x)(2)
print(a)