class Venta:
    def __init__(
        self,
        codigo,
        usuario,
        producto,
        fecha
    ):
        self.codigo = self.validar_texto(
            codigo,
            "El código"
        )
        self.usuario = self.validar_texto(
            usuario,
            "El usuario"
        )
        self.producto = self.validar_texto(
            producto,
            "El producto"
        )
        self.fecha = self.validar_texto(
            fecha,
            "La fecha"
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
            "codigo": self.codigo,
            "usuario": self.usuario,
            "producto": self.producto,
            "fecha": self.fecha
        }