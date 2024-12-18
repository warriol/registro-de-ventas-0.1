import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('ventas.db')

# Crear un cursor
cursor = conn.cursor()

# Crear la tabla de ventas
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL,
    fecha TEXT NOT NULL
)
''')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Tabla creada exitosamente")