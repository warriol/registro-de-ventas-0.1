import tkinter as tk
from tkinter import messagebox
import sqlite3

class GestionProductos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Gestión de Productos", font=('Helvetica', 16)).grid(row=0, column=0, columnspan=2, pady=10)

        btn_agregar = tk.Button(self, text="Agregar Producto", command=self.agregar_producto)
        btn_agregar.grid(row=1, column=0, padx=10, pady=10)

        btn_mostrar = tk.Button(self, text="Mostrar Productos", command=self.mostrar_productos)
        btn_mostrar.grid(row=1, column=1, padx=10, pady=10)

    def agregar_producto(self):
        def guardar_producto():
            nombre = entry_nombre.get()
            cantidad = entry_cantidad.get()
            peso = entry_peso.get()
            precio = entry_precio.get()

            if nombre and cantidad and peso and precio:
                conn = sqlite3.connect('mi_aplicacion.db')
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO productos (nombre, cantidad, peso, precio)
                VALUES (?, ?, ?, ?)
                ''', (nombre, cantidad, peso, precio))
                conn.commit()
                conn.close()
                messagebox.showinfo("Éxito", "Producto agregado exitosamente")
                ventana_agregar.destroy()
                self.mostrar_productos()
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

        ventana_agregar = tk.Toplevel(self)
        ventana_agregar.title("Agregar Producto")

        tk.Label(ventana_agregar, text="Nombre").grid(row=0, column=0, padx=10, pady=5)
        entry_nombre = tk.Entry(ventana_agregar)
        entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana_agregar, text="Cantidad").grid(row=1, column=0, padx=10, pady=5)
        entry_cantidad = tk.Entry(ventana_agregar)
        entry_cantidad.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(ventana_agregar, text="Peso").grid(row=2, column=0, padx=10, pady=5)
        entry_peso = tk.Entry(ventana_agregar)
        entry_peso.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(ventana_agregar, text="Precio").grid(row=3, column=0, padx=10, pady=5)
        entry_precio = tk.Entry(ventana_agregar)
        entry_precio.grid(row=3, column=1, padx=10, pady=5)

        btn_guardar = tk.Button(ventana_agregar, text="Guardar", command=guardar_producto)
        btn_guardar.grid(row=4, column=0, columnspan=2, pady=10)

    def mostrar_productos(self):
        for widget in self.grid_slaves():
            if int(widget.grid_info()["row"]) > 2:
                widget.grid_forget()

        conn = sqlite3.connect('mi_aplicacion.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        conn.close()

        for i, producto in enumerate(productos):
            tk.Label(self, text=f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}, Peso: {producto[3]}, Precio: {producto[4]}").grid(row=i+3, column=0, columnspan=2, padx=10, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Gestión de Productos")
    frame = GestionProductos(root, None)
    frame.pack(fill="both", expand=True)
    root.mainloop()