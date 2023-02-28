class Persona:                              #Creacion de la clase "Persona" seguido de dos puntos para dar paso a la serie de instrucciones que se encuentren subsecuentes a ella donde se encontraran atributos y metodos.
    def __init__(self,nombre):              #definicion de la funcion "__init__" la cual recibe como parametros entre parentesis la palabra "self" la cual permite especificar la ubicacion de las propiedades contenidas en la clase definiendo que son propias de esta, ademas recibir como argumento "nombre".
        self.__nombre=nombre                #uso del argumento "self" para incorporar las propiedades de una clase seguido de un punto y dos guines bajos los cuales permiten administrar el acceso de privacidad para que este sea privado, encontramos entonces el atributo "__nombre" al cual se le asignara el argumento "nombre".
        print('Activando constructor')

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def metodo(self):
        print('Soy un método')


ob=Persona('Ana')
print(ob.getNombre())
ob.setNombre('Maria')
print(ob.getNombre())
#ob.metodo()
#print(type(ob))
