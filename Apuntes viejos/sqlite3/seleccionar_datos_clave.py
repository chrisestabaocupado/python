import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conexion = sqlite3.connect("sqlite3/test.sqlite3")
conexion.row_factory = dict_factory

consulta = conexion.cursor()

sql = "SELECT * FROM test"
consulta.execute(sql)
filas = consulta.fetchall()

for fila in filas:
    print (fila["cadena_texto"])

    
    
    
consulta.close()

conexion.commit()
conexion.close()