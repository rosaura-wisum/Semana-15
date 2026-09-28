class Usuario:
    def __init__(
        self,
        identificador,
        nombre,
        usuario,
        contrasena=None,
        **kwargs
    ):
        if contrasena is None:
            contrasena = kwargs.get("contraseña")

        self.identificador = self.validar_texto(
            identificador,
            "El identificador"
        )
        self.nombre = self.validar_texto(
            nombre,
            "El nombre"
        )
        self.usuario = self.validar_texto(
            usuario,
            "El usuario"
        )
        self.contrasena = self.validar_texto(
            contrasena,
            "La contraseña"
        )

    @staticmethod
    def validar_texto(valor, campo):
        if valor is None or not str(valor).strip():
            raise ValueError(
                f"{campo} no puede estar vacío."
            )

        return str(valor).strip()

    def a_diccionario(self):
        return {
            "identificador": self.identificador,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "contraseña": self.contrasena
        }