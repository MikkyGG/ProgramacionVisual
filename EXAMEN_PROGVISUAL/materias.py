# EXAMEN PROGRAMACION VISUAL

# EJERCICIO 4: MATERIAS

# DATOS DE USUARIO

"""
NOMBRE: Miguel David Palma Lara

MATERIA: Programacion Visual

ID: 00294955

"""


asignaturas = int(input("Ingresa el numero de materias a ingresar: "))

def materias(asignaturas):

	lista_m = []

	for i in range(asignaturas):

		materia = input("Ingrese la materia " + str(i+1) + ": ")

		lista_m.append(materia)

	print("Tus materias son :", lista_m)

materias(asignaturas)

