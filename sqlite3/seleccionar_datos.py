import sqlite3

conexion = sqlite3.connect("sqlite3/test.sqlite3")

consulta = conexion.cursor()

# Extrayendo todas las filas
sql = "SELECT * FROM test"

if (consulta.execute(sql)):
    filas = consulta.fetchall()
    for fila in filas:
        print ("ID:", fila[0])
        print ("Cadena de Texto:", fila[1])
        print ("Entero:", fila[2])
        print ("Decimal:", fila[3])
        print ("Fecha:", fila[4])
        print ()

# Extrayendo solo una fila
sql = "SELECT * from test WHERE id=%s" % 2
consulta.execute(sql)
fila = consulta.fetchone()

print ("Seleccionando un solo registro con el ID", fila[0], ":", fila[1], fila[2], fila[3], fila[4])
print ()

# Extrayendo entre un rango con BETWEEN
argumentos = (2, 3)
sql = "SELECT * FROM test WHERE id BETWEEN ? AND ?"
consulta.execute(sql, argumentos)
filas = consulta.fetchall()

for fila in filas:
    print (fila[0], ":", fila[1], fila[2], fila[3], fila[4])



consulta.close()

conexion.commit()
conexion.close()