class empleado:
    
    
    def __init__(self, nombre, cargo, salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario
    
    #GETTERS AND SETTERS
    
    #nombre
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    #cargo
    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, cargo):
        self.__cargo = cargo
    
    #salario
    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__salario = salario
        
        
    
    #metodo calculo salario
    def Cs(self):
        if self.getSalario() >= 1200000:
            salario1= self.getSalario()/240
            print ("el salario por hora del empleado es: ", round(salario1))
        else:
            print("salario minimo fuera de parametro")
            
    #metodo aumento IPC
    def ipc(self):
        ipc = self.getSalario() * (13.25/100)
        print("el empleado recibe de incremento segun el ipc: ", ipc)
        
    #metodo aumento de salario minimo
    def ipc3(self):
        if self.getSalario() == 1200000: 
            aumentominimo = self.getSalario() *(3/100)
            print ("el usuario recibe un incremento de: ", aumentominimo, "debido a que gana el salario minimo" )
        
    #horas extras
    def extras(self):
        ex = int(input("ingrese las horas extras realizadas en la semana: "))
        if ex <= 10:
            var = ex * (self.getSalario()/240)
            print ("el valor de las horas extras trabajadas es: ", var)
        else:
            print("no puede trabajar mas de 10 horas semanalmente")
            
            
        
        
    
        
ob = empleado("", "", "")

ob.setNombre(input("Digitar nombre del empleado: "))
ob.setCargo(input("Digitar cargo del empleado: "))
ob.setSalario(int(input("Digitar el salario del empleado:")))



print (ob.getNombre(), ob.getCargo(), ob.getSalario())
ob.Cs()
ob.ipc()
ob.ipc3()
ob.extras()