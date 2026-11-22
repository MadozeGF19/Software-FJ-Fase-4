"""
Clase Reserva que integra Cliente y Servicio con control de estado y excepciones.
"""
from src.entidad import EntidadBase
from src.cliente import Cliente
from src.servicios import Servicio
from src.excepciones import ReservaInvalidaError, ServicioNoDisponibleError

class Reserva(EntidadBase):
    def __init__(self, id_reserva: str, cliente: Cliente, servicio: Servicio, duracion: float):
        super().__init__(id_reserva)
        if not cliente:
            raise ReservaInvalidaError("La reserva debe tener un cliente válido asignado.")
        if not servicio or not servicio.disponible:
            raise ServicioNoDisponibleError("El servicio solicitado no existe o no está disponible.")
        
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "PENDIENTE"
        self.costo_total = 0.0

    def procesar_reserva(self, descuento: float = 0.0) -> float:
        """Procesamiento con bloques try/except/else/finally."""
        try:
            self.costo_total = self.servicio.calcular_costo(self.duracion, descuento=descuento)
        except Exception as e:
            self.estado = "RECHAZADA"
            raise ReservaInvalidaError(f"Error procesando la reserva {self.id_entidad}: {e}") from e
        else:
            self.estado = "CONFIRMADA"
            return self.costo_total
        finally:
            # Mantener consistencia de ejecución
            pass

    def cancelar(self):
        if self.estado == "CANCELADA":
            raise ReservaInvalidaError("La reserva ya se encuentra cancelada.")
        self.estado = "CANCELADA"

    def obtener_resumen(self) -> str:
        return f"Reserva [{self.id_entidad}] | Cliente: {self.cliente.nombre} | Servicio: {self.servicio.nombre} | Estado: {self.estado} | Total: ${self.costo_total:,.2f}"
