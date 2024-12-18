import tkinter as tk
from tkinter import messagebox
import sqlite3

class GestionClientes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Gestión de Clientes", font=('Helvetica', 16)).grid(row=0, column=0, columnspan=2, pady=10)

        btn_agregar = tk.Button(self, text="Agregar Cliente", command=self.agregar_cliente)
        btn_agregar.grid(row=1, column=0, padx=10, pady=10)

        btn_mostrar = tk.Button(self, text="Mostrar Clientes", command=self.mostrar_clientes)
        btn_mostrar.grid(row=1, column=1, padx=10, pady=10)

    def agregar_cliente(self):
        def guardar_cliente():
            nombre = entry_nombre.get()
            telefono = entry_telefono.get()

            if nombre and telefono:
                conn = sqlite3.connect('mi_aplicacion.db')
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO clientes (nombre, telefono)
                VALUES (?, ?)
                ''', (nombre, telefono))
                conn.commit()
                conn.close()
                messagebox.showinfo("Éxito", "Cliente agregado exitosamente")
                ventana_agregar.destroy()
                self.mostrar_clientes()
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

        ventana_agregar = tk.Toplevel(self)
        ventana_agregar.title("Agregar Cliente")

        tk.Label(ventana_agregar, text="Nombre").grid(row=0, column=0, padx=10, pady=5)
        entry_nombre = tk.Entry(ventana_agregar)
        entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana_agregar, text="Teléfono").grid(row=1, column=0, padx=10, pady=5)
        entry_telefono = tk.Entry(ventana_agregar)
        entry_telefono.grid(row=1, column=1, padx=10, pady=5)

        btn_guardar = tk.Button(ventana_agregar, text="Guardar", command=guardar_cliente)
        btn_guardar.grid(row=2, column=0, columnspan=2, pady=10)

    def mostrar_clientes(self):
        for widget in self.grid_slaves():
            if int(widget.grid_info()["row"]) > 2:
                widget.grid_forget()

        conn = sqlite3.connect('mi_aplicacion.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clientes')
        clientes = cursor.fetchall()
        conn.close()

        for i, cliente in enumerate(clientes):
            tk.Label(self, text=f"ID: {cliente[0]}, Nombre: {cliente[1]}, Teléfono: {cliente[2]}").grid(row=i+3, column=0, columnspan=2, padx=10, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Gestión de Clientes")
    frame = GestionClientes(root, None)
    frame.pack(fill="both", expand=True)
    root.mainloop()