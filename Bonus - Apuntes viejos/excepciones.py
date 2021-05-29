entero = input("Introduzca un numero entero: ")

try:
    entero = int(entero) # Si incertas un numero entero
    print ("Brutal, alto número") # Todo chévere
except ValueError: # Si no es un entero
    print ("Estás meando fuera del perol") # Manda esto
