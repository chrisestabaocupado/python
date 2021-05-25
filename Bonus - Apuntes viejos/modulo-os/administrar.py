import os

def init():
    print ("*** ADMINISTRAR ARCHIVOS Y CARPETAS ***\n")
    opcion = input("Seleccione una opción c=crear, e=eliminar: ")
    if (opcion == "c"):
        ruta = input("Indique la ruta, si no indica la ruta, la ruta será la actual: ")
        if (ruta == ""):
            ruta = os.getcwd() + "\\"
            # Comprobar si la ruta existe
            if (os.path.isdir(ruta)):
                tipo = input("Indique el tipo a=archivo, c=carpeta: ")
                if (tipo == "a"):
                    archivo = input("Indique el nombre del archivo: ")
                    # Crear el archivo
                    manejador = open(ruta+archivo, "w")
                    manejador.close()
                    print ("Archivo", archivo, "creado con éxito")
                elif (tipo == "c"):
                    carpeta = input("Indique el nombre de la carpeta: ")
                    # Crear carpeta
                    os.mkdir(ruta+carpeta)
                    print ("Carpeta", carpeta, "creada con éxito")
                else: # Reinicar el programa
                    init()
    elif (opcion == "e"):
        ruta = input ("Indique la ruta, si no indica la ruta, la ruta será la actual: ")
        if (ruta == ""):
            ruta = os.getcwd() + "\\"
        eliminar = input("Indique el nombre de la carpeta o archivo a eliminar: ")
        # Si es un archivo
        if (os.path.isfile(ruta+eliminar)):
            os.remove(ruta+eliminar)
            print ("Archivo", eliminar, "eliminado con éxito.")
        # Si es una carpeta
        elif (os.path.isdir(ruta+eliminar)):
            os.rmdir(ruta+eliminar)
            print ("Carpeta", eliminar, "eliminada con éxito.")
        else: # Reiniciar el programa
            init()
    else: # Reiniciar el programa
        init()

# Llamando a la función
init()