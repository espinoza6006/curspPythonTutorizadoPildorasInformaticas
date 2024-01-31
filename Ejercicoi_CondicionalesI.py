'''
Tipo impositivo declaración Renta.

Renta                 Tipo Impositivo. 
Renta < 12000 -->       7%
12000<Renta<18000 ----> 15%
18000<Renta<35000 --> 21%
35000<Renta<70000--> 35%
Renta>70000 -----> 45%



Crea un programa que pregunte por consola la renta. En función de la renta introducida, el programa devolverá el texto: “A la renta (aquí iría la renta introducida) 
le corresponde un (aquí iría el tipo impositivo) de tipo impositivo.

Ejemplo: En caso de introducir por consola 13500, el programa devolverá el texto: “A la renta 13500 le corresponde un 15% de tipo impositivo”

El programa debe permitir la introducción de rentas decimales.
'''

LIMITE_INFERIOR=0
LIMITE_SIETE=12000
LIMITE_15=18000
LIMITE_21=35000
LIMITE_45=70000

print("Calculo Tipo Impositivio Declaración Renta.")

rentaUsuario=float(input("Introduzca la renta en Euros: "))

def calculoRentaTipoImpositivo(_renta):
    if _renta<LIMITE_INFERIOR:
        print("Error en el valor de la renta. Debe ser mayor que "+ str(LIMITE_INFERIOR))
    elif _renta==LIMITE_INFERIOR:
        print("A la renta "+str(_renta)+" le corresponde un 0%")
    elif _renta<LIMITE_SIETE:
        print("A la renta "+str(_renta)+" le corresponde un 7%")
    elif _renta<LIMITE_15:
        print("A la renta "+str(_renta)+" le corresponde un 15%")
    elif _renta<LIMITE_21:
        print("A la renta "+str(_renta)+" le corresponde un 21%")
    elif _renta<LIMITE_45:
        print("A la renta "+str(_renta)+" le corresponde un 35%")
    else:
        print("A la renta "+str(_renta)+" le corresponde un 45%")

calculoRentaTipoImpositivo(rentaUsuario)