"""
Clase Cliente con encapsulamiento y validaciones de datos personales.
"""
import re
from src.entidad import EntidadBase
from src.excepciones import ClienteInvalidoError

class Cliente(EntidadBase):
    def __init__(self, id_cliente: str, nombre: str, correo: str, telefono: str):
        super().__init__(id_cliente)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or len(valor.strip()) < 3:
            raise ClienteInvalidoError("El nombre del cliente debe tener al menos 3 caracteres.")
        self._nombre = valor.strip()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron, valor):
            raise ClienteInvalidoError(f"El correo '{valor}' no tiene un formato válido.")
        self._correo = valor.strip()

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):
        if not valor.isdigit() or len(valor) < 7:
            raise ClienteInvalidoError("El teléfono debe ser numérico y contener al menos 7 dígitos.")
        self._telefono = valor.strip()

    def obtener_resumen(self) -> str:
        return f"Cliente [{self.id_entidad}]: {self.nombre} ({self.correo})"
