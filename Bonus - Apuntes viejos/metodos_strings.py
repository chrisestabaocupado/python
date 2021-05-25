# -*- coding: utf-8 -*-

# Metodos de Formato
print ('----')

texto1 = "skere"
# Primera letra en mayúsculas
print (texto1.capitalize())
# Método: capitalize()

print ('----')

texto2 = "HOLA MUNDO"
# Todas las letras en minúsculas
print (texto2.lower())
# Método: lower()

print ('----')

texto3 = 'mundo hola'
# Todas las letras en mayúsculas
print (texto3.upper())
# Método: upper()

print ('----')

texto4 = 'MlA DoHoUn'
# Mayúsculas a minúsculas y viceversa
print (texto4.swapcase())
# Método: swapcase()

print ('----')

texto5 = "hola mundo"
# Formato título
print (texto5.title())
# Método tittle()

print ('----')

texto6 = "bienvenido a mi aplicación".capitalize()
# Una copia de la cadena centrada
print (texto6.center(50, "="))  # Salida: ============Bienvenido a mi aplicación============
print (texto6.center(50, " "))
# Método: center(longitud, "caracter de relleno")

print ('----')

texto7 = "a aplicación mi bienvenido".capitalize()
# Una copia de la cadena alineada a la izquierda
print (texto7.ljust(50, "=")) # Salida: A aplicación mi bienvenido========================
# Método: ljust(longitud[, “caracter de relleno”])

print ('----')

texto8 = "a aplicación mi bienvenido".capitalize()
# Una copia de la cadena alineada a la derecha
print (texto8.rjust(50, "=")) # Salida: ========================A aplicación mi bienvenido
# Método: rjust(longitud[, “caracter de relleno”])

print ('----')

numero_factura = 1575
"""Una copia de la cadena rellena con ceros a la izquierda
hasta alcanzar la longitud indicada"""
print (str(numero_factura).zfill(12))
# Método: zfill(longitud)

print ('----')



# Métodos de busqueda




texto9 = "hola mundo".capitalize()
# Un entero representando la cantidad de apariciones de subcadena dentro de cadena
print (texto9.count("a"))  # Salida (1)
# Método: count(“subcadena”, posicion_inicio, posicion_fin)

print ('----')

texto10 = "hoal mundo".capitalize()
"""Un entero representando la posición donde inicia 
la subcadena dentro de cadena. Si no la encuentra, retorna -1"""
print (texto10.find("mundo"))  #Salida (5)
print (texto10.find("mi", 0, 10))  # Salida (-1)
# Método: find(“subcadena”[, posicion_inicio, posicion_fin])

print ('----')

# Saber si una cadena comienza con una subcadena determinada
texto11 = "hola mundo".capitalize()
# Retorna: True o False
print (texto11.startswith("Hola"))
print (texto11.startswith("mundo"))
print (texto11.startswith("skere", 16))
# Método: startswith(“subcadena”, posicion_inicio, posicion_fin)

print ('----')

#Saber si una cadena finaliza con una subcadena determinada
cadena = "bienvenido a mi aplicación".capitalize()
# True o False
print (cadena.endswith("aplicación"))
print (cadena.endswith("Bienvenido"))
print (cadena.endswith("Bienvenido", 0, 10))

print ('----')

# Saber si una cadena es alfanumérica
cadena = "pepegrillo 75"
# Retorna: True o False
print (cadena.isalnum())
cadena = "pepegrillo"
print (cadena.isalnum())
cadena = "pepegrillo75"
print (cadena.isalnum())
# Método: isalnum()

print ('----')

# Saber si una cadena es alfabética
cadena = "pepegrillo 75"
# Retorna: True o False
print (cadena.isalpha())
cadena = "pepegrillo"
print (cadena.isalpha())
cadena = "pepegrillo75"
print (cadena.isalpha())
# Método: isalpha()

print ('----')

# Saber si una cadena es numérica
cadena = "pepegrillo 75"
# Retorna: True o False
print (cadena.isdigit())
cadena = "7584"
print (cadena.isdigit())
cadena = "75 84"
print (cadena.isdigit())
cadena = "75.84"
print (cadena.isdigit())
# Método: isdigit()

print ('----')

