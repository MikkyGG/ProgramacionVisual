# EJERCICIO # 6

"""

Ejercicio de Python 6: FUNCIONES
Nombre: Miguel David Palma Lara
Materia: Programacion Visual

"""

"""
Realiza una funcion que imprima "Hola Mundo"
Realiza una funcion que sume dos numeros pasados por parametros
Realiza una funcion que indique si un numero pasado por parametro es par o impar
Crea un funcion que calcule el factorial de un numero pasado por parametro
Crea una funcion que dados dos numeros mostrara todos los numeros que hay entre ellos

"""

# HOLA MUNDO

def hola(holamundo):

	print("Hola mundo")

hola("holamundo")


# SUMA DE DOS NUMEROS

def sumas(num1, num2):

	suma = num1 + num2

	print(suma)

sumas(5, 5)

# PAR O IMPAR

num = int(input("Ingresa cualquier numero: "))

def pares(par):

	if num%2 == 0:

		print("Este numero es par")

	elif num%2 != 0:

		print("Este numero es impar")

pares(num)


# FACTORIAL


num = int(input("Ingresa un numero: "))

def factorial(f):

	fact_total = 1
	
	while f > 1:
		fact_total *= f

		f -= 1


		print(f, " > ", end="")

	print(" = ", fact_total)

factorial(num)




# ENTRE NUMEROS

num1 = int(input("Ingrese el primer rango de numero: "))
num2 = int(input("Ingrese el segundo rango de numero: "))

def rangos(num1, num2):

	for i in range(num1,num2):
		print(i)

rangos(num1, num2)
