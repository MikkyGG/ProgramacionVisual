# EXAMEN PROGRAMACION VISUAL

# EJERCICIO 1: IMC

# DATOS DE USUARIO

"""
NOMBRE: Miguel David Palma Lara

MATERIA: Programacion Visual

ID: 00294955

"""

print("Bienvenido al programa IMC, porfavor ingresa tus datos...\n")

peso = float(input("Ingresa tu peso en kg: "))

estatura = float(input("Ingresa tu estatura en metros: "))


def indice_masa(peso, estatura):


	imc = peso / (estatura*estatura)

	imc = round(imc, 2)

	rango = ["Delgadez muy severa", "Delgadez Severa", "Delgadez", "Peso Saludable", "Sobrepeso", "Obesidad Moderada", "Obesidad Severa", "Obesidad Morbida"]

	if imc <= 15:

		print("Tu IMC es de:", imc, "por lo cual tu tienes:", rango[0])

	elif imc <= 15.9:

		print("Tu IMC es de:", imc, "por lo cual tu tienes:", rango[1])

	elif imc >= 16 and imc <= 18.4:

		print("Tu IMC es de:", imc, ", por lo cual tu tienes:", rango[2])

	elif imc >= 18.5 and imc <= 24.9:

		print("Tu IMC es de:", imc, ", por lo cual tu tienes:", rango[3])

	elif imc >= 25 and imc <= 29.9:

		print("Tu IMC es de:", imc, ", por lo cual tu tienes:", rango[4])

	elif imc >= 30 and imc <= 34.9:

		print("Tu IMC es de:", imc, ", por lo cual tu tienes:", rango[5])

	elif imc >= 35 and imc <= 39.9:

		print("Tu IMC es de:", imc, ", por lo cual tu tienes:", rango[6])

	elif imc >= 40:

		print("Tu IMC es de:", imc, ", por lo cual tu tienes:", rango[7])

indice_masa(peso, estatura)