# Cada vez que recibe una entrada en forma de la palabra Espatifilo, grite involuntariamente a la consola la siguiente cadena: "¡Espatifilo es la mejor planta de todas!"
# Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:
# imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILIO" (mayúsculas)
# imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
# imprima "¡Espatifilo!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.

entrada = input("Introduce el nombre de una planta: ")

if entrada == "ESPATIFILIO":
    print("Si - !El Espatifilo! es la mejor planta de todos los tiempos!")
elif entrada == "espatifilo":
    print("No, !quiero un gran Espatifilo!")
else:
    print(f"!Espatifilo!, !No {entrada}!")