# Saber si una cadena contiene solo minúsculas
cadena = "pepe grillo"
# Retorna: True o False
print (cadena.islower())
cadena = "Pepe Grillo"
print (cadena.islower())
cadena = "Pepegrillo"
print (cadena.islower())
cadena = "pepegrillo75"
print (cadena.islower())
# islower()

print ('----')

# Saber si una cadena contiene solo mayúsculas
cadena = "PEPE GRILLO"
# Retorna: True o False
print (cadena.isupper())
cadena = "Pepe Grillo"
print (cadena.isupper())
cadena = "Pepegrillo"
print (cadena.isupper())
cadena = "PEPEGRILLO"
print (cadena.isupper())
# Método: isupper()

print ('----')

# Saber si una cadena contiene solo espacios en blanco
cadena = "pepe grillo"
# Retorna: True o False
print (cadena.isspace())
cadena = " "
print (cadena.isspace())
# Método: isspace()

print ('----')

# Saber si una cadena tiene Formato De Título
cadena = "Pepe Grillo"
# Retorna: True o False
print (cadena.istitle())
cadena = "Pepe grillo"
print (cadena.istitle())
# Método: istitle()

print ('----')




# Métodos de Susitución

# Dar formato a una cadena, sustituyendo texto dinámicamente

cadena = "bienvenido a mi aplicación {0}"
# Retorna la cadena formateada
print (cadena.format("en Python"))
cadena = "Embeces {0} vida {1} es como {2}"
print (cadena.format("la", "no", "queremos"))
cadena = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}"
print (cadena.format(bruto=100, iva=21, neto=121))
print (cadena.format(bruto=100, iva=100 * 21 / 100, neto=100 * 21 / 100 + 100))

print ('----')

# Reemplazar texto en una cadena
buscar = "nombre apellido"
# Retorna la cadena reemplazada
reemplazar_por = "Juan Pérez"
print ("Estimado Sr. nombre apellido:".replace(buscar, reemplazar_por))
# Método: replace(“subcadena a buscar”, “subcadena por la cual reemplazar”)

print ('----')

# Eliminar caracteres a la izquierda y derecha de una cadena

cadena = "  www.eugeniabahit.com  "
# Retorna la cadena sustituida
print (cadena.strip())
print (cadena.strip(' '))
# Método: strip([“caracter”])

print ('----')

# Eliminar caracteres a la izquierda de una cadena
cadena = "www.eugeniabahit.com"
#Retorna la cadena sustituida
print (cadena.lstrip("w." ))
cadena = " www.eugeniabahit.com"
print (cadena.lstrip())
#Método: lstrip([“caracter”])

print ('----')

cadena = "www.eugeniabahit.com     "
# Retorna: la cadena sustituida
print (cadena.rstrip( ))
#Método: rstrip([“caracter”])

print ('----')




# Métodos de unión y división

#Unir una cadena de forma iterativa
formato_numero_factura = ("Nº 0000-0", "-0000 (ID: ", ")")
"""Retorna la cadena unida con el iterable 
(la cadena es separada por cada uno de los elementos del iterable)"""
numero = "275"
numero_factura = numero.join(formato_numero_factura)
print (numero_factura)
# Método: join(iterable)

print ('----')

# Partir una cadena en tres partes, utilizando un separador
tupla = "http://www.eugeniabahit.com".partition("www.")
"""Retorna una tupla de tres elementos donde el primero es el contenido de la cadena
previo al separador, el segundo, el separador mismo y el tercero, el contenido de la
cadena posterior al separador"""
print (tupla)
protocolo, separador, dominio = tupla
print ("Protocolo: {0}\nDominio: {1}".format(protocolo, dominio))
# Método: partition(“separador”)

print ('----')

#Partir una cadena en varias partes, utilizando un separador
keywords = "python, guia, curso, tutorial".split(", ")
#Retorna una lista con todos elementos encontrados al dividir la cadena por un separador
print (keywords)
#Método: split(“separador”)

print ('----')

# Partir una cadena en en líneas
texto = """Linea 1
Linea 2
Linea 3
Linea 4
"""
# Retorna una lista donde cada elemento es una fracción de la cadena divida en líneas
print (texto.splitlines())
texto = "Linea 1\nLinea 2\nLinea 3"
print (texto.splitlines())
# Método: splitlines()