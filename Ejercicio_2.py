"""

Ejercicio de Python 2. Cuadrado de un numero
Nombre: Miguel David Palma Lara
Materia: Programacion Visual

"""

mul = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for r in range(1, 11):

	mul.append(r**2)

print(mul)

# Comprension de listas

mul2 = [r**2 for r in range(1, 11)]
print("Otra forma ", mul2)

print(min(mul2))
print(max(mul2))
print(sum(mul2))