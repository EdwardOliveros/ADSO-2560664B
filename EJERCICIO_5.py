def acentuación():

    x = input ("ingrese una palabra: ")
    vec = x

    for i in vec[0]:

        #AGUDAS
        if vec[-1] == "á" or vec[-1] == "é" or vec[-1] == "í" or vec[-1] == "ó" or vec[-1] == "ú":
            print("la palabra es aguda")
            print (vec[-1:])
        elif vec[-2] == "á" or vec[-2] == "é" or vec[-2] == "í" or vec[-2] == "ó" or vec[-2] == "ú" == vec[-2]:
            print("la palabra es aguda")
            print (vec[-2:])

        #GRAVES
        elif vec[-3] == "á" or vec[-3] == "é" or vec[-3] == "í" or vec[-3] == "ó" or vec[-3] == "ú":
                print("la palabra es grave")
                print (vec[-3:])
        elif vec[-4] == "á" or vec[-4] == "é" or vec[-4] == "í" or vec[-4] == "ó" or vec[-4] == "ú" == vec[-4]:
                    print("la palabra es grave")
                    print (vec[-4:])
        
        #ESDRUJULAS
        elif vec[-5] == "á" or vec[-5] == "é" or vec[-5] == "í" or vec[-5] == "ó" or vec[-5] == "ú":
                print("la palabra es esdrujulas")
                print (vec[-5:])
        elif vec[-6] == "á" or vec[-6] == "é" or vec[-6] == "í" or vec[-6] == "ó" or vec[-6] == "ú" == vec[-6]:
                    print("la palabra es esdrújulas")
                    print (vec[-6:])

        #ESDRUJULAS
        elif vec[-7] == "á" or vec[-7] == "é" or vec[-7] == "í" or vec[-7] == "ó" or vec[-7] == "ú":
                print("la palabra es esdrujulas")
                print (vec[-7:])
        elif vec[-8] == "á" or vec[-8] == "é" or vec[-8] == "í" or vec[-8] == "ó" or vec[-8] == "ú" == vec[-8]:
                    print("la palabra es esdrújulas")
                    print (vec[-8:])

        #SOBREESDRUJULA
        elif vec[-9] == "á" or vec[-9] == "é" or vec[-9] == "í" or vec[-9] == "ó" or vec[-9] == "ú":
                print("la palabra es sobreesdrujulas")
                print (vec[-9:])
        elif vec[-10] == "á" or vec[-10] == "é" or vec[-10] == "í" or vec[-10] == "ó" or vec[-10] == "ú" == vec[-10]:
                    print("la palabra es sobreesdrújulas")
                    print (vec[-10:])
        
        else:
            print ("tiene otra acentuación")

acentuación()