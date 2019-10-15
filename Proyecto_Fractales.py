from turtle import *


# MARTA LORENA GAZO MORALES



# PROYECTO FRACTALES


# INICIO DE CODIGO DE FRACTALES

#######################################################################################

# ACOIRIS GEOMETRICO

def fractal_arcoiris():
	
	# VALORES PARA PERSONALIZAR EL TURTLE
	reset()
	bgcolor("Black")
	c = ("Red", "Orange", "Yellow", "Lime Green", "Deep Sky Blue", "Royal Blue", "Purple")
	pensize(2)
	speed(0)


	# INICIO DEL CODIGO ARCOIRIS

	print("")

	print("BIENVENIDO AL ARCOIRIS GEOMETRICO!")

	print("")


	# PARAMETROS INGRESADOS POR EL USUARIO Y VALIDACION DE PARAMETROS

	while True:
		try:
			lado = int(input("Ingrese el numero de lados (A partir de 2 y se recomienda hasta 30): "))
			if lado < 2:
				raise ValueError("Numero invalido")
			break
		except:
			print("NUMERO INVALIDO - Ingresa un numero mayor a 1 \n")



	n_min = int(input("Ingresa el largo minimo de los lados (Puede ser positivo o negativo): "))



	while True:
		try:
			n = int(input("Ingrese el largo maximo de los lados (Solo positivos y mayor al largo minimo): "))
			if n < 1 or n <= n_min:
				raise ValueError("Numero invalido")
			break
		except:
			print("NUMERO INVALIDO - Ingresa un numero mayor a 0 y mayor que el largo minimo \n")



	# DEF PARA CREAR LAS FORMAS GEOMETRICAS

	def formas(lado, n):
	
		for i in range(lado):
			forward(n)
			right(360/lado)
	

	# DEF QUE DA INICIO AL ARCOIRIS

	def arcoiris(n_min, colores, n):
		if (n_min > n or colores < 0):
			return

		elif colores == 6:
			color(c[colores])
			colores = 0
		else:
			color(c[colores])
			colores = colores + 1

		for i in range(lado): 
			forward(n_min)
			right(360/lado)
			i = i + 1	
		
		left(360/lado)
		forward(n_min-1.2)
		formas(lado, n_min-1.2)
		arcoiris(n_min+1, colores, n)


	# LLAMAR AL DEF

	arcoiris(n_min, 1, n)

	

#######################################################################################

# ESPIRALES GEOMETRICOS

def fractal_espirales():

	# PARAMETROS PARA PERSONALIZAR TURTLE

	reset()
	bgcolor("Medium Slate Blue")
	pensize(2)

	speed(0)
	color("Orange")

	# INICIO DEL CODIGO

	print("")

	print("BIENVENIDO A ESPIRALES GEOMETRICOS!")

	print("")


	# PARAMETROS INGRESADOS POR EL USUARIO Y VALIDACION DE PARAMETROS

	while True:
		try:
			lado = int(input("Ingrese el numero de lados (A partir de 2): "))
			if lado < 2:
				raise ValueError("Numero invalido")
			break
		except:
			print("NUMERO INVALIDO - Ingresa un numero mayor a 1 \n")



	while True:
		try:
			n_min = int(input("Ingresa el largo minimo de los lados: "))
			if n_min < 1:
				raise ValueError("Numero invalido")
			break
		except:
			print("NUMERO INVALIDO - Ingresa un numero mayor a 0 \n")


	n = int(input("Ingrese el largo maximo los lados (Numeros positivos): "))

	
	while True:
		try:
			n_saltos = int(input("Ingresa el largo de saltos de los lados (Numeros positivos): "))
			if n_saltos < 1:
				raise ValueError("Numero invalido")
			break
		except:
			print("NUMERO INVALIDO - Ingresa un numero mayor a 0 \n")

	while True:
		try:
			grados = int(input("Ingresa los grados de movimiento (Positivos y Negativos): "))
			if grados == 0 or grados > 360:
				raise ValueError("Numero invalido")
			break
		except:
			print("NUMERO INVALIDO - Ingresa un numero entre 1 a 360 \n")



	# DEF PARA CREAR LAS FIGURAS GEOMETRICAS


	def formas(lado, n):
	
		for i in range(lado):
			forward(n)
			left(360/lado)


	# DEF PARA CREAR LA ESPIRAL

	def espiral():

		for i in range(n_min, n, n_saltos):
			formas(lado, i)
			right(grados)



	# LLAMAR A LA FUNCION

	espiral()

	

