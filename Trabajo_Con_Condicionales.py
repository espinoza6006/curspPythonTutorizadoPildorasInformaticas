'''
Condicionales if. 

sintaxis: 

if  condicion:
    lineacodigo condicional. 
    linea codigo condicional. 

Ejemplo: Crear un programa que evalue las calificones de una asignatura de un alumno, y en fucnión de esa nota (1-10) el programa nos diga si ha aprobado o si esta en suspenso. 


Función input() --> Es parecida a la clase scanner en java. 
Instrucción que permitirá introducir valores por techado. 

Sintaxis: 

nombreVaribale=input()

Lo único que ay que tener en cuenta es que cuando utilizamos la función input() cualquier valor que introduzcamos por teclado es considerado como texto. Tenemos que transformar ese valor a valores numéricos. Para ellos tenemos que hacer un casting utilizando la función int()  /// float() // o cualquier otra función que consideremos

nombreVariable=float(input())
nombreVariable=int(input())

La función input() permite parámetros. 

nombreVariable=input("mensaje Usuario") --> Con lo que hago es que se escriba una descripción de lo que deberá hacer el usuario. 

'''

NOTA_APROBADA=5
NOTA_MAXIMA=10
NOTA_MINIMA=0

print("Programa para diagnosticar si has aprobado o suspendido una asignatura.")
print()

notaAlumno= float(input("Introduzca su nota: ")) #la función input trabajar como la clase scanner en java.. pero la diferencia es que input lo toma como string. tenemos que hacer un casting o una conversion de tipo de datos. 

def asignaturaAprobada(notaAlumno):
    if notaAlumno>=5:
        print("Felicidades has Aprobado")
    if notaAlumno<5:
        print("Has Suspendido!!!. No te preocupes sigue estudiando :)")
    
asignaturaAprobada(notaAlumno)

# Otra forma. 

def evaluacionAlumno(notaAlumno): 
    evaluacion="Has Aprobado!!"
    if notaAlumno<5:
        evaluacion="Has Suspendido!!!"
    return evaluacion

evaluacion=evaluacionAlumno(notaAlumno)

print(evaluacion)

# Cuando hacemos debbuging no se va a entrar en la función hasta que se hace el llamado de la función en el codigo. 
        




