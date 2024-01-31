'''
Trabajando con bucle while..

Sintaxis: 


linea de codigo
linea de codigo
linea de codigo

while condicion:
    cuerpo del bucle
    cuerpo del bucle

linea de codigo
linea de codigo
linea de codigo

'''

contador=0

while contador<10:
    print("Hola Williams", (contador+1))
    contador=contador+1 # Incremento de la variable contador

print("Fin del bucle")


'''
Ejemplo 2.

imaginar que tengamos que controlar el acceso a de usuarios a una zona dependiendo de la edad que tenga ese usuario.

Para este primer ejemplo la re4sctricción es no tener negativa y edad >100 tambien error. . 


'''

edadusuario=int(input("Inrtroduzca su edad: "))

while edadusuario<0 or edadusuario>100:
    print("Edad Erronea. La edades comprendidas tienes que estar entre (0-99)")
    edadusuario=int(input("Inrtroduzca su edad: "))
    #break # Esta instrucción lo que hace es forzar a que se salga del bucle de forma forzada, rompe con la condicion del bucle. 

print("******************************************************")
print("Bienvenido a la zona peronal. Acceso Permitido")
print("******************************************************")

print("Edad del usuario "+ str(edadusuario)+ " annos")