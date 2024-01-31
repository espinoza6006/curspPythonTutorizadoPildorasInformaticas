'''
Crear un programa en el cual se pedida al usuario introduzca una nota por teclado y dependiendo de la nota que se introduzca se motrará lo siguiente: 

nota<5 --> insuficiente. 
nota<6 --> suficiente. 
nota<7 --> bien
nota<9 --> notable
nota<10 --> sobresaliente. 


'''
LIMITE_INFERIOR=0
LIMITE_INSUFICIENTE=5
LIMITE_SUFICIENTE=6
LIMITE_BIEN=7
LIMITE_NOTABLE=9
LIMITE_SOBRESALIENTE=10

print("Verificacion calificaciones")

notaUsuario=float(input("Introduzca su nota: "))

if notaUsuario<LIMITE_INFERIOR or notaUsuario>LIMITE_SOBRESALIENTE:
    print("Nota Incorrecta. Debes introducir una nota entre ","(" ,LIMITE_INFERIOR," - ",LIMITE_SOBRESALIENTE,")")
elif notaUsuario<LIMITE_INSUFICIENTE:
    print("Su nota es: "+str(notaUsuario)+ ". Nota Insuficiente.")
elif notaUsuario<LIMITE_SUFICIENTE:
    print("Su nota es: "+str(notaUsuario)+ ". Nota Suficiente. ")
elif notaUsuario<LIMITE_BIEN:
    print("Su nota es: ", notaUsuario, ". Nota Bien!!!")
elif notaUsuario<LIMITE_NOTABLE:
    print("Su nota es: ", notaUsuario, ". Nota Notable")
elif notaUsuario<=LIMITE_SOBRESALIENTE:
    print("su nota es: "+ str(notaUsuario)+ ". Nota Sobresaliente!!!")
#else:
 #   print("Nota Incorrecta. Debes introducir una nota entre ","(" ,LIMITE_INFERIOR," - ",LIMITE_SOBRESALIENTE,")")