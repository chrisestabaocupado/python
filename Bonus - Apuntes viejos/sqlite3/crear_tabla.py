import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("sqlite3/test.sqlite3")

# Seleccionar el cursor para realizar la consulta
consulta = conexion.cursor()

# Crear tabla
sql = """
CREATE TABLE IF NOT EXISTS test(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
cadena_texto VARCHAR(50) NOT NULL,
entero INTEGER NOT NULL,
decimal FLOAT NO NULL,
fecha DATE NOT NULL)"""

# Ejecutar la consulta
if (consulta.execute(sql)):
    print ("Tabla creada con exito")
else:
    print ("Ha ocurrido un error al crear la tabla")
    
# Terminar consulta
consulta.close()

# Guardar los cambios en al base de datos
conexion.commit()

# Cerrar conexion a la DB
conexion.close()