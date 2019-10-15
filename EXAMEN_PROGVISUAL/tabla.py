# EXAMEN PROGRAMACION VISUAL

# EJERCICIO 3: TABLA

# DATOS DE USUARIO

"""
NOMBRE: Miguel David Palma Lara

MATERIA: Programacion Visual

ID: 00294955

"""


numero = int(input("Ingresa el numero a multiplicar: "))

def tabla(numero):

	contador = 1

	for i in range(1, 11):

		resultado = numero * contador


		print(numero, "*", contador, "= ", resultado)

		contador = contador + 1

tabla(numero)