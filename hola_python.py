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