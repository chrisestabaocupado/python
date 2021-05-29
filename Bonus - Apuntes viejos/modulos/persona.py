class Persona():
    # Método constructor
    def __init__(self):
        # Propiedades privadas
        self.__nombre = "Introduzca un nombre"
        self.__pais = "Introduzca un país"
        # Propiedad publica
        self.sexo = ["Hombre", "Mujer"]
    
    def nombre(self, nombre=""):
        if (nombre !=""):
            return nombre
        else: 
            return self.__nombre
        
    def pais(self, pais=""):
        if (pais !=""):
            return pais
        else:
            return self.__pais
    
    def edad(self, edad=0):
        return edad
    
    def estatura(self, estatura=0):
        return estatura
    
    def peso(self, peso=0):
        return peso