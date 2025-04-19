# Crear una función que reciba un número y devuelva si es par o impar

# Definir la función
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"


# Pedir un número al usuario
num = int(input("Introduce un número: "))


# Llamar a la función y mostrar el resultado
print(es_par_o_impar(num))