class A1:                                       #Creacion de la clase "A1"
    def __init__(self):                         #Definicion del constructor sin parametros, self indica que las propiedades de la clase pertenecen a si misma
        pass                                    #Funcion pass para omitir la ejecucion del contenido
    def saludo(self):                           #definicion de metodo "saludo" con parametro "self".
        print('Hola desde A1')                  #función print para imprimir los datos entre el parentesis en cadena de texto

class A2:                                       #Creación de clase "A2"
    def __init__(self):                         #Inicialización de constructor sin parametros
        pass                                    #Funcion pass para omitir la ejecucion del contenido
    def saludo(self):                           #Definición de metodo "Saludo"
        print('Hola desde A2')                  #Función "print" imprime datos contenidos en el parentesis


class B(A2,A1):                                 #Creación de la clase "B" tomando como parametros "A1" y "A2" siendo clases padre que permitiran heredar 
    def __init__(self):                         #
        pass
    def saludo(self):
        print('Hola desde B')
    def __str__(self):
        return 'Soy un objeto de la clase B'
obj=B()
print(obj.__str__())
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())
