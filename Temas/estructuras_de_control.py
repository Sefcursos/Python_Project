# Condicionales if, elif, else. NOTA: No se usan parentesis en la condición y el bloque de código debe estar indentado
edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
elif edad > 12:
    print("Eres un adolescente.")
else:
    print("Eres un baby.")

# Bucles (for y while)
# for (Bucle de rango) en python se utiliza principalmente para iterar sobre listas o rangos númericos

for i in range(5): # Este va de 0 a 4
    print("Iteración:", i)

Archivos= ["Audios", "Video", "Obj"]
for Archivos in Archivos:
    print("Me gusta la", Archivos)

# while (Bucle condicional) este ejecuta el código mientras una condición sea verdadera
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1 # Equivalente a contador++

# Operadores de asignación, son usados para asignar valores a variables (=, +=, -=, *=, /=, //=, %=, **=)

# = Asigna un valor,  x es ahora 5
# += Suma y asigna,   x = x + 3
# -= Resta y asigna,  x = x - 2
# *= Multiplica y asigna,  x = x * 4
# /= Divide y asigna,  x = x / 2
# //= División entera y asigna,  x = x // 3
# %= Módulo y asigna, x = x % 2
# **= Potencia y asigna, x = x **3

x = 10
x += 5     # Ahora x es 15 (10 + 5)
x -= 3     # Ahora x es 12 (15 - 3)
x *= 2     # Ahora x es 24 (12 * 2)
x /= 4     # Ahora x es 6.0 (24 / 4)

# Operadores de comparación (==, !=, >, <, >=, <=)

# == Igualdad
# != Diferente
# > Mayor que
# < Menor que
# >= Mayor o igual
# <= Menor o igual

a = 10
b = 5

print(a == b) # False (10 no es igual a 5)
print(a != b) # True (10 es diferente de 5)
print(a > b) # True (10 es mayor que 5)
print(a < b) # False ( 10 no es menor que 5)
print(a >= 10) # True (10 es igual a 10)
print(b <= 5) # True (5 es igual a 5)

# Operadores lógicos
# and Verdadero si ambas condiciones son verdaderas      x and y => False
# or  Verdadero si al menos una condicion es verdadera   x or y => True
# not Invierte el valor lógico                           not x => False

# Los : en Python se utilizan para denotar el inicio de un bloque de codigo, que pertenece a una estructura de control como un if, for, while
if x > 5:
    print("Mayor que 5")

# El ; se utiliza para terminar la instrucción

