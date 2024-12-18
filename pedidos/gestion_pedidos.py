import tkinter as tk

def abrir_registrar_pedidos():
    ventana = tk.Toplevel()
    ventana.title("Registrar Pedidos")
    tk.Label(ventana, text="Registrar Pedidos").pack()

def abrir_modificar_pedidos():
    ventana = tk.Toplevel()
    ventana.title("Modificar Pedidos")
    tk.Label(ventana, text="Modificar Pedidos").pack()

def abrir_ver_pedidos():
    ventana = tk.Toplevel()
    ventana.title("Ver Pedidos")
    tk.Label(ventana, text="Ver Pedidos").pack()

if __name__ == '__main__':
    abrir_registrar_pedidos()
    abrir_modificar_pedidos()
    abrir_ver_pedidos()