'''
Trabajando con Diccionarios. 

Sintaxis: 

nombreDiccionario={clave:valor}

Recordar que cuando estamos trabajando con texto los valores deben ir entre comillas. 

'''

# Ejemplos crear un diccionaio donde se deseen almacenar una serie de capitales del mundo. 

'''

Recorda que como estamos hablando de formaco clave:valor esa clave debe ser úbina y que no se repitiese. por lo tanto en este caso 
es conveniente colocar como clave el nombre del país ya que estos tiene una sola capital. 

'''

capitalesMundo={"Spain":"Madrid", "Venezuela":"Caracas", "Noruega":"Oslo", "Francia":"Paris", "Alemania": "Berlin"}


# Mostar los el contenido del Diccionario --> utilizamos la función print(nombreDiccionario)
print(capitalesMundo)


'''
Para agregar mas elementos al diccionario podemos hacerlo de la siguiente forma: 

nombreDiccionario[clave]=Valor --> simplemente recordar que no se puenden repetir las claves. 

'''

capitalesMundo["Hungria"]="Budapest"
print("agregando Hungria")
print(capitalesMundo)


'''
Acceder a los valores de una clave. 

nombrediccionario[clave]

'''

capitalSpain=capitalesMundo["Spain"]
print("La capital de spain es: ",capitalSpain)

'''
Instrucción del --> Permite eliminar una clave :valor del diccionario

sintaxis: 

del nombreDiccionario[clave]

'''
del capitalesMundo["Hungria"]

print(capitalesMundo)


'''
crear diccionario con varios tipos de datos

'''

datos={"España": "Madrid",23:"M. Jordan","Mosqueteros":3} # Se pueden combinar varios tipos de datos textos, numericos, etc

'''

NOTA: 
como nota impotante python se denomina como lenguaje de programación de tipado Dinamico ya que permite justamente declarar variables u otras estructuras de
almacenamiento de datos (listas, tuplas diccionarios) con variaos tipos de datos. 

mientras los lenguajes de promracacion de tipado estatico esto no se puede hace en este caso se debe especificar el tipo de valor con que se desea trabajar. 


'''

print(datos)


'''
una operación que se suele utilizar frecuentemente en los diccionarios es utilizar las tuplas para asignar claves. ya que la tupla nos permite su acceso con indices pero estas son más estrictas para
que las listas a la hora de manipular sus datos. 

sintaxis: 

1- Declaración de tupla donde se alamacenaras las claves. 
mitupla=(valor1, valor2, valoor3,...)
2- declaración de diccionario: 
midiccionario={mitupla[indice0]:valor, mitupla[indice1]:valor}


'''


claveCapitales=("Espanna", "Reino Unido", "Venezuela", "Portugal") # Declaración de tupla asignar claves
valoresCapitales={claveCapitales[0]:"Madrid", claveCapitales[1]:"Londres", claveCapitales[2]:"Caracas", claveCapitales[3]:"Lisboa"} #Declaración del diccionario assignando lla clave que tiene la tupla y el valor correspondiente.

print(valoresCapitales)


'''
Función keys --> permite conocer todas las claves de un diccionario. 

sintaxis: 

nombreDiccionatio.keys()

'''


clavesDiccionarioValoresCapitales=valoresCapitales.keys()

print(clavesDiccionarioValoresCapitales)



'''

Metodo values() --> permitira conocer cuales son los valores de un diccionario. 

sintxis: 

nombreDiccionario.values()
'''

valoresDiccionario_valoresCapitales= valoresCapitales.values()

print("Los valores del diccionario valorescapitales son: ", valoresDiccionario_valoresCapitales)


'''
len() --> conocer la longitud de un diccionario, es decir cuantos elementos tiene.

len(nombreDiccionario)

'''

longitudDiccionario_valoresCapitales=len(valoresCapitales)

print("Total elementos o longitud del diccionario: ", longitudDiccionario_valoresCapitales)


'''

Diccionarios Anidados, es decir un diccionario dentro de otro diccionario.

'''


datosJordan={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls","Anillos":[1991,1992,1993,1996,1997,1998]} 

print(datosJordan)

print(datosJordan["Anillos"])


datosJordanDos={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls","Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}

print(datosJordanDos)

print(datosJordanDos.keys)