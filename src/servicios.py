"""
Jerarquía de Servicios con Polimorfismo y Sobrecarga de Métodos.
"""
from abc import abstractmethod
from src.entidad import EntidadBase
from src.excepciones import ServicioNoDisponibleError

class Servicio(EntidadBase):
    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float):
        super().__init__(id_servicio)
        self._nombre = nombre
        self._tarifa_base = tarifa_base
        self._disponible = True

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def tarifa_base(self) -> float:
        return self._tarifa_base

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, estado: bool):
        self._disponible = estado

    @abstractmethod
    def calcular_costo(self, duracion: float, descuento: float = 0.0, impuesto: float = 0.19) -> float:
        """Calcula el costo del servicio aplicando polimorfismo y sobrecarga simulada."""
        pass

    @abstractmethod
    def describir_servicio(self) -> str:
        pass

    @abstractmethod
    def validar_parametros(self, duracion: float) -> bool:
        pass

    def obtener_resumen(self) -> str:
        return f"Servicio [{self.id_entidad}]: {self.nombre} - Base: ${self.tarifa_base:.2f}"


class ReservaSala(Servicio):
    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, capacidad_personas: int):
        super().__init__(id_servicio, nombre, tarifa_base)
        self.capacidad_personas = capacidad_personas

    def validar_parametros(self, duracion: float) -> bool:
        if duracion <= 0 or duracion > 12:
            raise ServicioNoDisponibleError("La reserva de sala debe ser entre 1 y 12 horas.")
        return True

    def calcular_costo(self, duracion: float, descuento: float = 0.0, impuesto: float = 0.19) -> float:
        self.validar_parametros(duracion)
        subtotal = self.tarifa_base * duracion
        subtotal_con_descuento = subtotal * (1 - descuento)
        total = subtotal_con_descuento * (1 + impuesto)
        return round(total, 2)

    def describir_servicio(self) -> str:
        return f"Reserva de Sala '{self.nombre}' (Capacidad: {self.capacidad_personas} personas)."


class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, incluye_seguro: bool = True):
        super().__init__(id_servicio, nombre, tarifa_base)
        self.incluye_seguro = incluye_seguro

    def validar_parametros(self, duracion: float) -> bool:
        if duracion < 1:
            raise ServicioNoDisponibleError("El alquiler de equipo requiere al menos 1 día de duración.")
        return True

    def calcular_costo(self, duracion: float, descuento: float = 0.0, impuesto: float = 0.19) -> float:
        self.validar_parametros(duracion)
        costo_diario = self.tarifa_base + (15000 if self.incluye_seguro else 0)
        subtotal = costo_diario * duracion
        total = subtotal * (1 - descuento) * (1 + impuesto)
        return round(total, 2)

    def describir_servicio(self) -> str:
        seguro_str = "con seguro" if self.incluye_seguro else "sin seguro"
        return f"Alquiler de Equipo '{self.nombre}' ({seguro_str})."


class AsesoriaEspecializada(Servicio):
    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, consultor: str):
        super().__init__(id_servicio, nombre, tarifa_base)
        self.consultor = consultor

    def validar_parametros(self, duracion: float) -> bool:
        if duracion < 0.5:
            raise ServicioNoDisponibleError("La asesoría mínima es de 0.5 horas (30 mins).")
        return True

    def calcular_costo(self, duracion: float, descuento: float = 0.0, impuesto: float = 0.19) -> float:
        self.validar_parametros(duracion)
        subtotal = self.tarifa_base * duracion
        total = subtotal * (1 - descuento) * (1 + impuesto)
        return round(total, 2)

    def describir_servicio(self) -> str:
        return f"Asesoría Especializada con el consultor {self.consultor}."
