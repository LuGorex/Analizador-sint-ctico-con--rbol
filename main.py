import tkinter as tk
from mainwindowtk import MainWindow  # Importa la clase migrada a tkinter

if __name__ == "__main__":
    root = tk.Tk()  # Inicializa la ventana principal
    app = MainWindow(root)  # Crea una instancia de MainWindow
    root.mainloop()  # Inicia el bucle de eventos