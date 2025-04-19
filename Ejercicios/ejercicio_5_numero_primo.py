# Escribe un programa que pida un número al usuario y determine si es primo o no. Un número primo es aquel que solo es divisible por 1 y por sí mismo

# Pedimos un número al usuario
numero = int(input("Introduce un número: "))

# Un número menor que 2 no es primo
if numero < 2:
    print(f"El número {numero} no es primo.")
else:
    es_primo = True # Suponemos que es primo
    for i in range(2, int(numero ** 0.5) + 1): # Revisamos hasta la raíz cuadrada del número
        if numero % i == 0: # Si es divisible por otro número, no es primo
            es_primo = False
            break # Salimos del bucle si encontramos un divisor

    # Mostramos el resultado
    if es_primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")

# Si el número es menor que 2, se descarta automáticamente.
# Se asume que el número es primo (es_primo = True)
# Se usa un for que recorre desde 2 hasta la raíz cuadrada del número (NOTA: Optimización)
# Si se encuentra un divisor (numero % i == 0), se marca como no primo y se detiene el bucle (break)
# Al final se imprime el resultado



