# EXAMEN PROGRAMACION VISUAL

# EJERCICIO 7: DESCUENTO

# DATOS DE USUARIO

"""
NOMBRE: Miguel David Palma Lara

MATERIA: Programacion Visual

ID: 00294955

"""



def descuento(desc, importe):

	dicc = {
	
	"Descuento": desc,
	"Importe": importe

	}

	print("El importe del producto es: $" + str(dicc["Importe"]) + " Y su descuento es de: " + str(dicc["Descuento"]) + "%")

descuento(15, 1500)


