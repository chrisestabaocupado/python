# Ejemplo 1: accediendo a través del namespace
import modulos.matematicas

print ("Ejemplo 1:", modulos.matematicas.sumar(5, 5, 3, 12))

# Ejemplo 2: accediendo a través de un alias
import modulos.matematicas as m
print ("Ejemplo 2:", m.restar(20, 5, 2, 3, 5))

# Ejemplo 3: accediendo directamente a los elementos
from modulos.matematicas import * 
print ("Ejemplo 3:", multiplicar(5, 2))

# Ejemplo 4: obtener un elemento en especifico 
from modulos.matematicas import dividir, sumar
print ("Ejemplo 4:", dividir(10, 2))

# Ejemplo 5: asignar a los elementos un alias
from modulos.matematicas import multiplicar as m, dividir as d
print ("Ejemplo 5:", m(3, 3))
print ("Ejemplo 5:", d(5, 5))