# EXAMEN PROGRAMACION VISUAL

# EJERCICIO 2: SECRETO

# DATOS DE USUARIO

"""
NOMBRE: Miguel David Palma Lara

MATERIA: Programacion Visual

ID: 00294955

"""

palabra = "progvisual"

def secreto(palabra):

	secreto = input("Ingresa la palabra secreta: ")
	secreto = secreto.lower()

	if secreto == palabra:

		print("Palabra correcta, bienvenido!")

	else:
		print("Palabra incorrecta, intentalo de nuevo")


secreto(palabra)