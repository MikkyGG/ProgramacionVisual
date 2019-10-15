# EXAMEN PROGRAMACION VISUAL

# EJERCICIO 5: DICCIONARIO

# DATOS DE USUARIO

"""
NOMBRE: Miguel David Palma Lara

MATERIA: Programacion Visual

ID: 00294955

"""

print("Bienvenido! porfavor ingresa los siguientes datos: \n")

nombre = input("Nombre: ")

edad = int(input("Edad: "))

direccion = input("Direccion: ")

telefono = int(input("Telefono: "))

dicc = {
	
"Nombre": nombre,
"Edad": edad,
"Direccion": direccion,
"Telefono": telefono	

}

def diccionario(dicc):

	print(dicc["Nombre"], "tiene", dicc["Edad"], "años, vive en", dicc["Direccion"], " y su telefono es:", dicc["Telefono"])

diccionario(dicc)