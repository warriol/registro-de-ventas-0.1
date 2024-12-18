import tkinter as tk

def abrir_gestion_clientes():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Clientes")
    tk.Label(ventana, text="Gestión de Clientes").pack()

if __name__ == '__main__':
    abrir_gestion_clientes()