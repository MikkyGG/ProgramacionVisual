# APUNTES DE CLASE 1:

# VARIABLES Y ASIGNACION DE VARIABLES Y FORMATOS

name = "Miguel"
edad = 19

print(name)
print(edad)

nombre = "Ada"
apellido = "Lovelace"

fullname = nombre + " " + apellido
print(fullname)

fullname = '{} {}'.format(nombre, apellido)
print(fullname)

print(name.title())
print(name.upper())
print(name.lower())

# Para saber el tipo de variable;;;;;P

print(type(nombre))
print(type(edad))

mensaje = 'Feliz Cumple ' + str(edad) + '!.'
print(mensaje)

falso = False
true = True

print(falso)
print(true)
print(type(falso))
print(type(falso))