from modulos.persona import Persona

class Deportista(Persona):
    
    def deporte(self, deporte=""):
        return deporte

    def detener(self):
        return "El deportista está detenido"
    
    def correr(self):
        return "El deportista está corriendo"
    
    def saltar(self):
        return "El deportista está saltando"
    
    def nadar(self):
        return "El deportista está nadando"

    # Método privado
    def __metodo(self):
        return "Este es un método privado"