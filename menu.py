import tkinter as tk
from tkinter import messagebox

from clientes.gestion_clientes import abrir_gestion_clientes
from productos.gestion_productos import abrir_gestion_productos
from compras.gestion_compras import abrir_registrar_compras, abrir_modificar_compras, abrir_ver_compras
from pedidos.gestion_pedidos import abrir_registrar_pedidos, abrir_modificar_pedidos, abrir_ver_pedidos
from cierre.gestion_cierre import abrir_cierre_del_dia

def salir():
    root.destroy()

root = tk.Tk()
root.title("Menú Principal")

menu = tk.Menu(root)
root.config(menu=menu)

gestion_menu = tk.Menu(menu)
menu.add_cascade(label="Gestión", menu=gestion_menu)
gestion_menu.add_command(label="Gestión de Clientes", command=abrir_gestion_clientes)
gestion_menu.add_command(label="Gestión de Productos", command=abrir_gestion_productos)

compras_menu = tk.Menu(menu)
menu.add_cascade(label="Compras", menu=compras_menu)
compras_menu.add_command(label="Registrar Compras", command=abrir_registrar_compras)
compras_menu.add_command(label="Modificar Compras", command=abrir_modificar_compras)
compras_menu.add_command(label="Ver Compras", command=abrir_ver_compras)

pedidos_menu = tk.Menu(menu)
menu.add_cascade(label="Pedidos", menu=pedidos_menu)
pedidos_menu.add_command(label="Registrar Pedidos", command=abrir_registrar_pedidos)
pedidos_menu.add_command(label="Modificar Pedidos", command=abrir_modificar_pedidos)
pedidos_menu.add_command(label="Ver Pedidos", command=abrir_ver_pedidos)

menu.add_command(label="Cierre del Día", command=abrir_cierre_del_dia)
menu.add_command(label="Salir", command=salir)

root.mainloop()