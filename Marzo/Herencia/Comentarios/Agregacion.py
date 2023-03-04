class Aprendiz:                             #creacion de la clase con nombre "Aprendiz"
    def __init__(self,nombre):              #definicion de constructor con la palabra reservada "self" que hace referencia a que el contenido que tiene esta clase es propia de ella junto con el atributo nativo "nombre"
        self.__nombre=nombre                #uso de la funcion "self" para resaltar que el acceso del atributo sera reservado.
        self.__cursos=[]                    #asignacion de lista a elemento "curso" el cual se encontrara privado.

    def agregarCurso(self,titulo):          #
        self.__cursos.append(titulo)

    def getCursos(self):
        return self.__cursos

class Curso:
    def __init__(self,titulo):
        self.__titulo=titulo

    def getTitulo(self):
        return self.__titulo
    
a=Aprendiz('Martha')
c1=Curso('Python Intermedio')
c2=Curso('Python Basico')
c3=Curso('Introduccion a Java')

a.agregarCurso(c1)
a.agregarCurso(c2)
a.agregarCurso(c3)

print(a.getCursos())


for curso in a.getCursos():
    print(curso.getTitulo())
