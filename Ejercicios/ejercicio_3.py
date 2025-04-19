# Tienen que hacer un ejercicio que pida al usuario un número y luego sume todos los números desde 1 hasta ese número usando un bucle for

# Pedimos un número al usuario
numero = int(input("Introduce un número: "))

# Iniciamos la variable para la suma
suma_total = 0

# Usamos el bucle for para sumar los números del 1 al número ingresado
for i in range(1, numero + 1):
    suma_total += i # Sumamos cada número

# Mostramos el resultado
print(f"La suma de los números del 1 al {numero} es: {suma_total}")
