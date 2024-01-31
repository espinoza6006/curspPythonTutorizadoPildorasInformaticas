'''
Sintaxis: condiciones if - else. 

If condición:
	Codigo1
	Codigo2
else:
          codigo3
	Codigo4
Líneas código
Líneas código. 

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

notaAlumno=float(input("Introduce tu nota: "))

def verificacionNotas(_notaAlumno):
    if _notaAlumno>=5:
        print("Has Aprobado. Felicidades.")
    else:
        print("Has Suspendido!!. Animo tu puedes con Python!!!")


verificacionNotas(notaAlumno)


def verificacionNotaDos(_notaAlumno):
    valoracion=""
    if _notaAlumno<NOTA_APROBADA:
        valoracion="Suspenso."
    else: 
        valoracion="Aprobado!!!"
    return valoracion

valoracion=verificacionNotaDos(notaAlumno)

print(valoracion)


def valoracionNotasTres(_notaAlumno):
    valoracion=""
    if _notaAlumno<0:
        valoracion="nota Incorrecta."
    elif _notaAlumno<5:
        valoracion="Suspenso"
    elif _notaAlumno>10:
        valoracion="nota Incorrecta."
    else:
        valoracion="Aprobada"
    return valoracion

valoracionTres=valoracionNotasTres(notaAlumno)
print(valoracionTres)
    
    
    



    