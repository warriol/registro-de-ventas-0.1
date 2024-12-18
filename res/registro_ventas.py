import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Función para agregar una venta a la base de datos
def agregar_venta():
    producto = entry_producto.get()
    cantidad = entry_cantidad.get()
    precio = entry_precio.get()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if producto and cantidad and precio:
        conn = sqlite3.connect('ventas.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO ventas (producto, cantidad, precio, fecha)
        VALUES (?, ?, ?, ?)
        ''', (producto, cantidad, precio, fecha))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Venta registrada exitosamente")
        entry_producto.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

# Función para mostrar los productos en una nueva ventana
def mostrar_productos():
    # Crear una nueva ventana
    ventana_productos = tk.Toplevel(root)
    ventana_productos.title("Productos Registrados")
    
    # Conectar a la base de datos
    conn = sqlite3.connect('ventas.db')
    cursor = conn.cursor()
    
    # Obtener todos los productos de la base de datos
    cursor.execute('SELECT * FROM ventas')
    productos = cursor.fetchall()
    
    # Mostrar los productos en la nueva ventana
    for i, producto in enumerate(productos):
        tk.Label(ventana_productos, text=f"ID: {producto[0]}, Producto: {producto[1]}, Cantidad: {producto[2]}, Precio: {producto[3]}, Fecha: {producto[4]}").grid(row=i, column=0, padx=10, pady=5)
    
    # Cerrar la conexión a la base de datos
    conn.close()

# Crear la ventana principal
root = tk.Tk()
root.title("Registro de Ventas")

# Crear los widgets
tk.Label(root, text="Producto").grid(row=0, column=0, padx=10, pady=5)
entry_producto = tk.Entry(root)
entry_producto.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Cantidad").grid(row=1, column=0, padx=10, pady=5)
entry_cantidad = tk.Entry(root)
entry_cantidad.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Precio").grid(row=2, column=0, padx=10, pady=5)
entry_precio = tk.Entry(root)
entry_precio.grid(row=2, column=1, padx=10, pady=5)

btn_agregar = tk.Button(root, text="Agregar Venta", command=agregar_venta)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

btn_mostrar = tk.Button(root, text="Mostrar Productos", command=mostrar_productos)
btn_mostrar.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()