'''
Estudiando las tuplas 

miTupla=(elemento1, elemento2, eleenmto3, ..., )
'''

misdatos=("Williams", "Ingeniero Automatizacion","Venezuela", "Allianz Technology", "Barcelona", 2800)
#utilizo la función type para saber que tipo de objeto que estoy declarando
type(misdatos)
print(type(misdatos))
print("Mis datos son: ", misdatos)

longitudTupla=len(misdatos)
print("la Tupla misDatos tiene ", longitudTupla, "elementos")

'''

Método list() --> Convertir Tuplas a Lista.

sintaxis: 

Tengoque declarar una lista --> miLista = list(NombreTupla)

'''

misdatosLista=list(misdatos)

print("La lista misDatosLista es: ", misdatosLista)

misdatosLista.append("Maracay")
misdatosLista.append("Venezuela")
misdatosLista.append("Venezuela")
print("La lista misDatosLista es: ", misdatosLista)


'''
 Metodo tuple() --> Convertir una lista en tupla

 Sintaxis: 

 Tengo que declarar una tupla: miTupla=tuple(NombreLista)

'''

miTuplaDos=tuple(misdatosLista)

print("Mi tuplaDos: ", miTuplaDos)

'''
Palabra reservada in --> me permte conocer si un elemento se encuentra dentro de una tupla. 

Sintaxis: 

print(valorElmento in nombreTupla)

Devolvera valor boolenao de True o False

'''

print("Barcelona" in miTuplaDos) # Devolvera True o False

# Otra forma de hacerlo con coondicionales. 
print("********************************************")
valorElemento="Ernesto"

if valorElemento in miTuplaDos:
    print("El elemento ", valorElemento, " esta en la tupla.")

else:
     print("El elemento ", valorElemento, "  NO esta en la tupla.")
print("********************************************")


'''
Metodo count() --> Si queremos saber cuans veces se repites un elemetn dento de una tupla 

sintaxis: 

nombreTumpla.count(Valorelemento)

'''

miTuplaDos.count("Aragua")
print("El elemento Venezuela se repite: ",miTuplaDos.count("Aragua"))

elementoRepetido="Venezuela"
vecesRepetidoEnTupla=miTuplaDos.count(elementoRepetido)

print("El elemento",elementoRepetido, " esta ", vecesRepetidoEnTupla, " veces" )


'''

Desempaquetado de una Tupla consiste en ir de elemento en elemento y almacenarlo en una variable.

Sintaxis: 

se deberar ir creando variables.

variable1, variable2, variable3, variableN=nombretupla 
 
se tiene que tener en cuenta el orden de las variables declaradas para que el sistema las extraiga de la tupla. 

'''

nombre, profesion, nacionalidad, company, direccion, salario, lugarnacimiento, paisNacimiento, nacionalidad = miTuplaDos

print("Nombre: ", nombre)
print("Profesion: ", profesion)
print("Nacionalidad: ", nacionalidad)
print("Empresa ", company)
print("direccion: ", direccion)
print("salario: ", salario)
print("lugarnacimiento: ", lugarnacimiento)
print("Pais de nacimiento: ", paisNacimiento)
print("Nacionalidad: ", nacionalidad)






