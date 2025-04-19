# Escribe un programa que pida al usuario un número y muestre su tabla de multiplicar del 1 al 10 usando un bucle for

# Pedimos un número al usuario
numero = int(input("Introduce un número: "))


# Usamos un bucle for para generar la tabla de multiplicar
for i in range(1, 11): # Desde 1 hasta 10
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
