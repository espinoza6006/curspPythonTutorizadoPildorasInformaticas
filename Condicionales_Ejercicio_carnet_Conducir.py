'''
obtención de carnet de conducir. 

edad<=18 and edad>=90
tener la vision correcta. 
puedes intentar obtener el carnet de conducir. 

'''


print(" Obtencion Carnet de conducir. ")

edadusuario=int(input("Introduce tu edad: "))
vision=input("¿tienes la vision correcta? si/no: ")

if edadusuario>=18 and edadusuario<=90 and (vision=="si" or vision=="SI" or vision=="Si"):
    print("Puedes intentar obtener el carnet de conducir. ")
else:
    print("Lo siento. No cumples con la edad necesario. ")

# otra forma utilizando simbolo de menor que concatenado en la misma expresion. trabajaría de la misma forma que el operador "and"... 
if 18<edadusuario<=90 and (vision=="si" or vision=="SI" or vision=="Si"):
    print("Puedes intentar obtener el carnet de conducir. ")
else:
    print("Lo siento. No cumples con la edad necesario. ")

