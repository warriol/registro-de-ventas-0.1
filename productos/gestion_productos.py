import tkinter as tk

def abrir_gestion_productos():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Productos")
    tk.Label(ventana, text="Gestión de Productos").pack()

if __name__ == '__main__':
    abrir_gestion_productos()