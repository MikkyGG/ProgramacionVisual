name = "Miguel"
edad = 19

print(name)
print(edad)

nombre = "Ada"
apellido = "Lovelace"

fullname = nombre + " " + apellido
print(fullname)

fullname = '{} {}'.format(nombre, apellido)
print(fullname)

print(name.title())
print(name.upper())
print(name.lower())

# Para saber el tipo de variable;;;;;P

print(type(nombre))
print(type(edad))

mensaje = 'Feliz Cumple ' + str(edad) + '!.'
print(mensaje)

falso = False
true = True

print(falso)
print(true)
print(type(falso))
print(type(falso))

# Operaciones basicas

num1 = 20
num2 = 10
suma = num1 + num2
resta = num1 - num2
mul = num1 * num2
div = num1 / num2

print("La suma es ", suma)
print("La resta es ", resta)
print("la multiplicacion es ", mul)
print("La division es ", div)

''' Esto es un comentario
de varias lineas '''

ciudad = '  Campeche  ' # Esto es un comentario tambien
print(ciudad.rstrip())
print(ciudad.lstrip())
print(ciudad.strip())

# Tipos de datos: Listas, Tuplas, Diccionarios

''' Para declarar una lsita en python nombre_lista = []
'''

bicicletas = ['carrera', 'montaña', 'hibrida', 'urbana', 'plegable']

print(bicicletas)
print(type(bicicletas))
print(bicicletas[1].title())

mensaje_2 = "Mi primera bicicleta fue " + bicicletas[3] + "."
print(mensaje_2)

marca_motos = ['Hayley Davison', 'Yamaha', 'Ducati', 'Italika']
print(marca_motos)

# Agregar nuevos elementos a una lista con append
marca_motos.append('Canan')
print(marca_motos)

marca_motos.insert(1, 'otra marca')
print("Con un nuevo indice 1 ", marca_motos)

# Eliminar indice

del marca_motos[0]
print(marca_motos)

# pop() para sacar ultimos elementos de la lista

print(marca_motos.pop())

marca_motos.remove('Ducati')
print(marca_motos)

"""
Ejercicio de python 1
Nombre:
Materia:

"""


# Limpiar lista

# marca_motos = []
# print("Lista vacia ", marca_motos)


# Ciclo For

magos = ['Harry Puto']

for valor in magos:
	print(valor)

print("Esto esta afuera")


for valor in range(1, 11):
	print(valor)


numeros = list(range(1, 11))
print(numeros)


"""

Ejercicio de Python 2. Cuadrado de un numero
Nombre:
Materia:

"""

# Fin del ejercicio

"""
Un millon: haga una lista de los numeros de uno a un millon y luego use
un bucle for para imprimir los numeros. (Si la salida tarda demasiado, 
detenga presionando ctrl-c) o cerrando la ventana de salida).

Use min() y max() para asegurarse de que su lista realmente comience en uno
y termine en un millon.

Ademas, use la funcion sum() para ver que tan rapido Python puede sumar un millon de numeros

"""

# MOVER VARIABLES

cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
	# print(car)
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())


respuesta = 17

if respuesta != 42:
	print("Respuesta incorrecta")



user_ban = ["pepe charly", "jose", "maria"]

user = input("Ingresa tu nombre de usuario: ")

if user not in user_ban:
	print(user.title() + " no esta baneado")

else:

	print(user.title() + " esta baneado")



"""
if - elif - else

La entrada para menores de 4 años es gratuita
La entrada para cualquier persona entre las edades de 4 y18 años es de $ 50
La entrada para cualquier persona mayor de 18 años es de $100
"""

operacion = input("Ingrese la operacion a realizar: ")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo nuero: "))

if operacion == "suma":
	resultado = num1 + num2

elif operacion == "resta":
	resultado = num1 - num2

elif operacion == "division":
	resultado = num1 / num2

else: 
	resultado = num1 * num2

print("El resultado de la operacion: " + str(operacion) + " es " + str(resultado))



"""
diccionarios

"""
participantes = {
	
"nombre": "Miguel",
"edad": 22,
"cursos": ["Python", "Django", "Pycharm"]

}

print(participantes["nombre"])
print(participantes["edad"])
print(participantes["cursos"])

participantes["telefono"] = 9811126236
participantes["ocupacion"] = "Developer"
print("==========")
print(participantes)



jugador = {}

jugador["nickname"] = "MikkyGG"
jugador["score"] = 0

print(jugador)

jugador["score"] = 60
print("Tu score actual es: ", jugador["nickname"] + " es " + str(jugador["score"]))


# DICCIONARIO AVENGERS

avengers = {

	"Cap": {
		"nombre": "Steve",
		"apellido": "Rogers",
		"avenger": "Capitan America",
	},

	"Ironman": {
		"nombre": "Tony",
		"apellido": "Stark",
		"avenger": "Ironman",
	},

	"Hulk": {
		"nombre": "Bruce",
		"apellido": "Banner",
		"avenger": "Hulk",
	}

}


for username, avenger_info in avengers.items():
	print("\n Username " + username)
	fullname = avenger_info["nombre"] + " " + avenger_info["apellido"]
	avenger_name = avenger_info["avenger"]

	print("\t Nombre real " + fullname)
	print("\t Nombre del avenger + avenger")