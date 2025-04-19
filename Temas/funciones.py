# ¿Que son las funciones? son bloques de codigo que se pueden reutilizar simplemente llamando a la función.
# Esto permite la reutilización de codigo simple y elegante sin volver a escribir explicitamente secciones de código
# En Python se definen con def, seguidas de un nombre de función y parametros de funcion entre parentesis
# Una función siempre devuelve un valor. La función utiliza la palabra clave return para devolver un valor y si no, queremos devolver un valor utilizamos none

def saludar():
    print("!Hola! Bienvenido al curso de python")

# Llamar a la función, se puede llamar cuantas veces quieres, tener en cuenta, que esto puede cargar el sistema
saludar()

# Funciones con parentesis, podemos pasar valores a una función para que trabaje con ellos

def saludar2(nombre):
    print("Hola,", nombre)

saludar2("Kali") # Salida: Hola, kali

def sumar(a, b, c, d, e, f):
    resultado = a + b + c + d + e + f
    print("La suma es: ", resultado)

sumar(3, 7, 10, 20, 30, 40)  # Salida: La suma es: 110

# Si queremos que una función devuelva un valor

def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 5)
print("·El resultado es: ", resultado)

# Funciones con valores por defecto, se utiliza cuando queremos que un parámetro tenga un valor predeterminado
def presentar(nombre, edad=18):
    print("Nombre:", nombre)
    print("Edad:", edad)

presentar("Miguel") # Toma la edad por defecto (18)
presentar("Jennifer", 25) # Aquí usamos 25 en vez de 19, toma la edad que le hemos puesto, en vez de los 18 por defecto







