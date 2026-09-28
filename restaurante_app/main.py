import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import (
    ArchivoServicio
)

from servicios.restaurante_servicio import (
    RestauranteServicio
)

from ui.login_view import LoginView
from ui.main_view import MainView


class AplicacionRestaurante:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title(
            "Restaurante - Tkinter"
        )

        self.root.geometry(
            "850x620"
        )

        self.root.minsize(
            700,
            550
        )

        ruta_base = (
            Path(__file__).resolve().parent
        )

        archivo_servicio = (
            ArchivoServicio(
                ruta_base / "datos"
            )
        )

        self.servicio = (
            RestauranteServicio(
                archivo_servicio
            )
        )

        self.usuario_actual = None
        self.vista_actual = None

        self.mostrar_login()

    def cambiar_vista(self, vista):
        if self.vista_actual is not None:
            self.vista_actual.destroy()

        self.vista_actual = vista

        self.vista_actual.pack(
            fill="both",
            expand=True
        )

    def mostrar_login(self):
        vista = LoginView(
            self.root,
            self.servicio,
            self.iniciar_sesion
        )

        self.cambiar_vista(vista)

    def iniciar_sesion(self, usuario):
        self.usuario_actual = usuario

        vista = MainView(
            self.root,
            self.servicio,
            usuario,
            self.cerrar_sesion
        )

        self.cambiar_vista(vista)

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.mostrar_login()

    def ejecutar(self):
        self.root.mainloop()


if __name__ == "__main__":
    aplicacion = AplicacionRestaurante()
    aplicacion.ejecutar()