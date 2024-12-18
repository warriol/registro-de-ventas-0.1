import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class GestionCompras(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Gestión de Compras", font=('Helvetica', 16)).grid(row=0, column=0, columnspan=3, pady=10)

        btn_registrar = tk.Button(self, text="Registrar Compras", command=self.registrar_compras)
        btn_registrar.grid(row=1, column=0, padx=10, pady=10)

        btn_modificar = tk.Button(self, text="Modificar Compras", command=self.modificar_compras)
        btn_modificar.grid(row=1, column=1, padx=10, pady=10)

        btn_ver = tk.Button(self, text="Ver Compras", command=self.ver_compras)
        btn_ver.grid(row=1, column=2, padx=10, pady=10)

    def registrar_compras(self):
        def guardar_compra():
            cliente_id = entry_cliente_id.get()
            producto_id = entry_producto_id.get()
            cantidad = entry_cantidad.get()
            precio = entry_precio.get()
            tipo_pago = entry_tipo_pago.get()

            if cliente_id and producto_id and cantidad and precio and tipo_pago:
                conn = sqlite3.connect('mi_aplicacion.db')
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO compras (fecha, cliente_id, producto_id, cantidad, precio, tipo_pago)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cliente_id, producto_id, cantidad, precio, tipo_pago))
                conn.commit()
                conn.close()
                messagebox.showinfo("Éxito", "Compra registrada exitosamente")
                ventana_registrar.destroy()
                self.ver_compras()
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

        ventana_registrar = tk.Toplevel(self)
        ventana_registrar.title("Registrar Compras")

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

        tk.Label(ventana_registrar, text="Tipo de Pago (Contado/Credito)").grid(row=4, column=0, padx=10, pady=5)
        entry_tipo_pago = tk.Entry(ventana_registrar)
        entry_tipo_pago.grid(row=4, column=1, padx=10, pady=5)

        btn_guardar = tk.Button(ventana_registrar, text="Guardar", command=guardar_compra)
        btn_guardar.grid(row=5, column=0, columnspan=2, pady=10)

    def modificar_compras(self):
        # Aquí puedes agregar la lógica para modificar compras si lo deseas
        ventana_modificar = tk.Toplevel(self)
        ventana_modificar.title("Modificar Compras")
        tk.Label(ventana_modificar, text="Modificar Compras").pack()

    def ver_compras(self):
        for widget in self.grid_slaves():
            if int(widget.grid_info()["row"]) > 2:
                widget.grid_forget()

        conn = sqlite3.connect('mi_aplicacion.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM compras
        ''')
        compras = cursor.fetchall()
        conn.close()

        if compras:
            for i, compra in enumerate(compras, start=3):
                tk.Label(self, text=f"Fecha: {compra[1]}, Cliente ID: {compra[2]}, Producto ID: {compra[3]}, Cantidad: {compra[4]}, Precio: {compra[5]}, Tipo de Pago: {compra[6]}").grid(row=i, column=0, columnspan=3, padx=10, pady=5)
        else:
            tk.Label(self, text="No hay compras registradas").grid(row=3, column=0, columnspan=3)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Gestión de Compras")
    root.geometry("800x600")
    GestionCompras(root, None).pack()
    root.mainloop()