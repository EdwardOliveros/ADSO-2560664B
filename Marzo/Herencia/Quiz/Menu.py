########################CLASE USUARIO########################
class usuario:
    def __init__(self, id, nombre, apellido, edad, contactnum, rol, nomusuario, contraseña, estado):

        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.contactnum=contactnum
        self.rol=rol
        self.nomusuario=nomusuario
        self.contraseña=contraseña
        self.estado=estado
        
        
    
    def mostrarusuario(self):
        print (f"Id: {self.id}")
        print (f'Nombre: {self.nombre}')
        print (f'Apellido: {self.apellido}')
        print (f'Edad: {self.edad}')
        print (f'Contacto: {self.contactnum}')
        print (f'Rol: {self.rol}')
        print (f'Usuario: {self.nomusuario}')
        print (f'Contraseña: {self.contraseña}')
        print (f'Estado: {self.estado}')
        
    def actualizarnombre(self, newnombre):
        self.nombre=newnombre


obj_Instructor = usuario("", "", "", "", "", "", "", "", "")
obj_Estudiante = usuario("", "", "", "", "", "", "", "", "")


########################Clase Instructor########################

class Instructor(usuario):
    def __init__(self, id, nombre, apellido, edad, contactnum, rol, nomusuario, contraseña, estado, credencial, especializacion, cargo):
        super().__init__(id, nombre, apellido, edad, contactnum, rol, nomusuario, contraseña, estado)

        self.credencial = credencial
        self.especializacion = especializacion
        self.cargo = cargo
        print("Instructor: ")

    def mostrarIns(self):
        print(f"Credencial: {self.credencial}")
        print (f'Especializacion: {self.especializacion}')
        print (f'Cargo: {self.cargo}')
    
    
        
    

obj_Instructor = Instructor("123456789", "Luis", "Gomez", 32, "3104578167", "Instructor", "Luis_G", "123abc", "Activo", "1a2b3c", "Analista", "Docente")

obj_Instructor.mostrarusuario()

obj_Instructor.mostrarIns()

print("")
########################Clase Estudiante########################

class Estudiante(usuario):
    def __init__(self, id, nombre, apellido, edad, contactnum, rol, nomusuario, contraseña, estado, curso):
        super().__init__(id, nombre, apellido, edad, contactnum, rol, nomusuario, contraseña, estado)

        self.curso = curso
        print("Estudiante: ")
        
    def mostrarEst(self):
        print(f"Curso: {self.curso}")


obj_Estudiante = Estudiante("110794806", "Edward", "Oliveros", 18, "3173964954", "Estudiante", "Edward_O", "123abc", "Activo", "Ciencias")
obj_Estudiante.mostrarusuario()
obj_Estudiante.mostrarEst()

print("")

########################    Matricula    ########################

class matricula():
    def __init__(self, id, detalle, requerimiento, fecha):
        self.id=id
        self.detalle=detalle
        self.requerimiento= requerimiento
        self.fecha=fecha
        self.estudiante = None
        print("Iniciando Matricula: ")

    def muestramatricula(self):
        print(self.id)
        print(self.detalle)
        print(self.requerimiento)
        print(self.fecha)

        if self.estudiante==None:
            print("Matricular Estudiante")
        else:
            print(self.estudiante)

    def matricular(self, estudiante):
        if isinstance(estudiante, Estudiante):
            self.estudiante=Estudiante
        else:
            print("Agrege un estudiante")

    def mostrarMatr(self):
        print(f"id: {self.id} detalle: {self.detalle} requerimiento: {self.requerimiento} fecha: {self.fecha}")

obj_Matricula = matricula("13579b", "Inscripción", "Prueba de Estado", "20-01-2023")
obj_Matricula.mostrarMatr()

obj_Matricula.matricular(obj_Estudiante)

obj_Matricula.muestramatricula()
obj_Estudiante.mostrarEst()

print("")
 
########################   ASIGNATURAS   ########################

class asignatura():
    def __init__(self, id, nombre, descripcion, instructor, cronograma):
        self.id=id
        self.nombre=nombre 
        self.descripcion=descripcion
        self.instructor=instructor
        self.cronograma=cronograma
        self.instructor = None
        print("Iniciando Asignatura:")

    def muestraasignatura(self):
        print(self.id)
        print(self.nombre)
        print(self.descripcion)
        print(self.instructor)
        print(self.cronograma)

        if self.instructor==None:
            print("Asignar Instructor")
        else:
            print(self.instructor)

    def asignatura(self, instructor):
        if isinstance(instructor, Instructor):
            self.instructor=Instructor
        else:
            print("Agrege un Instructor: ")

    def mostrarAsign(self):
        print(f"id: {self.id} Nombre: {self.nombre} Descripcion: {self.descripcion} Instructor: {self.instructor}  Cronograma: {self.cronograma}")
    
matematicas = asignatura("2468A", "Matematicas", "Algebra Booleana", "Luis", "08-03-2023 al 08-05-2023")
matematicas.mostrarAsign()

matematicas.asignatura(obj_Instructor)

matematicas.muestraasignatura()


################## Cursos ####################
class cursos:
    def __init__(self, id, descripcion, fecha, nivelaño):
        self.id=id
        self.descripcion=descripcion
        self.fecha=fecha
        self.nivelaño=nivelaño
        self.asignatura=[]
        self.matricula=[]
        
    def agregarasignaturas(self, curso):
        self.asignatura.append(curso)
        
    def mostrarcurso(self):
        print(f'id: {self.id}')
        print(f'descripcion {self.descripcion}')
        print(f'fecha: {self.fecha}')
        print(f'nivel de año: {self.nivelaño}')
        print(f'Asignaturas: {self.asignatura}')
    
    def getcurso(self):
        print (f' asignatura: {self.asignatura}')

        
obj_curso = cursos("12345", "descripcion de curso", "08-03-2023", "3 trimestre", )


        

        

while True:
    print("Bienvenido, seleccione el rol:\n 1.Instructor\n 2.Estudiante")
    var=int(input("ingrese: "))
    match var:
        case 1:
            print("Bienvenido al rol de Instructor: ")
            print("1.Consultar Cursos\n2.Ver Datos de usuario\n3.Actualzar datos")
            var=int(input())
            match var:
                case 1:
                    obj_curso.mostrarcurso()
                    obj_curso.agregarasignaturas(obj_Asignatura)
                    print(obj_curso.getcurso())
                case 2:
                    obj_Instructor.mostrarusuario()
                    obj_Instructor.mostrarIns()
                    
                case 3:
                    print("Actualizar: \n 1.Nombre")
                    var=int(input())
                    match var:
                        case 1:
                            obj_Instructor.actualizarnombre(input())
                            obj_Instructor.mostrarusuario()
                            
                    
    
    

    