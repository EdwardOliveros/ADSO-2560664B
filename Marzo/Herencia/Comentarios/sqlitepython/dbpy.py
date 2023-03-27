import sqlite3                                        #importación de libreria sqlite3
#con=sqlite3.connect('C:\\narvaez\\db\\conpython.db') #creacion de conexion por medio de un objeto para instanciar la ubicacion del archivo por medio de ruta relativa
con=sqlite3.connect('sqlitepython/conpython.db')      #creacion de conexion por medio de un objeto para instanciar la ubicacion del archivo por medio de ruta absoluta
print(type(con))                                      #impresión del tipo de dato del objeto
micursor=con.cursor()                                 #asignacion del objeto con un metodo de clase a una variale
print(type(micursor))                                 #impresion del tipo de dato del objeto
sentencia="SELECT * from alumno;"                     #creacion de variable y asignacion de cadena de texto conteniendo una sentencia de comando sql
micursor.execute(sentencia)                           #ejecucion de la sentencia sql 
for fila in micursor.fetchall():
    print(fila[0])
    print(fila[1])
    print(fila[2])
    print(fila[3])
    print('-'*50)
