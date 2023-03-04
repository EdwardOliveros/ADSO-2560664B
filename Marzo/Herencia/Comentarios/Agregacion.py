class Aprendiz:                             #creacion de la clase con nombre "Aprendiz"
    def __init__(self,nombre):              #definicion de constructor con la palabra reservada "self" que hace referencia a que el contenido que tiene esta clase es propia de ella junto con el atributo nativo "nombre"
        self.__nombre=nombre                #uso de la funcion "self" para resaltar que el acceso del atributo sera reservado.
        self.__cursos=[]                    #asignacion de lista a elemento "curso" el cual se encontrara privado.

    def agregarCurso(self,titulo):          #creacion de metodo "agregarCurso" con la propiedad "self" y "titulo"
        self.__cursos.append(titulo)        #instacia "curso" haciendo uso del metodo "append" para concatenar la lista con el parametro "titulo"

    def getCursos(self):                    #definicion de "getCursos" para funcionar como un metodo de la presente clase
        return self.__cursos                #retorno de valores alojados en "cursos"

class Curso:                                #Creacion de clase "Curso"
    def __init__(self,titulo):              #creacion de constructor que contendra el atributo "titulo" perteneciente a la clase "Curso"
        self.__titulo=titulo                #Establece que el atributo tendra un acceso privado

    def getTitulo(self):                    #la clase "getTitulo" es definida y consigo "self" que indica que el contenido sera propio del metodo
        return self.__titulo                #retorno y obtencion de valores dados para titulo
    
a=Aprendiz('Martha')                        #un nuevo objeto es creado y pertenece a la clase "Aprendiz" recibiendo una cadena de caracteres
c1=Curso('Python Intermedio')               #Variable de nombre "c1" toma el valor de "Python Intermedio" como titulo de clase "Curso"
c2=Curso('Python Basico')                   #Variable de nombre "c2" toma el valor de "Python Basico" como titulo de clase "Curso"
c3=Curso('Introduccion a Java')             #Variable de nombre "c3" toma el valor de "Introduccion a Java" como titulo de clase "Curso

a.agregarCurso(c1)                          #se implementa el metodo "agregarCurso" para almacenar lo dado en la variable "c1" en el objeto "a"
a.agregarCurso(c2)                          #se implementa el metodo "agregarCurso" para almacenar lo dado en la variable "c2" en el objeto "a"
a.agregarCurso(c3)                          #se implementa el metodo "agregarCurso" para almacenar lo dado en la variable "c3" en el objeto "a"

print(a.getCursos())                        #Impresion de la lista tomando como base el objeto "a" junto al metodo "getCursos" perteneciente de la clase "Aprendiz"


for curso in a.getCursos():                 #Uso del ciclo for con el iterador "curso" en el objeto y su metodo para obtener el Curso
    print(curso.getTitulo())                #Se muestra en pantalla la lista.
