'''
Realizar un programa que saque la raiz cuadrada de un número. hay que tomar en cienta que las raices cuadradas de los numeros negativos no existen. 
'''

import math # importaremos la clase math para poder tener accesos a los difernetes metodos como raices cuadras e incluso numero aleatoriols. 

print("Programa para calcular la raiz cuadrada de un Numero. ")

numeroUsuario=float(input("Introduce un numero: "))
intentos=1

'''
if numeroUsuario<0:
    while numeroUsuario<0:
        print("Numero incorrecto. No se existe la raiz de numero negativos en los numeros reales. ")
        numeroUsuario=float(input("Introduce un numero: "))
        intentos=intentos+1
        if intentos==5:
            print("Has intentado ", (intentos+1), " veces")
            break
        if numeroUsuario>0:
            raizCuadrada=math.sqrt(numeroUsuario)
            print("La razis cuadrada del numero: "+str(numeroUsuario)+ " es "+ str(raizCuadrada))
else:
    if numeroUsuario>0:
        raizCuadrada=math.sqrt(numeroUsuario)
        print("La razis cuadrada del numero: "+str(numeroUsuario)+ " es "+ str(raizCuadrada))

'''

while numeroUsuario<0:
        print("Numero incorrecto. No se existe la raiz de numero negativos en los numeros reales. ")
        numeroUsuario=float(input("Introduce un numero: "))
        intentos=intentos+1
        if intentos==5:
            break

if intentos==5:
    print("Has intentado ", (intentos+1), " veces")
else:
    raizCuadrada=math.sqrt(numeroUsuario)
    print("La razis cuadrada del numero: "+str(numeroUsuario)+ " es "+ str(raizCuadrada))


print("Fin del programa")


