mensajeUsuario="Williams" #Creación (declaración) e iniciar (inicializar) de variable
edadUsuario=28
nombreUsuario="Ernesto"
numeroUno=8
numeroDos=7


print("********************************************************")
print("Hola Mundo")
print("********************************************************")
print(mensajeUsuario + " vas a convertirte en un programador Python")
print("********************************************************")

mensajeUsuario="Adios Williams" #En este punto le se asignado otro valor a la variable mensajeUsuario, con el fin de verificar como las variables pueden cambiar a lo largo del programa. 

print(mensajeUsuario)

print("Hola" + nombreUsuario + "tu edad es: " + str(edadUsuario)) # En este caso tuve que usar un casting y pasar el valor de edadUsuario a String ya que la función print solo puede aceptar tipo String. 


# para saber el tipo de dato de una variable debemos utilizar la funcion type(nombreVariable)
tipoDato=type(mensajeUsuario)
print(tipoDato)

# Utilizando operadores logicos. 
resultadoSuma=numeroUno+numeroDos
print(numeroUno+numeroDos)
print(resultadoSuma)
resultadoResta=numeroUno-numeroDos
print("la resta es: "+ str(resultadoResta))
