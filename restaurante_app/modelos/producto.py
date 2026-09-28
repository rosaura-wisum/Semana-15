class Producto:
    def __init__(
        self,
        codigo,
        nombre,
        precio
    ):
        self.codigo = self.validar_texto(
            codigo,
            "El código"
        )

        self.nombre = self.validar_texto(
            nombre,
            "El nombre"
        )

        try:
            self.precio = float(precio)
        except (TypeError, ValueError):
            raise ValueError(
                "El precio debe ser numérico."
            )

        if self.precio < 0:
            raise ValueError(
                "El precio no puede ser negativo."
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
            "nombre": self.nombre,
            "precio": self.precio
        }