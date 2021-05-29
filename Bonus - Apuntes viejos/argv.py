import sys

print ("Todos los argumentos pasados en la línea de  comandos", sys.argv)

print ("El nombre del script Python que se está ejecutando es:", sys.argv[0])

print ("\n\n ***Programa para multiplicar dos numeros*** \n\n")
numero1 = sys.argv[1]
numero2 = sys.argv[2]

try:
    numero1 = float(numero1)
    numero2 = float(numero2)
    total = numero1 * numero2
    print ("El total de la multiplicacion de", numero1, "por", numero2, "es igual a:", total)
except ValueError:
    print ("No es un argumento valido")