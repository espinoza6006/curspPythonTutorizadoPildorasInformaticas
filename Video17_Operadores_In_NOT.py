

trabajadores=["Williams", "Paula", "Manuel", "Pedro", "Ana", "Sandra"]

busquedaUsuario=input("Escriba el nombre del usuario que quiere localizar en la lista: ")


#Utilizo el operador in para saber si un elemento esta o no en la lista. esto devolvera true o false. 
if busquedaUsuario in trabajadores:
    print("El usuario esta en la Lista")
    posicionTrabajador=trabajadores.index(busquedaUsuario) # utilizo el metodo index para saber en que posición esta el trabajador en la lista. 
    print("El trabajador ", busquedaUsuario, " esta en la posicion: ",posicionTrabajador," de la lista")
else:
    print("El trabajador", busquedaUsuario, " No esta en la base de datos. ")


# Ejemplo del operador in para hacer busquedas dentro de un String. 


lenguaje_Trim1="Java, Python, PHP, C#, HTML, JavaScript"

# si queremos hacer una busque de un lenguaje en concreta para ver si se encuentra o no dentro del la variable lenguaje_Trim1
# lo podemos hacer con un condicional y con el operador in 

lenguajeInteres=input("Escribe el nombre del lenguaje que estas interesado: ")

def busquedaLenguaje(_lenguajeTrimente,_lenguajeInteres):
    if _lenguajeInteres in _lenguajeTrimente:
        print("El lenguaje "+_lenguajeInteres+ " se cursa en en el Trimestre 1")
    else:
        print("El lenguaje", _lenguajeInteres," no esta en este trimestre")

busquedaLenguaje(lenguaje_Trim1,lenguajeInteres)


# Operador NOT. se traduce como no.. es como invertir la logica o el sentido de la condicion que desees plantear. 
# sintaxis: if condicion not in valor: 


def busquedaLenguaje(_lenguajeTrimente,_lenguajeInteres):
    if _lenguajeInteres in _lenguajeTrimente:
        print("El lenguaje "+_lenguajeInteres+ " se cursa en en el Trimestre 1")
    elif _lenguajeInteres=="SQL" not in _lenguajeTrimente: # Operador not in 
        print("Tienes Razon SQL debe estar en esta lista. ")
    else:
        print("El lenguaje", _lenguajeInteres," no esta en este trimestre")

busquedaLenguaje(lenguaje_Trim1,lenguajeInteres)

