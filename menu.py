import tkinter as tk
from clientes.vistas_clientes import GestionClientes
from productos.vistas_productos import GestionProductos
from compras.vistas_compras import GestionCompras
from pedidos.vistas_pedidos import GestionPedidos
from cierre.vistas_cierre import GestionCierre

def mostrar_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.title("Menú Principal")
root.geometry("800x600")

# Crear un contenedor para los marcos
container = tk.Frame(root)
container.pack(side="top", fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Inicializar los marcos
frames = {}
for F in (GestionClientes, GestionProductos, GestionCompras, GestionPedidos, GestionCierre):
    page_name = F.__name__
    frame = F(parent=container, controller=root)
    frames[page_name] = frame
    frame.grid(row=0, column=0, sticky="nsew")

# Crear el menú
menu = tk.Menu(root)
root.config(menu=menu)

gestion_menu = tk.Menu(menu)
menu.add_cascade(label="Gestión", menu=gestion_menu)
gestion_menu.add_command(label="Gestión de Clientes", command=lambda: mostrar_frame(frames["GestionClientes"]))
gestion_menu.add_command(label="Gestión de Productos", command=lambda: mostrar_frame(frames["GestionProductos"]))

compras_menu = tk.Menu(menu)
menu.add_cascade(label="Compras", menu=compras_menu)
compras_menu.add_command(label="Registrar Compras", command=lambda: mostrar_frame(frames["GestionCompras"]))
compras_menu.add_command(label="Modificar Compras", command=lambda: mostrar_frame(frames["GestionCompras"]))
compras_menu.add_command(label="Ver Compras", command=lambda: mostrar_frame(frames["GestionCompras"]))

pedidos_menu = tk.Menu(menu)
menu.add_cascade(label="Pedidos", menu=pedidos_menu)
pedidos_menu.add_command(label="Registrar Pedidos", command=lambda: mostrar_frame(frames["GestionPedidos"]))
pedidos_menu.add_command(label="Modificar Pedidos", command=lambda: mostrar_frame(frames["GestionPedidos"]))
pedidos_menu.add_command(label="Ver Pedidos", command=lambda: mostrar_frame(frames["GestionPedidos"]))

menu.add_command(label="Cierre del Día", command=lambda: mostrar_frame(frames["GestionCierre"]))
menu.add_command(label="Salir", command=root.quit)

# Mostrar el primer marco
mostrar_frame(frames["GestionClientes"])

root.mainloop()