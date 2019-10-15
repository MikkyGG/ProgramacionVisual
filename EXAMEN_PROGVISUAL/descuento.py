# EXAMEN PROGRAMACION VISUAL

# EJERCICIO 7: DESCUENTO

# DATOS DE USUARIO

"""
NOMBRE: Miguel David Palma Lara

MATERIA: Programacion Visual

ID: 00294955

"""

desc = int(input("Ingresa el porcentaje de descuento: "))

importe = float(input("Ingresa el importe del producto: "))

def descuento(desc, importe):

	dicc = {
	
	"Descuento": desc,
	"Importe": importe

	}

	descuentos = importe * desc / 100 

	resultado = importe - descuentos

	print("El importe del producto es: $" + str(dicc["Importe"]) + " y su descuento es de: " + str(dicc["Descuento"]) + "%")

	print("El costo del producto despues del descuento es de: $", resultado)

descuento(desc, importe)


