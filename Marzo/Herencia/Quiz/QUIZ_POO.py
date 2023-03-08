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
        print("Usuario: ")
        
    
    def mostrarusuario(self):
        print(f"Id: {self.id} Nombre: {self.nombre} Apellido: {self.apellido} Edad: {self.edad} Contacto: {self.contactnum} Rol: {self.rol} Usuario: {self.nomusuario} Contraseña: {self.contraseña} Estado: {self.estado}")


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
        print(f"Credencial: {self.credencial} Especializacion: {self.especializacion} Cargo: {self.cargo}")
    

obj_Instructor = Instructor("123456789", "Luis", "Gomez", 32, "3104578167", "Instructor", "Luis_G", "123abc", "Activo", "1a2b3c", "Analista", "Docente")

obj_Instructor.mostrarusuario()

obj_Instructor.mostrarIns()


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
        print(f"id: {self.id} detalle: {self.detalle} requerimiento: {self.requerimiento} fecha {self.fecha}")

obj_Matricula = matricula("13579b", "Inscripción", "Prueba de Estado", "20-01-2023")
obj_Matricula.mostrarMatr()

obj_Matricula.matricular(obj_Estudiante)

obj_Matricula.muestramatricula()


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
    
obj_Asignatura = asignatura("2468A", "Matematicas", "Algebra Booleana", "Luis", "08-03-2023 al 08-05-2023")
obj_Asignatura.mostrarAsign()

obj_Asignatura.asignatura(obj_Instructor)

obj_Asignatura.muestraasignatura()   

        


    
