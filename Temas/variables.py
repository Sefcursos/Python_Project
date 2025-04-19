# Print muestra información en la pantalla
print("Hola Mundo, se me daño mi ordenador :(")

# Tipos de datos
numero = 10       # Entero (int)
texto = "Hola"    # Cadena de texto (str) (string)
decimal = 3.14    # Decimal (float)
booleano = True   # Booleano (bool)
tuple = (1, 2, 3)  # Lista inmutable


# Para leer datos del usuario, usamos "input()". Siempre devuelve una cadena (String), por lo que a veces hay que convertirla
# input solicita un dato alusuario si lo utilizamos junto a int convierte ese dato en un entero
nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre)

#  Si queremos un numero lo convertimos
edad = int(input("¿Cuantos años tienes? "))
print("En 10 años tendrás", edad + 10)

# Operadores básicos en Python
# Suma
a = 3 + 2
print(a)  #5

# Resta
b = 10 - 4
print(b)

# Multiplicación
c = 6 * 7
print(b) #6

# División
d = 8 / 3
print(d) # 2.666666666665

# Division entera // (sin decimales, redondea hacia abajo
e = 8 // 3
print(e) #2

# Módulo % (resto de la división, útil para saber sin un número es par o impar)
f = 10 % 3
print(f) #1 (porque 10 / 3 = 3, sobra 1

# Potencia ** (elevar un número a otro)
g = 2 ** 3
print(g) #8 (2 x 2 x 2)

