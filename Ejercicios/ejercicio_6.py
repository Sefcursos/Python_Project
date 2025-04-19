# NIVEL 1
# Usando uno de los operadores de comparación en Python,
# escribe un programa simple de dos líneas que tome el parámetro n como entrada,
# que es un entero, e imprime False si n es menor que 100, y True if n es mayor o igual que 100.


# n = int(input("Introduce un número: "))
# print("Es mayor o igual a 100" if n>= 100 else "Es menor que 100")

# NIVEL 2
# Que acepte varios números uno tras otro
# Que detecte si el dato introducido no es número
# Que finalice cuando el usuario escriba "salir"
# Después de salir que siga mostrando el número es mayor o igual a 100 o menor.


# while True:
#     entrada = input("Introduce un número (o escribe 'salir' para terminar):" )
#     if entrada.lower() == "salir":
#         print("Programa finalizado 🔚.")
#         break
#     try:
#         n = int(entrada)
#         print("✅ Es mayor o igual a 100" if n >= 100 else " ❌ Es menor que 100")
#     except ValueError:
#         print("⚠️ Entrada no válida. Por favor Eduardo, introduce un numero entero o 'salir'.")


# NIVEL 3
# Acepta múltiples entradas
# Valida los errores
# Guarda los números en una list
# Al finalizar, muestre un resumen de cuantós números fueron mayores o iguales a 100 y cuántos fueron menores.

# mayores = []
# menores = []
#
# while True:
#     entrada = input("Introduce un número (o escribe 'salir' para terminar): ")
#
#     if entrada.lower() == "salir":
#         print("\n🔚 Programa finalizado. Mostrando resumen..\n")
#         break
#
#     try:
#         n = int(entrada)
#         if n >= 100:
#             mayores.append(n)
#             print("✅ Es mayor o igual a 100")
#         else:
#             menores.append(n)
#             print("❌ Es menor que 100")
#     except ValueError:
#         print("⚠️ Entrada no válida. Por favor, introduce un número entero o 'salir'.")
#
# # Mostrar resumen
# print("📊  RESUMEN")
# print(f"🔵 Números mayores o iguales a 100: {len(mayores)} -> {mayores}")
# print(f"🔴 Números menores que 100: {len(menores)} -> {menores}")

# En Python len() se utiliza para obtener la cantidad de elementos que hay en una colección, como: Listas, Cadenas de texto (str), Diccionarios, etc..
# Listas
# alumnos = ["Miguel", "Mariano", "Eduardo", "Jennifer"]
# print(len(alumnos)) # Resultado es 4 alumnos.

# Parentesis (): Se usan llamar funciones, agrupar operaciones, definir argumentos, etc...
# print("Hola Jennifer") # Print es una función
#
# resultado = (3 + 5) * 2 # Prioridad en la suma
#
# def saludar(nombre):
#     print("Hola", nombre)

# Corchetes [] se utilizan para crear listas, acceder a elementos con indices, modificar listas, Slicing (corte de listas o string)
# mi_lista = [10, 20, 30]
#
# print(mi_lista[0]) # Imprime 20
#
# mi_lista[0] = 100
#
# print(mi_lista[0:2]) # Imprime [100, 20]

# Las llaves {} estas se utilizan en diccionarios, conjuntos(sets)
persona = {
    "nombre": "Jennifer",
    "edad": 24,
    "ciudad": "Alcantarilla"
}
print(persona["nombre"]) # Imprime: Jennifer
print(persona["edad"])
print(persona["ciudad"])

# Conjuntos(sets) -> Colecciones sin elementos repetidos, no tienen ni orden, ni índices
numeros = {1, 2, 3, 4, 4, 3, 2, 1}
print(numeros) # Imprime: {1, 2, 3}

numeros2 = (1, 2, 3, 4, 4, 3, 2, 1)
print(numeros2)