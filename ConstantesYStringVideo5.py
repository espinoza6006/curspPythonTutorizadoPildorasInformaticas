# Constantes y Strings

NUMERO1=8 # Declaracion de la consrtante

NUMERO1=15 # Declaración de la misma constante, la teoria nos dice que una constante su valor no puede cmbiar a lo largo del rpgrama. pero vemos en este caso que en python si se puede hacer. 
#entonces para evitar este tipo de situaciones, las contantes por lo general se declara e inicializar en en otro modulo, es decir un archivo diferente al código principal. 

print(NUMERO1)


# String --> Concatenación de String
variableStringMultiple= """ jhdfjkhsjkfhskjfhjsdkhdkjfhkj
klsdjflksjdflkfjlksfjlsdflkjlfkjsflkjsflsjlksjflkfjslk
lkjsflkjsflksjlksjlksjlsfjlskjlskjlskfjlkfjflskjl
"""
nombre="Williams"
edadUsuario= 28
# La función print() sirve para imprimir en consola. 
#print("Hola mi nombre es: " + nombre +" y tengo la edad de: " + edadUsuario) 
'''
La función print() --> no permite la concatenación de String con valores numéricos. porque nos arroja un error de tipo: 

TypeError: can only concatenate str (not "int") to str

Para solventarlo podemos utilizar un casting y convertir el valor de edadUsuario a string. Para ello utilizamos la funcion str()

Todas las funciones en programación tienen parentesis() algunos pueden llevar argumentos y otros no. 


'''
print("Hola mi nombre es: " + nombre +" y tengo la edad de: " + str(edadUsuario)+ " años")

'''
Pero en algunas versiones superiores de python podemos utilizar la coma (,) en vez del operador (+) y vemos que si podemos hacer la concatenación entre string y valores hnumericos. 
'''

print("Hola mi nombre es: " + nombre +" y tengo la edad de: " ,edadUsuario," annos")

print("El valor de la variable sting multiple es: "+variableStringMultiple)
