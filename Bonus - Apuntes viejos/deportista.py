from modulos.deportista import Deportista

deportista = Deportista()

print ("*** Deportista ***  \n\n")

print ("Nombre:", deportista.nombre("Dade"))
print ("País:", deportista.pais("Perú"))
print ("Edad:", deportista.edad("22"))
print ("Sexo:", deportista.sexo[0])
print ("Estatura:", deportista.estatura(1.80))
print ("Peso:", deportista.peso("50kg"))
print ("Deporte:", deportista.deporte("Atletismo"))
print (deportista.correr())
print (deportista.detener())
print (deportista.saltar())
print (deportista.nadar())