# Escribir y leer ficheros

"""
MODOS:


w: escritura, crea ficheros si no existe
si existe reemplaza el contenido anterior por el nuevo contenido

a: escritura, crea el fichero si no existe
si existe agrega el contenido al final del contenido existente

r: lectura de ficheros
"""


# Crear el manejador para crear un archivo HTML
manejador = open("index.html", "w")

html = "<!DOCTYPE HTML> \n"
html += "<html> \n"
html += "<head> \n"
html += "<title>Hola mundo</title> \n"
html += "</head> \n"
html += "<body> \n"
html += "<h1>Hola mundo</h1> \n"
html += "</body> \n"
html += "</html> \n"

# Escribimo en el fichero
manejador.write(html)

manejador.close()

print ()
print ("*** DOCUMENTO HTML CREADO CON EXITO***")
print ()

print ("*** Lecutra de fichero ***")

manejador = open("./usernames/index.html", "r")
contenido = manejador.read()

if ("<!DOCTYPE HTML>" in contenido):
    print ("Sí es un documento HTML")
else:
    print ("No es un documento HTML")

manejador.close()

print ()

print ("*** Leer el fichero por bucle for ***")

manejador = open("index.html", "r")
for linea in manejador:
    print (linea, end="")
manejador.close()