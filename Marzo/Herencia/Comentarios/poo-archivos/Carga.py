#importación de todos los elementos de la clase "Vehiculo" desde otro archivo contenido en la carpeta nativa
from Vehiculo import *

#creación de la clase "Carga" recibiendo como parametro la herencia de la clase "Vehiculo"
class Carga(Vehiculo):
  
  #inicialización del constructor con sus instancias
    def __init__(self,placa,conductor,capacidad,ejes):
      
      #Instancia de la clase padre con los atributos heredados
        Vehiculo.__init__(self,placa,conductor)
        
        #asignacion de instacias a atributos
        self.__capacidad=capacidad
        self.__ejes=ejes
        
        #creacion de metodos "Getters" para retornar valores contenidos en los atributos
    def getCapacidad(self):
        return self.__capacidad    
    def getEjes(self):
        return self.__ejes
