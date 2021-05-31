# Una super clase es aquella de la cual se heredan ciertos elementos
# y pueden servir como base para crear otras clases con características similares
class Animal:
	def __init__(self, nombre, color):
		self.nombre = nombre
		self.color = color
# Por otro lado esta es una subclase, hereda elementos de una superclase
# pero también puede añadirle sus metodos y propiedades por si misma
class Perro(Animal):
	def ladrar(self):
		print("Wooof!")

class Ave(Animal):
	def silbar(self, sonido):
		print(f"{self.nombre} hace:", sonido)

lobo = Perro("Lobo", "Blanco/Negro")
pollito = Ave("Pollito", "Amarillo")

pollito.silbar("Pio Pio Pio")
lobo.ladrar()

# Así mismo si una clase hereda elementos similares los puede sobre escribir
class Persona:
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

	def hablar(self):
		print("Hola!!")

class Weird(Persona):
	def hablar(self):
		print("How When Buta")

luis = Weird("Luis", "Carreño")

luis.hablar()

# Herencia indirecta
class A:
	def metodo(self):
		print(1)

class B(A):
	def metodo_2(self):
		print(2)

class C(B):
	def metodo_3(self):
		print(3)

c = C()

c.metodo()
c.metodo_2()
c.metodo_3()

# Super

class D(A):
	def metodo(self):
		super().metodo()
		print(2)

D().metodo()