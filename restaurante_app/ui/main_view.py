import tkinter as tk
from tkinter import ttk, messagebox


class MainView(tk.Frame):
    def __init__(
        self,
        master,
        servicio,
        usuario_actual,
        al_cerrar_sesion
    ):
        super().__init__(
            master,
            bg="#eef3f8"
        )

        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion

        self.color_principal = "#263238"
        self.color_secundario = "#546e7a"
        self.color_fondo = "#eef3f8"
        self.color_blanco = "white"

        self.configurar_estilos()
        self.crear_interfaz()

    def configurar_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Menu.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=10
        )

    def crear_interfaz(self):
        encabezado = tk.Frame(
            self,
            bg=self.color_principal,
            height=70
        )

        encabezado.pack(
            fill="x"
        )

        titulo = tk.Label(
            encabezado,
            text="Restaurante App",
            bg=self.color_principal,
            fg=self.color_blanco,
            font=("Segoe UI", 20, "bold")
        )

        titulo.pack(
            side="left",
            padx=25,
            pady=18
        )

        usuario = tk.Label(
            encabezado,
            text=f"Usuario: {self.usuario_actual.usuario}",
            bg=self.color_principal,
            fg=self.color_blanco,
            font=("Segoe UI", 10)
        )

        usuario.pack(
            side="right",
            padx=25
        )

        menu = tk.Frame(
            self,
            bg=self.color_fondo
        )

        menu.pack(
            fill="x",
            padx=20,
            pady=20
        )

        ttk.Button(
            menu,
            text="Inicio",
            style="Menu.TButton",
            command=self.mostrar_inicio
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            menu,
            text="Usuarios",
            style="Menu.TButton",
            command=self.mostrar_usuarios
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            menu,
            text="Productos",
            style="Menu.TButton",
            command=self.mostrar_productos
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            menu,
            text="Ventas",
            style="Menu.TButton",
            command=self.mostrar_ventas
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            menu,
            text="Cerrar sesión",
            style="Menu.TButton",
            command=self.al_cerrar_sesion
        ).pack(
            side="right",
            padx=5
        )

        self.contenido = tk.Frame(
            self,
            bg=self.color_fondo
        )

        self.contenido.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.mostrar_inicio()

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Bienvenido al sistema",
            bg=self.color_fondo,
            fg=self.color_principal,
            font=("Segoe UI", 22, "bold")
        )

        titulo.pack(
            pady=40
        )

        descripcion = tk.Label(
            self.contenido,
            text=(
                "Seleccione una opción del menú "
                "para continuar."
            ),
            bg=self.color_fondo,
            fg=self.color_secundario,
            font=("Segoe UI", 12)
        )

        descripcion.pack()

    def mostrar_usuarios(self):
        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Usuarios registrados",
            bg=self.color_fondo,
            fg=self.color_principal,
            font=("Segoe UI", 18, "bold")
        )

        titulo.pack(
            pady=15
        )

        tabla = ttk.Treeview(
            self.contenido,
            columns=(
                "identificador",
                "nombre",
                "usuario"
            ),
            show="headings"
        )

        tabla.heading(
            "identificador",
            text="Identificador"
        )
        tabla.heading(
            "nombre",
            text="Nombre"
        )
        tabla.heading(
            "usuario",
            text="Usuario"
        )

        tabla.column(
            "identificador",
            width=120
        )
        tabla.column(
            "nombre",
            width=200
        )
        tabla.column(
            "usuario",
            width=150
        )

        tabla.pack(
            fill="both",
            expand=True
        )

        for usuario in self.servicio.obtener_usuarios():
            tabla.insert(
                "",
                "end",
                values=(
                    usuario.identificador,
                    usuario.nombre,
                    usuario.usuario
                )
            )

    def mostrar_productos(self):
        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Productos",
            bg=self.color_fondo,
            fg=self.color_principal,
            font=("Segoe UI", 18, "bold")
        )

        titulo.pack(
            pady=15
        )

        tabla = ttk.Treeview(
            self.contenido,
            columns=(
                "codigo",
                "nombre",
                "precio"
            ),
            show="headings"
        )

        tabla.heading(
            "codigo",
            text="Código"
        )
        tabla.heading(
            "nombre",
            text="Nombre"
        )
        tabla.heading(
            "precio",
            text="Precio"
        )

        tabla.pack(
            fill="both",
            expand=True
        )

        for producto in self.servicio.obtener_productos():
            tabla.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    f"${producto.precio:.2f}"
                )
            )

    def mostrar_ventas(self):
        self.limpiar_contenido()

        VentasView(
            self.contenido,
            self.servicio
        ).pack(
            fill="both",
            expand=True
        )


