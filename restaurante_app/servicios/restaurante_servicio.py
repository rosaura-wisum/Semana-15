from datetime import datetime

from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta


class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio

        self.usuarios = []
        self.productos = []
        self.ventas = []

        self.cargar_datos()

    def cargar_datos(self):
        datos_usuarios = self.archivo_servicio.leer_json(
            "usuarios.json"
        )

        datos_productos = self.archivo_servicio.leer_json(
            "productos.json"
        )

        datos_ventas = self.archivo_servicio.leer_json(
            "ventas.json"
        )

        self.usuarios = []

        for dato in datos_usuarios:
            contrasena = dato.get(
                "contraseña",
                dato.get("contrasena")
            )

            usuario = Usuario(
                dato["identificador"],
                dato["nombre"],
                dato["usuario"],
                contrasena
            )

            self.usuarios.append(usuario)

        self.productos = []

        for dato in datos_productos:
            producto = Producto(
                dato["codigo"],
                dato["nombre"],
                dato["precio"]
            )

            self.productos.append(producto)

        self.ventas = []

        for dato in datos_ventas:
            venta = Venta(
                dato["codigo"],
                dato["usuario"],
                dato["producto"],
                dato["fecha"]
            )

            self.ventas.append(venta)

    def validar_acceso(self, usuario, contrasena):
        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario == usuario
                and usuario_registrado.contrasena == contrasena
            ):
                return usuario_registrado

        return None

    def obtener_usuarios(self):
        return self.usuarios

    def obtener_productos(self):
        return self.productos

    def obtener_ventas(self):
        return self.ventas

    def registrar_venta(
        self,
        usuario,
        codigo_producto
    ):
        if not usuario:
            raise ValueError(
                "Debe seleccionar un usuario."
            )

        if not codigo_producto:
            raise ValueError(
                "Debe seleccionar un producto."
            )

        usuario_encontrado = None

        for usuario_registrado in self.usuarios:
            if usuario_registrado.usuario == usuario:
                usuario_encontrado = usuario_registrado
                break

        if usuario_encontrado is None:
            raise ValueError(
                "El usuario seleccionado no existe."
            )

        producto_encontrado = None

        for producto in self.productos:
            if producto.codigo == codigo_producto:
                producto_encontrado = producto
                break

        if producto_encontrado is None:
            raise ValueError(
                "El producto seleccionado no existe."
            )

        numero = len(self.ventas) + 1
        codigo_venta = f"V{numero:03d}"

        fecha = datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )

        venta = Venta(
            codigo_venta,
            usuario_encontrado.usuario,
            producto_encontrado.nombre,
            fecha
        )

        self.ventas.append(venta)

        self.guardar_ventas()

        return venta

    def guardar_ventas(self):
        datos = []

        for venta in self.ventas:
            datos.append(
                venta.a_diccionario()
            )

        self.archivo_servicio.escribir_json(
            "ventas.json",
            datos
        )