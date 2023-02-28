try:                             #Inicializa la función que permitira intentar y evaluar una operación por medio de unas instrucciones
    #print(1/1))                 #Imprime la division de los valores insertados 
    raise SyntaxError            #la funcion "raise" permite ejecutar y arrojar la excepcion sin necesidad de evaluar que se ejecuten intrucciones    
except SyntaxError:              #con la funcion "except" se especificara el tipo de error se debera validar para arrojar un respuesta a continuacion
    print('Cierra el parentesis')#se invoca la funcion "print" para imprimir por pantalla lo que se indique una vez ocurra la funcion "except"
