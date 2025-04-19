import tkinter as tk
from tkinter import messagebox


class StickFigureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Amigo de las Plantas")

        self.label = tk.Label(root, text="Ingresa el nombre de una planta:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Enviar", command=self.revisar_planta)
        self.button.pack()

        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()

        self.text_resultado = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.text_resultado.pack()

        self.dibujar_muñeco_neutro()

    def dibujar_muñeco_neutro(self):
        self.canvas.delete("all")
        # Cabeza
        self.canvas.create_oval(120, 50, 160, 90, fill="white", outline="black", tag="muñeco")
        # Cuerpo
        self.canvas.create_line(140, 90, 140, 170, width=2, tag="muñeco")
        # Brazos
        self.canvas.create_line(100, 110, 180, 110, width=2, tag="muñeco")
        # Piernas
        self.canvas.create_line(140, 170, 110, 220, width=2, tag="muñeco")
        self.canvas.create_line(140, 170, 170, 220, width=2, tag="muñeco")

    def bailar(self):
        for _ in range(4):
            self.canvas.move("muñeco", 5, 0)
            self.canvas.update()
            self.canvas.after(100)
            self.canvas.move("muñeco", -5, 0)
            self.canvas.update()
            self.canvas.after(100)

    def llorar(self):
        self.dibujar_muñeco_neutro()
        # Lágrimas
        self.canvas.create_oval(130, 80, 135, 90, fill="blue", tag="lágrima")
        self.canvas.create_oval(145, 80, 150, 90, fill="blue", tag="lágrima")
        # Planta marchita
        self.canvas.create_line(250, 250, 250, 230, width=3, fill="brown")
        self.canvas.create_arc(235, 200, 265, 230, start=0, extent=180, style=tk.ARC, outline="darkgreen")

    def mostrar_planta_hermosa(self):
        self.canvas.create_line(250, 250, 250, 200, width=3, fill="green")
        self.canvas.create_oval(240, 180, 260, 200, fill="lightgreen", outline="darkgreen")

    def revisar_planta(self):
        planta = self.entry.get().strip().lower()
        if planta == "spatifilio":
            self.dibujar_muñeco_neutro()
            self.bailar()
            self.mostrar_planta_hermosa()
            self.text_resultado.config(text="¡El espatifilio es la mejor planta de todas!", fg="green")
        else:
            self.text_resultado.config(text="Nooo... esa no es la mejor planta 😢", fg="red")
            self.llorar()


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = StickFigureApp(root)
    root.mainloop()
