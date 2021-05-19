# r: read
# w: write, sobreescribe el contenido de un archivo, si no existe lo crea
# a: append, agrega contenido al final del archivo
# b: modo binario

mi_archivo = open("./files/archivo.txt", "r+")

for i in mi_archivo.read(4):	# Puedes pasar el número de bytes a leer
	print(i)
# 1 byte = 1 carácter
# Al enviar el parámetro lo que estás haciendo es colocar el cursor en un espacio en específico
# así como lo haces en el block de notas o en el editor de código
# una vez coloques el cursor en un sitio no lo puedes echar para atrás
# sin embargo puedes seguir avanzando en el texto
# si utilizas el método read sin enviar parámetros lo retorna es el resto del documento
# pero podrías seguir enviando parametros para extraer el texto en partes
print(mi_archivo.read())

print(mi_archivo.read()) # Si ya leiste todo el contenido del texto
# e intentas volver a leerlo, retornará un string vacío

multilinea = open("./files/multilinea.txt", "r+")

print(multilinea.readlines()) # Puedes leer el documento línea por línea
# el método readlines te va a retornar un array con todas las líneas del documento
# va a pasar lo mismo que con el método read si intentas leerlo de nuevo, te va a retornar un string vácio

multilinea.close()	# Al terminar de usar los archivos es buena práctica cerrarlos
mi_archivo.close()	# esto mejora el rendimiento