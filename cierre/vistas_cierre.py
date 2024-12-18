import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class GestionCierre(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Cierre del Día", font=('Helvetica', 16)).grid(row=0, column=0, columnspan=2, pady=10)

        btn_cierre = tk.Button(self, text="Realizar Cierre del Día", command=self.realizar_cierre)
        btn_cierre.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def realizar_cierre(self):
        today = datetime.now().strftime("%Y-%m-%d")
        
        conn = sqlite3.connect('mi_aplicacion.db')
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT SUM(precio * cantidad) FROM compras WHERE DATE(fecha) = ?
        ''', (today,))
        
        total_ventas = cursor.fetchone()[0]
        conn.close()

        if total_ventas is not None:
            self.result_label.config(text=f"Total de ventas del día: ${total_ventas:.2f}")
        else:
            self.result_label.config(text="No se encontraron ventas para el día de hoy")
        
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Cierre del Día")
    root.geometry("800x600")
    GestionCierre(root, None).pack()
    root.mainloop()