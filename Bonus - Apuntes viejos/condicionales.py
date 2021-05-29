#Operadores Lógicos
"""
if (si), elif (sino, si) y else(sino)
not (si la condicion no se cumple...)
and(y), or(o)
xor(o excluyente, es decir, si por lo menos uno de los valores resula verdadero se aplica)
"""


# Operadores de Comparación
"""
Igual a     ==
Diferente de    !=
Mayor que   >
Menor que   <
Mayor o Igual que   >=
Menor o Igual que   <=
"""

# Primer ejemplo de condicionales

variable = 1
if (variable == 1):
    # Si la condición se cumple hace esto
    print ("Se cumple")
elif (variable != 0):
    # Si no, si se cumple esto hace esto
    print ("Se cumple")
else:
    # Si no se cumple ninguna hace esto otro
    print ("No se cumple")
    
# Ejmplos usando operadores logicos
if not (variable > 10):
    print ("Esto funciona")
    
variable2 = 4

if (variable == 1 and variable < variable2): # Si la variable es igual a 1 y menor que 4 hace lo de abajo
    print (variable, "Es menor que", variable2, "e igual a 1")

if (variable > variable2 or variable == 1):
    print ("Una de las dos condiciones se cumple")
    
    
# membership


lista = ["uno", "dos", "tres"]
if ("dos" in lista):
    print ("Se encontró")
else:
    print ("No se encontró")
