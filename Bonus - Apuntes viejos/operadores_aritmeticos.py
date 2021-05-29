# Operadores Aritmeticos


uno = 1
dos = 2
tres = 3
cien = 100

# Suma (+)
suma = uno + uno
print ("Esto es una suma:", suma)

# Resta (-)
resta = tres - dos
print ("Esto es una resta:", resta)

# Multiplicación (*)
multiplicacion = tres * 2
print ("Esto es una multiplicación:", multiplicacion)

# Potenciación (//)
potencia = 2 ** 10
print ("Potencia:", potencia)

# División (/)
division = multiplicacion / tres # Division con decimales
print ("Esto es una división:", division)

# Divisiones enteras o sin decimales (//)
divisionEntera = 10 // tres
print ("División sin decimales:", divisionEntera)

# Residuo de una división (%)
resto = 10 % tres
print ("Resto o residuo de una división:", resto)


# Priorización con parentesis
# Prioridad: parentesis>potenciación>multiplicación>división>módulo>suma>resta
parentesis = tres + tres * tres # Es igual a 12
parentesis = (tres + tres) * tres # Es igual a 18 
print ("Operaciones con parentesis:", '(3 + 3) * 3', "Es igual a:", parentesis)


# Asignación acumulada
variable = 10
variable += 5
variable += 2
print ("Asignación acumulada", variable)

variable = 10
variable -= 5
variable -= 4
print ("Asignación acumulada", variable)


# Incremento
uno = uno + 1
print("Incremento", uno)
# Decremento
uno = uno - 1
print ("Decremento", uno)