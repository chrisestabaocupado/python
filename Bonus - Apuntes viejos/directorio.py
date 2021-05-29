import glob, os.path

# glob permite indexar en la ruta seleccionada para examinar los archivos y documentos que contiene
todos = glob.glob("directorio/*")
print ("Todos los archivos y carpetas que se encuentran en el directorio:")
print ()
print (todos)
print ()


# path es un submódulo de os, que permite (entre otras cosas) saber si un archivo o carpeta existe en la ruta indicada

# Todos los archivos dentro de un directorio
archivos = []
for element in todos:
    if(os.path.isfile(element)):
        archivos.append(element)
print ("Todos los archivos del directorio:", archivos)
print ()

# Todas las carpetas dentro de un directorio
carpetas = []
for element in todos:
    if(os.path.isdir(element)):
        carpetas.append(element)
print ("Todas las carpetas del directorio:", carpetas)
print ()

# Solo los archivos con una cierta extensión
txt = glob.glob("directorio/*.txt")
print ("Archivos .txt del directorio:", txt)
print ()

# Solo archivos con una cantidad de caracteres en su nombre
txt3char = glob.glob("directorio/???.txt")
print ("Archivos .txt con solo tres carácteres dentro de su nombre:", txt3char)