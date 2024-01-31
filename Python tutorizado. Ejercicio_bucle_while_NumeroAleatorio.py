'''
Ejercicio bucles y condicionales. Número aleatorio
Se trata de elaborar un programa que genere un número aleatorio entre 1 y 100. Para ello debemos importar el módulo random y utilizar 
la instrucción random.randint(1,100). Esta instrucción genera un número entero entre 1 y 100.

A continuación, se le pide al usuario que introduzca un número por consola entre 1 y 100. Si el número introducido por el usuario es menor, 
se imprime en consola un mensaje indicando que el número aleatorio es mayor que el introducido por él. 

Si el número introducido por el usuario es mayor que el aleatorio, se imprime un mensaje indicando que el número aleatorio es menor que el introducido por él. 
Después de indicar si es mayor o menor, se vuelve a pedir al usuario que introduzca un número entre 1 y 100.

Se trata de averiguar cuál es el número aleatorio generado por el programa a base de ir aproximándonos intento tras intento, 
y hacerlo en el menor número de intentos posibles así que también debemos controlar cuántos intentos consume el usuario para
adivinar el número aleatorio generado por el programa.

Cuando el usuario averigüe finalmente el número aleatorio, el programa imprimirá en consola “Correcto. Has utilizado…” y el nº de intentos consumidos

'''
import random

print("***Juego Adivinar un Numero generado por el sistema ***")
print(" Intstrucciones: \n 1. Deberas ingresar un Numero Comprendido entre 1-100.\n 2. Tendras 5 Intentos para adivinar numero.\n 3. Comenzamos. ")
numeroAleatorio=random.randint(1,100) # generación del número aleatorio entre 1,100
print(numeroAleatorio)
numeroUsuario=int(input(" Introduce tu numero: "))
intentosUario=1


while numeroUsuario<1 or numeroUsuario>100:
    print("Numero Incorrecto. El numero debe ser entre 1-100: ")
    numeroUsuario=int(input(" Introduce tu numero: "))
    intentosUario=intentosUario+1
    

while(numeroUsuario!=numeroAleatorio):
    if numeroUsuario<1 or numeroUsuario>100:
        print("Numero Incorrecto. El numero debe ser entre 1-100: ")
        numeroUsuario=int(input(" Introduce tu numero: "))

    elif numeroUsuario>numeroAleatorio:
        print("Numero incorrecto. Debes introducir un numero menor")
        numeroUsuario=int(input(" Introduce tu numero: "))
    else:
        print("Numero incorrecto. Debes introducir un numero mayor")
        numeroUsuario=int(input(" Introduce tu numero: "))
    intentosUario=intentosUario+1
print("************************************************************************")
print("Numero Correcto!! lo has conseguido en: ", intentosUario, " intentos")
print("************************************************************************")

print("Fin del programa!!")