#######################################################################################

# ARBOLES GEOMETRICOS

def fractal_arboles():

	# PARAMETROS PARA PERSONALIZAR TURTLE

	reset()
	left(90)
	speed(0)
	pensize(2)

	bgcolor("Peach Puff")
	color("Brown", "Forest Green")

	
	# INICIO DEL CODIGO

	print("")

	print("BIENVENIDO AL ARBOL GEOMETRICO!")

	print("")


	# PARAMETROS INGRESADOS POR EL USUARIO Y VALIDACION DE PARAMETROS

	while True:
		try:
			lado = int(input("Ingrese el numero de lados (A partir de 2): "))
			if lado < 2:
				raise ValueError("Numero invalido")
			break
		except:
			print("NUMERO INVALIDO - Ingresa un numero mayor a 1 \n")

	while True:
		try:
			n = int(input("Ingrese el largo de los lados (A partir de 10): "))
			if n < 10:
				raise ValueError("Numero invalido")
			break
		except:
			print("NUMERO INVALIDO - Ingresa un numero mayor a 10 \n")

	while True:
		try:
			l = int(input("Ingresa el largo del tronco (A partir de 10): "))
			if l < 10:
				raise ValueError("Numero invalido")
			break
		except:
			print("NUMERO INVALIDO - Ingresa un numero mayor a 10 \n")

	while True:
		try:
			ramas = int(input("Ingresa el numero de ramas (A partir de 1): "))
			if ramas < 1:
				raise ValueError("Numero invalido")
			break
		except:
			print("NUMERO INVALIDO - Ingresa un numero mayor a 0 \n")

	while True:
		try:
			hojas = int(input("Ingresa el numero de hojas (A partir de 2): "))
			if hojas < 2:
				raise ValueError("Numero invalido")
			break
		except:
			print("NUMERO INVALIDO - Ingresa un numero mayor a 1 \n")		



	# DEF PARA CREAR LAS FIGURAS GEOMETRICAS

	def formas(lado, n):
		begin_fill()
		for i in range(lado):
			forward(n)
			right(360/lado)
		end_fill()


	# DEF QUE CREA EL TAMAÑO DEL TRONCO PRINCIPAL, LAS RAMAS Y HOJAS

	def fractal(l):

		if (l < 10):
			return

		else:
			forward(l)
			formas(lado, n)
			left(30)
			fractal(ramas*l/hojas)
			right(60)
			fractal(ramas*l/hojas)
			left(30)
			backward(l)
	

	# LLAMAR A LA FUNCION PRINCIPAL

	fractal(l)

	

#######################################################################################

# MENU PRINCIPAL

def menu():
	
	opciones = 0
	
	while opciones!=4:
		
		print("\nBIENVENIDO A MI PROYECTO DE FRACTALES!")
		print("______________________________________")

		print("\nELIJE EL FRACTAL QUE DESEAS CREAR:\n")

		print("______________________________________\n")

		print("(Teclea el numero de opcion a elegir)\n")
		
		print("1.- ARCOIRIS")
		print("2.- ESPIRALES")
		print("3.- ARBOLES")
		print("\n4.- SALIR\n")

		opciones = int(input("OPCION: "))

		if opciones == 1:
			fractal_arcoiris()
		if opciones == 2:
			fractal_espirales()
		if opciones == 3:
			fractal_arboles()


# LLAMAR AL MENU

screen = Screen()
screen.bgcolor("White")

menu()

# SALIR DEL PROGRAMA

print("Hasta la proxima! ~")