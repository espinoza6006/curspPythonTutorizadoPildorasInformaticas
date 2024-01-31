'''
Funciones predefinidas en python. 

Sintaxis: 

def nombre_funcion():
    instrucciones Funcion
    instrucciones Funcion
    return (opcional)

def nombre_funcion(parametros):
    instrucciones Funcion
    instrucciones Funcion
    return (opcional)

'''

'''
creacion de una función que no devuelve valor y no recibe parametros. se imprimira por consola una serie de mensajes. 
'''

def imprimirMensajes(): # creación de una función. 
    print("Primera instruccion")
    print("Segunda instruccion")
    print("Sera el mejor programador de Python")

print("Aqui se imprimira la funcion.") # esta linea de código no forma parte de la función. 

imprimirMensajes() # llamada (invocar, ejecutar) de la función 


# Invocando la función varias veces :) para esto sirve las funciones para reutilizar el código y simplificar el codigo. 
imprimirMensajes()
imprimirMensajes()
imprimirMensajes()
imprimirMensajes()
imprimirMensajes()

''' 
print("Imprimiendo la funcion dntro de un bucle for. ")
for i in range(10):
    print(i)
    imprimirMensajes()
'''

'''
Funcion que devuelve unv valor

def nombre_funcion:
    lineas de codigo Funcion 
    return

'''

def funcionReturn():
    print("Esto es una funcion que devuelve un valor")
    return

mensajeRetorno=funcionReturn() # almecenando el valor de la funcion en una variable

def funcionDos():

    return "Asi tambien se hacen los retunr"

mensajeDos=funcionDos()
print(mensajeDos)


'''
funciones con parametrso o argumentos

sintaxis: 
nombreFuncion(parametros o variable local):

    return parametro

'''

print("Forma 1: ")
def imprimeMensajePeronalizado(mensajeUsuario):
    print(mensajeUsuario)
    return mensajeUsuario

mensajeUsuario="Hola Williams, esto es una funcion con parametros o argumentos"

imprimeMensajePeronalizado(mensajeUsuario) # debemos pasarle los `parametros`



print("Forma 2:" )
def imprimeMensajePeronalizado(mensajeUsuario,valor1,valor2):
   
    return mensajeUsuario + str((valor1+valor2)) # aqui los que se esta haciendo es devolver un mensaje + la sumatoria de dos numeros.. en este caso se debe tener en cuenta que no se pueden concatenar string + integer por eso se utiliza la funcion str()


imprimeMensaje =imprimeMensajePeronalizado("la Suma es: ", 2,6)

print(imprimeMensaje)


print("forma 3: ")

def sumarNumeros(mensajeResultado, valorUno,valorDos):
    sumatoria=valorUno+valorDos
    print(mensajeResultado,sumatoria)
    return sumatoria

mensaje_resultado="La suma es: "

totalResultado=sumarNumeros(mensaje_resultado,3,7)