class VentasView(tk.Frame):
    def __init__(
        self,
        master,
        servicio
    ):
        super().__init__(
            master,
            bg="#eef3f8"
        )

        self.servicio = servicio

        self.usuario_var = tk.StringVar()
        self.producto_var = tk.StringVar()

        self.crear_interfaz()
        self.actualizar_tabla()

    def crear_interfaz(self):
        titulo = tk.Label(
            self,
            text="Registro de ventas",
            bg="#eef3f8",
            fg="#263238",
            font=("Segoe UI", 18, "bold")
        )

        titulo.pack(
            pady=10
        )

        formulario = tk.Frame(
            self,
            bg="white",
            padx=20,
            pady=20
        )

        formulario.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            formulario,
            text="Usuario:",
            bg="white",
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        usuarios = [
            usuario.usuario
            for usuario in self.servicio.obtener_usuarios()
        ]

        self.combo_usuario = ttk.Combobox(
            formulario,
            textvariable=self.usuario_var,
            values=usuarios,
            state="readonly",
            width=25
        )

        self.combo_usuario.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            formulario,
            text="Producto:",
            bg="white",
            font=("Segoe UI", 10, "bold")
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        productos = [
            (
                f"{producto.codigo} - "
                f"{producto.nombre}"
            )
            for producto in self.servicio.obtener_productos()
        ]

        self.combo_producto = ttk.Combobox(
            formulario,
            textvariable=self.producto_var,
            values=productos,
            state="readonly",
            width=25
        )

        self.combo_producto.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Button(
            formulario,
            text="Registrar venta",
            command=self.registrar_venta
        ).grid(
            row=0,
            column=2,
            rowspan=2,
            padx=25,
            pady=10
        )

        titulo_tabla = tk.Label(
            self,
            text="Ventas registradas",
            bg="#eef3f8",
            fg="#263238",
            font=("Segoe UI", 13, "bold")
        )

        titulo_tabla.pack(
            pady=(20, 5)
        )

        self.tabla = ttk.Treeview(
            self,
            columns=(
                "codigo",
                "usuario",
                "producto",
                "fecha"
            ),
            show="headings"
        )

        self.tabla.heading(
            "codigo",
            text="Código"
        )
        self.tabla.heading(
            "usuario",
            text="Usuario"
        )
        self.tabla.heading(
            "producto",
            text="Producto"
        )
        self.tabla.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla.column(
            "codigo",
            width=90
        )
        self.tabla.column(
            "usuario",
            width=120
        )
        self.tabla.column(
            "producto",
            width=180
        )
        self.tabla.column(
            "fecha",
            width=150
        )

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def registrar_venta(self):
        usuario = self.usuario_var.get()
        producto_seleccionado = self.producto_var.get()

        if not usuario:
            messagebox.showwarning(
                "Validación",
                "Seleccione un usuario."
            )
            return

        if not producto_seleccionado:
            messagebox.showwarning(
                "Validación",
                "Seleccione un producto."
            )
            return

        codigo_producto = producto_seleccionado.split(
            " - "
        )[0]

        try:
            venta = self.servicio.registrar_venta(
                usuario,
                codigo_producto
            )

            messagebox.showinfo(
                "Venta registrada",
                (
                    f"Venta {venta.codigo} "
                    "registrada correctamente."
                )
            )

            self.usuario_var.set("")
            self.producto_var.set("")

            self.actualizar_tabla()

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for venta in self.servicio.obtener_ventas():
            self.tabla.insert(
                "",
                "end",
                values=(
                    venta.codigo,
                    venta.usuario,
                    venta.producto,
                    venta.fecha
                )
            )