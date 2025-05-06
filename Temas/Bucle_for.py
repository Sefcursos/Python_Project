# Bucle for: Se utiliza cunado queremos recorrer una secuencia como una lista, tupla, cadena, o rango de números.

# Ejercicio 1: Contar del 1 al 10
for i in range(1, 11):
    print(i)

# Ejercicio 2: Sumar todos los números de una lista
numeros = [1, 2, 3, 4, 5]
suma = 0
for num in numeros:
    suma += num
print("La suma es: ", suma)

# Ejercicio 3: Mostrar cada letra de una palabra
palabra = "python"
for letra in palabra:
    print(letra)

# Ejercicio 4: Números pares del 1 al 20, Debemos imprimir solo los números pares del 1 al 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Ejercicio 5: Crear un generador de contraseñas simples. Crear una lista de combinaciones de palabras y números como posibles contraseñas.
palabras = ['admin', 'user', 'test']
numeros = ['123', '2024', '000']

for palabra in palabras:
    for numero in numeros:
        print(palabra + numero)

# Ejercicio 6: Ataque de diccionario (simulado). Debemos intentar adivinar una contraseña usando una lista de posibles claves
diccionario = ['1234', 'admin', 'password', 'qwerty', 'hackme']
clave_real = 'hackme'

for intento in diccionario:
    print(f"Probando: {intento}")
    if intento == clave_real:
        print("!Contraseña encontrada!")
        break

# Ejercicio 7: Escaneo de puertos (simulado)
puertos_abierto = [21, 22, 80]

for puerto in range(20, 91):
    print(f"Escaneando puerto {puerto}...")
    if puerto in puertos_abierto:
        print(f"Puerto {puerto} está ABIERTO")

