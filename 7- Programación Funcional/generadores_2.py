def generar_cuidades(*ciudades):
	for i in ciudades:
		yield from i # Devuelve los sub elementos dentro de un elemento
		# Si fuese un string devolvería carácter por carácter
		# pero al ser una tupla va devolviendo cada uno de los elementos
		# dentro de ella

objetoCiudades = generar_cuidades((1,2,3), "Caracas", "Bogotá", "Ciudad de México")

print(next(objetoCiudades))

print(next(objetoCiudades))

print(next(objetoCiudades))