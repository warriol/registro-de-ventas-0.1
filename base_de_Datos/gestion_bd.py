import sqlite3

def conectar():
    return sqlite3.connect('mi_aplicacion.db')

def crear_tablas():
    with conectar() as conn:
        cursor = conn.cursor()
        with open('base_de_datos/esquema.sql', 'r') as f:
            cursor.executescript(f.read())
        conn.commit()

if __name__ == '__main__':
    crear_tablas()