class usuario:
    def __init__(self, id, nombre, apellido, edad, contactnum, nomusuario, contraseña, estado):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.contactnum=contactnum
        self.nomusuario=nomusuario
        self.contraseña=contraseña
        self.estado=estado
    
    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getEdad(self):
        return self.edad
    def getContactnum(self):
        return self.contactnum
    def getNomusuario(self):
        return self.nomusuario
    def getContraseña(self):
        return self.contraseña
    def getEstado(self):
        return self.estado
    
    def mostrarusuario(self):
        print(self.getId(), self.getNombre(), self.getApellido(), self.getEdad(), self.getContactnum(), self.getNomusuario(), self.getContraseña(), self.getEstado())

        
id = input()
nombre = input()
apellido = input()
edad = input()
contactnum = input()
nomusuario = input()
contraseña = input()
estado = input()

ob = usuario(id, nombre, apellido, edad, contactnum, nomusuario, contraseña, estado)
ob.mostrarusuario() 

    