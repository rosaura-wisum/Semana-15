import tkinter as tk
from tkinter import ttk, messagebox


class LoginView(tk.Frame):
    def __init__(
        self,
        master,
        servicio,
        al_iniciar_sesion
    ):
        super().__init__(
            master,
            bg="#eef3f8"
        )

        self.servicio = servicio
        self.al_iniciar_sesion = (
            al_iniciar_sesion
        )

        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Login.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=10
        )

        contenedor = tk.Frame(
            self,
            bg="white",
            padx=40,
            pady=35
        )

        contenedor.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        tk.Label(
            contenedor,
            text="Restaurante App",
            font=("Segoe UI", 20, "bold"),
            bg="white",
            fg="#263238"
        ).pack(
            pady=(0, 8)
        )

        tk.Label(
            contenedor,
            text="Inicio de sesión",
            font=("Segoe UI", 11),
            bg="white",
            fg="#546e7a"
        ).pack(
            pady=(0, 20)
        )

        tk.Label(
            contenedor,
            text="Usuario",
            font=("Segoe UI", 10, "bold"),
            bg="white"
        ).pack(
            anchor="w"
        )

        self.entrada_usuario = ttk.Entry(
            contenedor,
            width=32
        )

        self.entrada_usuario.pack(
            pady=(5, 12)
        )

        tk.Label(
            contenedor,
            text="Contraseña",
            font=("Segoe UI", 10, "bold"),
            bg="white"
        ).pack(
            anchor="w"
        )

        self.entrada_contrasena = ttk.Entry(
            contenedor,
            width=32,
            show="*"
        )

        self.entrada_contrasena.pack(
            pady=(5, 20)
        )

        ttk.Button(
            contenedor,
            text="Ingresar",
            style="Login.TButton",
            command=self.iniciar_sesion
        ).pack(
            fill="x"
        )

        self.entrada_usuario.focus()

    def iniciar_sesion(self):
        usuario = (
            self.entrada_usuario
            .get()
            .strip()
        )

        contrasena = (
            self.entrada_contrasena
            .get()
            .strip()
        )

        if not usuario or not contrasena:
            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese usuario y contraseña."
            )
            return

        usuario_actual = (
            self.servicio.validar_acceso(
                usuario,
                contrasena
            )
        )

        if usuario_actual is None:
            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos."
            )
            return

        self.al_iniciar_sesion(
            usuario_actual
        )