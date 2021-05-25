# While (mientras)
inicio = 0
final = 10

while (inicio != final): # Mientras inicio sea diferente a final
    print (inicio) # Se imprime el valor de inicio
    inicio += 1 # Y se incrementa en uno
# Si no se incrementa el valor de incio, esto se convertiria en un bucle infinito
else: # Una vez se cumpla la condición, ocurre esto
    print (inicio)
    print ("Listo")

    
print ("----")


# Romper la iteración en un punto determinado
start = 0
end = 10
while (start < end): # Mientras start sea menor que end
    print (start)
    if (start == 5): # Cuando start sea igual a cinco
        break        # Se rompe la iteración
    start += 1 # Y se incrementa el valor para que sea un bucle finito


print ("----")
    
    
# Recorrer arrays
index = 0
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while index < len(lista): # La función len() cuenta los elementos de cualquier tipo de dato
    print (index)
    index += 1
    
print ("----")


# For (por)

    
# range(incio, final)
for x in range(0, 10): # Necesito una x para cada rango desde 0 hasta el 10
    print (x)
else: # Una vez alcanzado el rango más alto haces esto
    print (x)
    print ("Listo")

    
print ("----")
    
    
# Imprimir cada uno de los elementos de una tupla
nombres = ("Manuel", "Fernando", "Yolanda", "Mario")

for nombre in range(len(nombres)):
    print (nombres[nombre])
else:
    print ("Esos son todos")

print ("----")    
    
# Una forma más facil de hacerlo
colores = ["Amarillo", "Azúl", "Rojo"]
for color in colores:
    print (color)
    
print ("----")


# Imprimir cada clave y valor de un diccionario

diccionario = {
    1:"Manuel",
    2:"Fernando",
    3:"Yolanda",
    4:"Mario"
}
for clave, valor in diccionario.items():
    print (clave, valor)
else:
    print ("Terminamos")
    

print ("----")
    

# Imprimir cada letra de un string
frase = "Skere"
for letras in frase:
    print (letras)
    