import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class GestionPedidos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Gestión de Pedidos", font=('Helvetica', 16)).grid(row=0, column=0, columnspan=2, pady=10)

        btn_agregar = tk.Button(self, text="Registrar Pedido", command=self.registrar_pedido)
        btn_agregar.grid(row=1, column=0, padx=10, pady=10)

        btn_mostrar = tk.Button(self, text="Ver Pedidos", command=self.mostrar_pedidos)
        btn_mostrar.grid(row=1, column=1, padx=10, pady=10)

    def registrar_pedido(self):
        def guardar_pedido():
            cliente_id = entry_cliente_id.get()
            producto_id = entry_producto_id.get()
            cantidad = entry_cantidad.get()
            precio = entry_precio.get()
            fecha_entrega = entry_fecha_entrega.get()

            if cliente_id and producto_id and cantidad and precio and fecha_entrega:
                conn = sqlite3.connect('mi_aplicacion.db')
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO pedidos (fecha, cliente_id, producto_id, cantidad, precio, fecha_entrega)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cliente_id, producto_id, cantidad, precio, fecha_entrega))
                conn.commit()
                conn.close()
                messagebox.showinfo("Éxito", "Pedido registrado exitosamente")
                ventana_registrar.destroy()
                self.mostrar_pedidos()
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

        ventana_registrar = tk.Toplevel(self)
        ventana_registrar.title("Registrar Pedido")

        tk.Label(ventana_registrar, text="ID Cliente").grid(row=0, column=0, padx=10, pady=5)
        entry_cliente_id = tk.Entry(ventana_registrar)
        entry_cliente_id.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana_registrar, text="ID Producto").grid(row=1, column=0, padx=10, pady=5)
        entry_producto_id = tk.Entry(ventana_registrar)
        entry_producto_id.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(ventana_registrar, text="Cantidad").grid(row=2, column=0, padx=10, pady=5)
        entry_cantidad = tk.Entry(ventana_registrar)
        entry_cantidad.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(ventana_registrar, text="Precio").grid(row=3, column=0, padx=10, pady=5)
        entry_precio = tk.Entry(ventana_registrar)
        entry_precio.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(ventana_registrar, text="Fecha de Entrega (YYYY-MM-DD)").grid(row=4, column=0, padx=10, pady=5)
        entry_fecha_entrega = tk.Entry(ventana_registrar)
        entry_fecha_entrega.grid(row=4, column=1, padx=10, pady=5)

        btn_guardar = tk.Button(ventana_registrar, text="Guardar", command=guardar_pedido)
        btn_guardar.grid(row=5, column=0, columnspan=2, pady=10)

    def mostrar_pedidos(self):
        for widget in self.grid_slaves():
            if int(widget.grid_info()["row"]) > 2:
                widget.grid_forget()

        conn = sqlite3.connect('mi_aplicacion.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pedidos')
        pedidos = cursor.fetchall()
        conn.close()

        for i, pedido in enumerate(pedidos):
            tk.Label(self, text=f"ID: {pedido[0]}, Fecha: {pedido[1]}, Cliente ID: {pedido[2]}, Producto ID: {pedido[3]}, Cantidad: {pedido[4]}, Precio: {pedido[5]}, Fecha de Entrega: {pedido[6]}").grid(row=i+3, column=0, columnspan=2, padx=10, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Gestión de Pedidos")
    frame = GestionPedidos(root, None)
    frame.pack(fill="both", expand=True)
    root.mainloop()