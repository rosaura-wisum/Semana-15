Restaurante App - Semana 15

Datos del estudiante

Nombre: Rosaura Carla Wisum Sharup

Tema

Programación Orientada a Objetos - Manejo de eventos y nueva operación

Descripción

Este proyecto corresponde a la continuación de "restaurante_app", desarrollado durante las semanas anteriores.

Para la Semana 15 se conserva la arquitectura existente y se incorpora una nueva operación de Ventas, manteniendo la separación entre datos, modelos, servicios e interfaz gráfica.

La nueva funcionalidad se adapta al contexto del restaurante y sigue el flujo trabajado en clase mediante botones y callbacks.

Objetivo

Agregar una nueva operación al sistema existente sin reconstruir la arquitectura desarrollada anteriormente.

La operación implementada permite registrar ventas relacionando un usuario, un producto y la fecha de registro.

Nueva operación: Ventas

La sección de ventas permite:

- Seleccionar un usuario mediante un "ttk.Combobox".
- Seleccionar un producto mediante un "ttk.Combobox".
- Registrar una venta mediante un botón.
- Ejecutar la acción utilizando "command=".
- Validar la información desde el servicio.
- Generar automáticamente el código de la venta.
- Registrar automáticamente la fecha y hora.
- Guardar la información en "ventas.json".
- Mostrar las ventas mediante un "ttk.Treeview".

La relación utilizada es:

Usuario + Producto + Fecha = Venta

Flujo de la operación

Botón Registrar venta
        ↓
Callback registrar_venta()
        ↓
RestauranteServicio
        ↓
Validación
        ↓
Creación de Venta
        ↓
ventas.json
        ↓
Actualización del Treeview

Estructura

restaurante_app/
│
├── assets/
│   └── icons/
│       └── sales.png
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md

Modelos

Producto

Representa los productos disponibles en el restaurante.

Usuario

Representa a los usuarios que pueden acceder al sistema.

Venta

Representa una venta registrada y contiene:

- Código.
- Usuario.
- Producto.
- Fecha.

Servicios

ArchivoServicio

Se encarga de leer y escribir la información almacenada en archivos JSON.

RestauranteServicio

Contiene la lógica de la aplicación y las validaciones relacionadas con usuarios, productos y ventas.

La interfaz no contiene la lógica de persistencia de los datos.

Interfaz gráfica

La aplicación utiliza Tkinter.

La interfaz permite:

- Iniciar sesión.
- Consultar usuarios.
- Consultar productos.
- Registrar ventas.
- Consultar las ventas registradas.
- Cerrar sesión.

Los botones utilizan "command=" para ejecutar las acciones correspondientes.

No se utilizan eventos avanzados como "bind()", doble clic, eventos de teclado o eventos de mouse.

Persistencia

Las ventas se almacenan en:

datos/ventas.json

Ejemplo:

[
    {
        "codigo": "V001",
        "usuario": "Carla",
        "producto": "Hamburguesa",
        "fecha": "2026-09-27 19:30"
    }
]

Datos de prueba

Usuarios:

Carla / 1234
Ismael / 1234

Productos existentes:

P001 - Hamburguesa
P002 - Pizza Personal
P003 - Ensalada
P004 - Papas Fritas
P005 - Jugo Natural

Ejecución

Desde la carpeta "restaurante_app":

python main.py

También puede ejecutarse utilizando la instalación de Python configurada en el equipo.

Tecnologías

- Python
- Programación Orientada a Objetos
- Tkinter
- JSON
- pathlib
- datetime
- Git
- GitHub

Conclusión

La Semana 15 mantiene la arquitectura desarrollada anteriormente para "restaurante_app" y agrega la operación de ventas.

La nueva funcionalidad utiliza botones con "command=", callbacks, servicios, persistencia en JSON y un "Treeview" para mostrar los registros, manteniendo la separación de responsabilidades del proyecto.