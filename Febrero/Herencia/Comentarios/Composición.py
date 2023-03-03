class Curso:                              #Se inicializa la clase recibiendo como nombre Curso
    def __init__(self,titulo):            #se crea el constructor con el parametro "titulo"
        self.__titulo=titulo              #se le asigna el parametro al atributo

    def getTitulo(self):                  #se crea un metodo
        return self.__titulo              #retorno del valor almacenado en el atributo

class Aprendiz:                           #creacion de clase de nombre "aprendiz"
    def __init__(self,nombre):            #creacion de constructor recibiendo como parametro "nombre
        self.__nombre=nombre              #se asigna a la variable el parametro
        self.__cursos=[]                  #se crea una lista que se asignara al atributo curso

    def agregarCurso(self,nombreCursito): #creacion de metodo "agregar curso que recibe como parametros "nombreCursito"
        cursito=Curso(nombreCursito)      #se crea una variable que instancia la clase Curso con Aprendiz y reciba los valores de la clase externa
        self.__cursos.append(cursito)     #se hace uso de un metodo .append para agregar a la lista los datos

    def getCursos(self):                  #
        return self.__cursos
    
ap=Aprendiz('Sofia')
ap.agregarCurso('Python Basico')
ap.agregarCurso('Python Intermedio')

for c in ap.getCursos():
    print(c.getTitulo())
