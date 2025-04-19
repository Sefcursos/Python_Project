#GESTOR DE NOTAS - BÁSICO

# Creamos listas vacías para guardar nombres y notas
alumnos = []
notas = []

# Cuántos alumnos se van a introducir en el programa
total = int(input("¿Cuántos alumnos quieres registrar?: "))

# Recorremos un bucle para registrar datos
for i in range(total):
    nombre = input(f"Introduce el nombre del alumno {i + 1}: ")
    nota = float(input(f"Introduce la nota de {nombre}: "))

# Usaremos un append, el append es un método que se usa en Python con listas para añadir un elemento al final de la lista.
    alumnos.append(nombre)
    notas.append(nota)

print("\n RESULTADOS ")
print("--------------------")

# Mostramos resultados y quién aprueba o suspende
for i in range(total):
    if notas[i] >= 9:
        estado = "EXCELENTE"
    elif notas[i] >= 5:
        estado = "APROBADO"
    else:
        estado = "SUSPENDIDO"
    print(f"{alumnos[i]} - Nota: {notas[i]} - {estado}")

# Calculamos la media
media = sum(notas) / total
print(f"\nMedia de la clase: {media: .2f}")

# Hemos aprendido
# Uso de input(), float, int
# Control de flujo con for y if-else
# Uso de listas (append, sum, índices)
# Formateo de texto (:.2f para limitar decimales)