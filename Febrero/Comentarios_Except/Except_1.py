try:                              #Inicializa la función denominada "try" que cumple con tiene como facultad intentar y evaluar operaciones por medio de una serie de instrucciones.
    #print(1/1))                  #Linea de codigo Comentada emplea una funcion print para imprimir la division de los valores insertados, se encuentra identada al bloque "try" para ser tomada en medio de la ejecucion del mismo 
    raise SyntaxError             #la funcion "raise" permite ejecutar y arrojar la excepcion sin necesidad de evaluar que se ejecuten intrucciones, para este caso ejecuta un tipo de error que sera evaluado de tipo sintatico.
except SyntaxError:               #con la funcion "except" se especificara el tipo de error y se debera validar para arrojar un respuesta a continuacion, se encuentra fuera del bloque "try" siendo un fragmento clave para excluir el error ejecutado.
    print('Cierra el parentesis') #se invoca la funcion "print" dentro del bloque "except" para imprimir por pantalla lo que se indique una vez ocurra la funcion "except".