#Creación de clase "Conductor"
class Conductor:
  
  #Creación de constructor recibiendo como parametros las instancias
    def __init__(self,nombre,documento):
      
      #Creación de atributos y asignación de instancias
        self.__nombre=nombre
        self.__documento=documento
        
        #Creación de 
    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento
        
