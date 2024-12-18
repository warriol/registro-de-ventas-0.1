import tkinter as tk

def abrir_registrar_compras():
    ventana = tk.Toplevel()
    ventana.title("Registrar Compras")
    tk.Label(ventana, text="Registrar Compras").pack()

def abrir_modificar_compras():
    ventana = tk.Toplevel()
    ventana.title("Modificar Compras")
    tk.Label(ventana, text="Modificar Compras").pack()

def abrir_ver_compras():
    ventana = tk.Toplevel()
    ventana.title("Ver Compras")
    tk.Label(ventana, text="Ver Compras").pack()

if __name__ == '__main__':
    abrir_registrar_compras()
    abrir_modificar_compras()
    abrir_ver_compras()