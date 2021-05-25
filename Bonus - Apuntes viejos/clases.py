from modulos.persona import Persona

persona = Persona()

print ("*** PERSONA ***  \n\n")

print ("Nombre:", persona.nombre("Dade"))
print ("País:", persona.pais("Perú"))
print ("Edad:", persona.edad("22"))
print ("Sexo:", persona.sexo[0])
print ("Estatura:", persona.estatura(1.80))
print ("Peso:", persona.peso("50kg"))