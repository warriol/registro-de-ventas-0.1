### Requisitos Previos

Asegúrate de tener Python instalado en tu máquina. Si no lo tienes, puedes descargarlo e instalarlo desde python.org.

### Escoge un Editor de Código

Para escribir código en Python, puedes usar cualquier editor de texto, pero te recomendaría usar un editor de código que haga tu vida más fácil. Aquí hay algunas opciones populares:

    Visual Studio Code (VS Code):
        Descargar: Visual Studio Code
        Instalar Extensión de Python: Una vez que hayas instalado VS Code, abre el editor y ve a la pestaña de extensiones (icono de cuadrado con cuatro lados en la barra lateral izquierda). Busca "Python" e instala la extensión de Microsoft.

### Crear un Nuevo Proyecto
Visual Studio Code (VS Code)

    Abre VS Code.
    Abre una Carpeta Nueva:
        Ve a Archivo > Abrir Carpeta... y selecciona una carpeta donde quieras guardar tu proyecto.
    Crear un Archivo de Python:
        En la barra lateral izquierda, haz clic derecho y selecciona Nuevo Archivo. Nombra el archivo registro_ventas.py.

## primer acercamiento a la aplicacion
1- una pantalla inicial con un menu: gestion de clientes, gestion de productos, registrar compras, modificar compras, ver compras, cierre del dia, registrar pedidos, modificar pedidos, ver pedidos y salir
2- crear un sistema de carpetas para organizar cada uno de estos modulos por separado
3- crear el esquema de base de datos y relaciones de forma que pueda mantener la integridad de los datos
4- los datos que deseo persistir son:
4.1- gestion de cliente: nombre y telefono
4.2- gestion de productos: nombre, cantidad, peso, precio
4.3- de las compras: fecha, cliente, produto, precio calculado segun cantidad o peso, y si es contado o credito
4.4- registrar pediod, seria como una compra pero la fecha es en el futro
4.5- cierre del dia, suma lo vendido en todo el dia
4.6- ver peidos, muestra listado de pedido para el dia siguiente

## sistema de carpetas
mi_aplicacion/
│
├── base_de_datos/
│   ├── esquema.sql
│   └── gestion_bd.py
├── clientes/
│   ├── gestion_clientes.py
│   └── vistas_clientes.py
├── productos/
│   ├── gestion_productos.py
│   └── vistas_productos.py
├── compras/
│   ├── gestion_compras.py
│   └── vistas_compras.py
├── pedidos/
│   ├── gestion_pedidos.py
│   └── vistas_pedidos.py
├── cierre/
│   ├── gestion_cierre.py
│   └── vistas_cierre.py
├── main.py
└── menu.py

### Escribir el Código

# Paso 1: Crear la Estructura del Proyecto

# Paso 2: Crear el Esquema de la Base de Datos

Vamos a definir el esquema de la base de datos en un archivo SQL llamado esquema.sql.

# Paso 3: Crear la Conexión a la Base de Datos

Vamos a crear un archivo llamado gestion_bd.py para manejar la conexión a la base de datos y la creación de tablas.

# Paso 4: Crear el Menú Principal

Vamos a crear un menú principal en menu.py que permitirá navegar entre los diferentes módulos.

# Paso 5: Crear los Módulos de Gestión

Vamos a crear archivos básicos para cada uno de los módulos. Cada archivo tendrá una función básica para abrir una ventana de Tkinter. Más adelante, puedes expandir estas funciones para agregar la lógica específica de cada módulo.

### Paso 7: Ejecutar el Proyecto

Crear la base de datos y las tablas:

    python base_de_datos/gestion_bd.py

Ejecutar la aplicación:

    python menu.py