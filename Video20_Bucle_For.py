'''
Trabajando con estructuras de control bucle for. 

Sintaxis: 

for variable in elemento a recorrer:
    cuerpo del bucle. 

donde: 
for --> palabara reservada for para hacer incapie q estamos trabajando con el bucle for. 
variabe --> por convención se suele utilizar con el nombre i, luego j luego z como nombres de variables contador.
elemento a recorrer --> puede ser una lista, tuplas, cadenas de texto, colecciones, etc etc. 

'''

miLista=[1,2,3,4,"hola",6,"Williams",8,9,10]
longitudLista=len(miLista)
print(longitudLista)
print()

for i in miLista:
    print(i) # Imprimira los elementos internos de la lista que son 10 elementos. 
    print("Williams ", i) # se repetirar el mensaje williams 10 veces, porque son 10 elementos que se encuentran en la lista. 
    print(miLista) # puedo imprimir los elementos de la lista. 
    

listaMeses=["Enero", "Febrero", "Marzo","Abril", "Mayo", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octbre", "Noviembre", "Diciembre"]
print(listaMeses[0])
#contador=0
for meses_anno in listaMeses:
    #print(listaMeses[contador])
    print(meses_anno)
    print("Hola esto es un bucle for, se repetiran 12 veces. porque 12 es la longitud de la lista")
    print(listaMeses)
    #contador=contador+1



# Utilizacion de rangos para determinar cuantas veces se repetirá un bucle for..

'''
sintaxis: 

for i in range(valor1,valor2): 
    cuerpo del bucle. 

    en este caso valor1 y valor2 son numeros enteros. Producira una secuencia de numeros entros que empezara desde el valor1 (inlusive)
    hasta el valor2 (no lo incluye) --> como en matematicas [valor1,valor2)

'''

for i in range(0,21):
    print(i) # Se imprimira los valores numericos desde el 0 al 20 es decir se repetira 21 veces el el cuerpo del bucle. 
    print("williams ", i)

    
