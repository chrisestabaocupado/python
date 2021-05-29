import sqlite3, datetime

print ("*** Programa para insertar registros en la tabla TEST ***")

cadena_texto = input("Introduzca una cadena de texto: ")
entero = input("Introduzca un número entero: ")
decimal = input("Introduzca un número decimal: ")

try: 
    entero = int(entero)
except ValueError:
    print (entero, "No es un numero entero")
    exit()

try:
    decimal = float(decimal) or int(decimal)
except ValueError:
    print (decimal, "No es un numero decimal")
    exit()

# Establecer la conexión
conexion = sqlite3.connect("sqlite3/test.sqlite3")

# Seleccionar el cursor para inciar la consulta
consulta = conexion.cursor()

# Valor de los argumentos
argumentos = (cadena_texto, entero, decimal, datetime.date.today())

sql = """
INSERT INTO test(cadena_texto, entero, decimal, fecha)
VALUES (?, ?, ?, ?)
"""
# Realizar la consulta
if (consulta.execute(sql, argumentos)):
    print ("Registro guardado con exito")
else:
    print ("Ha ocurrido un error al guardar el registro")
    
# Teminar la consulta
consulta.close()

# Guardar los cambios en la base de datos
conexion.commit()

# Cerrar la conexión
conexion.close()