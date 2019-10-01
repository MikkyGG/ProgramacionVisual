"""

Ejercicio de Python 5: VALIDACION DE EDADES
Nombre: Miguel David Palma Lara
Materia: Programacion Visual

"""

print("BIENVENIDO A LA FERIA!")

print("______________________________________")

edad = int(input("Ingresa tu edad: "))

if edad < 4:
	print("Tu entrada de niño es gratuita, que te diviertas!")

elif edad < 18:
	print("Tu entrada normal es de: $50 MXN, que te diviertas!")

else:
	print("Tu entrada de adulto es de: $100 MXN, que te diviertas!")



""" 

SEGUNDA FORMA

"""

if edad < 4:
	precio = "Tu entrada de niño es gratuita, que te diviertas!"

elif edad < 18:
	precio = "Tu entrada normal es de: $50 MXN, que te diviertas!"

else:
	precio = "Tu entrada de adulto es de: $100 MXN, que te diviertas!"

print(precio)


"""

TERCERA FORMA

"""

if edad < 4:
	precio = 0

elif edad < 18:
	precio = 50

else:
	precio = 100

print("La entrada por tu edad tiene un coste de: $" + str(precio) + " MXN")