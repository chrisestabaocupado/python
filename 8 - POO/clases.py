class Persona:
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

	def saludo(self):
		print(f"Hola! Soy {self.nombre} {self.apellido} \nMucho gusto!")

roberto = Persona("Roberto", "Gómez")

print(roberto.nombre, roberto.apellido)
roberto.saludo()