'''
Listas: 

Estructura de datos que nos permite almacenar gran cantidad de valores de cualquier tipo (numericos, booleanos, "textos", objetos) :) 

Sintaxis: nombreLista= [elemento1, elemento2, elemento3, ...., elementoN]


Ejemplo: imaginemos que deseamos crear un programa que debera almacenar muchos nombres de trabajadores..
'''

trabajadores=["Williams", "Maria","Antonio", "Miguel"]

print(trabajadores) # Mostramos los elementos de la lista Trabajadores

'''
Funciones o métodos predefinidos de las Listas

len() --> Función len() Nos permite conocer la longitud o cantidad de elementos de una lista

leng(nombreLista)

'''

longitudLista=len(trabajadores) # Me puedo crear una variable y en esa variable puedo almacenar la cantidad de elementos que tiene la lista. 

print("La lista trabajadores tiene "+ str(longitudLista)+ " Elementos")

print(len(trabajadores))

'''
Método append() --> Permite añadir elementos a una lista como argumento se debe colocar el valor del elemento que se desa agregar a la lista. 

Sintaxis: 

nombreLista.append(valorElmento) --> Recordar que si estamos hablando de elemento de tipo texto deben ir entre comillas. 


'''

trabajadores.append("Julio")

print(trabajadores)
print("Número de elemetos: ",len(trabajadores)) # Se imprimiran en este caso 5 elementos ya que se añadio Julio



'''
Acceder a un elemto en concreto de una lista.

Sintaxis: 

nombreLista[incideLista]

Hay una particularidad con respecto a los elementos de las listas es que en python tambien podemos acceder a los elementos de la lista con numeros negativos.

[0   1  2  3  4]  --> con índices negativos se empezaría a leer de derecha a izquierda empezando con -1
[-5 -4 -3 -2 -1]  
 
'''


nombreTrabajador=trabajadores[4]

print(nombreTrabajador)

nombreTrabajador=trabajadores[-2]

print(nombreTrabajador)

'''
Especificando rango de valores de una lista, es decir si quiero que acceder a los valores de la lista desde un indice a otro

Sintaxis: 

nombreLista[indice1:indiceN] --> se accederá desde el elemento con indice 1 hasta el elemento de indice n sin incluirlo

'''


trabajadores[0:3]

print(trabajadores[0:3]) # se accederá al alemento en la posición 0 hasta el elemento en la posición 2

print(trabajadores[1:]) # se accederá al alemento desde la posicion 1 hasta el ultimo elemento. 



'''
Probando diferentes métodos e instrucciónes de las Listas en python. 

'''

listaUno=["Ana", "Antono","Williams","Juan", "Pedro", "Laura", "Ray"]
listaDos=["Lennin", "Espinoza","Barcelona", 2500, True]
listaTres=["Javier", "Espinoza","Santiago Chile", 4500, True]


# Con el operador (+) podemos unir varias listas entre si

concatenarListas=listaUno+listaDos+listaTres

print("La concatenación de las listas es: ", concatenarListas)

# Método append() --> Permite añadir(anexar, agregar) UN elemento al final de la lista. 
#Ejemplo añadir un elemento a cada una de las listas 1,2,3
# Sintaxis: nombrelista.append(valorelemento)

listaUno.append("Justina")
listaDos.append(32)
listaTres.append(35)

print(listaUno)
print(listaDos)
print(listaTres)

'''
Intrucción del --> permite borrar UN elemento de la lista indicando el indice el elemtno. 

sintaxis: 

del nombreLista[indiceDelElemento]

Ejemplo borrar el elemento de indice en el ultimo indice de la lista 2 y 3
'''
print("Listas dos y tres sin borrar elementos")
print("listaDos: ",listaDos)
print("litaTres",listaTres)

cantidadElementosListaDos=len(listaDos)
cantidadElementosListaTres=len(listaTres)

ultimaPosicionListaDos=cantidadElementosListaDos-1
ultimaposicionListaTres=cantidadElementosListaTres-1

print("la listaDos tiene: ",cantidadElementosListaDos," elementos")
print("la listaTres tiene: ",cantidadElementosListaTres," elementos")

del listaDos[ultimaPosicionListaDos]
del listaTres[ultimaposicionListaTres]

print("listaDos: ",listaDos)
print("litaTres",listaTres)

'''
Método clear() --> vacia todos los elementos de una lista. 

Sintaxis: 

nombreLista.clear()

'''
print("Lista Dos:", listaDos)
listaDos.clear()
print("Lista Dos:", listaDos) # Aparecerá una lista vacia ya que he borrados los elemtneos de la lista con la función clear()
listaDos=["Lennin", "Espinoza","Barcelona", 2500, True]
'''
Método extend() --> este método une una lista a otra. 

sintaxis: 

NombreLista1.extend(nombreLista2)

Para ver el resultado debo mostrar por consola la lista en el cual al cual estoy añadiendo la otra en este caso, estoy añadiendo elementos a la lista1

print(nombreLista1)


OJO: NO SE VA A CREAR OTRA LISTA!!! simplemente se añaden los elementos de una lista a otra. 
'''

print("Uniendo listas con el metodo extend(). Se unirá la lisraUno con la ListaTres")
listaUno.extend(listaTres)
print(listaUno)
print("Uniendo listas con el metodo extend(). Se unira la lisrTres con la ListaTres")
listaTres.extend(listaDos)
print(listaTres)



'''
Método count() --> cuenta las veces que aparece un item.

sintaxis: 

nombreLista.count(Valor_A_Estudiar)
'''

print("ListaUno: ", listaUno)
print("listaDos ", listaDos)
print("listaTres ", listaTres)

repeticionEspinozaListaTres=listaTres.count("Espinoza")
print("El valor (Espinoza) se repite", repeticionEspinozaListaTres, " veces en la lista 3")


'''
Método index() --> devulve el índice en que aparece un item 

Sintaxis: 

nombreLista.index(elementoLista)

NOTA: DA Error si no esta el elemento. 

'''
print()
print("Posicion donde esta el elemento Laura en la ListaUno: ")
listaUno.index("Laura")
dondeEstaLaura=listaUno.index("Laura")
print(listaUno.index("Laura"))
print(dondeEstaLaura)

'''
Método insert() --> Permite agregar un elemento a una lista especificando el índice. 

sintaxis: 

nombreLista.insert(valorIndice,Elemento_a_Introducir)

'''

print("introducir en la listaDos en la posición 3 el elemento Dorado.")

listaDos.insert(3,"Dorado")
print("ListaDos ",listaDos)


'''
Metodo pop() --> extrae el elemento de una lista y lo borra. 

sintaxis: 

nombreLista.pop() --> Si el metodo no tienen  argumeto borrara el ultimo elemento de la lista.

Tambien podemos indicarle el indice del elemento a borrar. 
nombreLista.pop(IndiceElemento)

'''

listaDos.pop()

print(listaDos.pop())
print(listaDos)

listaDos.pop(3)
print(listaDos)

'''
metodo sort() --> ordena autoamticamnte los item de una lista por su valor de menor a mayor

sintaxis: 

nombreLista.sort() --> lo ordena de menor a mayor o alfabeticamente. 

podemos utilizar el argumento reverse=true oara idicar que los ordene al reves

en este caso no se puedes mezcal dentro de la lista tipos de datos
'''


print("ListaUno: ",listaUno)
print(listaUno.index(4500))
listaUno.pop(11)
print("ListaUno: ",listaUno)
print(listaUno.index(True))

listaUno.pop(11)

print("ListaUno: ",listaUno)
listaUno.sort()
print("ListaUno: ",listaUno)

