# Una funcion es una estructura de código reutilizable
# Que permite realizar ciertas acciones

def saluda(): # Una funcion simple
    # return ("Hola mundo")
    print ("Hola mundo")
# print (saluda())


saluda()

print ("\n\n")

def multiplicar(numero1, numero2): # Argumentos o parámetros
    return numero1 * numero2

numero1 = input("Introduzca el primer número: ")
numero2 = input("Introduzca el segundo número: ")
numero1 = float(numero1)
numero2 = float(numero2)


print (multiplicar(numero1, numero2))

print ("\n\n")

# Funcion con argumento opcional
def sumar (num1, num2=0):
    return num1 + num2

print (sumar(3, 10))


# Funcion con argumento array
def array (arr):
    resultado = ''
    for value in arr:
        resultado += str(value)
    return resultado

print (array(["Python", "Hola", 10, 34.4]))


print ("\n\n")

# Keywords como parámetros
def funcion (nombre, apellido):
    print ("Hola", nombre, apellido)

    
funcion(nombre="Christopher", apellido="Glood") # Parámetros como par clave=valor


# Cuando la cantidad de parametros es desconocida
def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios):
    print (parametro_fijo)
# Los parámetros arbitrarios se corren como tuplas
    for argumento in arbitrarios:
        print (argumento)

recorrer_parametros_arbitrarios('Fixed', 'arbitrario 1', 'arbitrario 2', 'arbitrario 3')


print ("\n\n")


def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios, **kwords):
    print (parametro_fijo)
    for argumento in arbitrarios:
        print (argumento)
# Los argumentos arbitrarios tipo clave, se recorren como los diccionarios
    for clave in kwords:
        print ("El valor de", clave, "es", kwords[clave])
    
    
recorrer_parametros_arbitrarios("Fixed", "arbitrario 1", "arbitrario 2", "arbitrario 3", clave1="valor uno", clave2="valor dos")


print ("\n\n")


def funcion (num1, num2):
    return num1 + num2

datos = [1, 1]
print (funcion(*datos))

datos = (1, 1)
print (funcion(*datos))

datos = {
    "num1":1,
    "num2":1
}
print (funcion(**datos))


print ("\n\n")


# lambda nos permite crear funciones con una sola instrucción
restar = lambda num1, num2: num1 - num2

print (restar(10, 5))


print ("\n\n")


def jugar(intento=1):
	respuesta = input("¿De qué color es una naranja? ")
	if respuesta != "naranja":
		if intento < 3:
			print ("\nFallaste! Inténtalo de nuevo")
			intento += 1
			jugar(intento) # Llamada recursiva
		else:
			print ("\nPerdiste!")
	else:
		print ("\nGanaste!")
jugar()