import tkinter as tk

def abrir_cierre_del_dia():
    ventana = tk.Toplevel()
    ventana.title("Cierre del Día")
    tk.Label(ventana, text="Cierre del Día").pack()

if __name__ == '__main__':
    abrir_cierre_del_dia()