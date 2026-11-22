"""
Gestor Principal con Registro de Logs y Memoria Interna (Sin Base de Datos).
"""
import logging
import os
from typing import List
from src.cliente import Cliente
from src.servicios import Servicio
from src.reserva import Reserva
from src.excepciones import SoftwareFJError

class SistemaSoftwareFJ:
    def __init__(self, log_filename: str = "logs/sistema_software_fj.log"):
        dir_name = os.path.dirname(log_filename)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        
        self.logger = logging.getLogger("SoftwareFJ")
        self.logger.setLevel(logging.INFO)
        
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_filename, encoding='utf-8')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        self.clientes: List[Cliente] = []
        self.servicios: List[Servicio] = []
        self.reservas: List[Reserva] = []
        self.logger.info("=== SISTEMA SOFTWARE FJ INICIALIZADO ===")

    def registrar_cliente(self, id_cliente: str, nombre: str, correo: str, telefono: str) -> Cliente:
        try:
            cliente = Cliente(id_cliente, nombre, correo, telefono)
            self.clientes.append(cliente)
            self.logger.info(f"CLIENTE REGISTRADO: {cliente.obtener_resumen()}")
            return cliente
        except SoftwareFJError as e:
            self.logger.error(f"ERROR AL REGISTRAR CLIENTE [{id_cliente}]: {e}")
            raise

    def registrar_servicio(self, servicio: Servicio) -> Servicio:
        try:
            if not servicio:
                raise SoftwareFJError("Intento de registro de servicio nulo.")
            self.servicios.append(servicio)
            self.logger.info(f"SERVICIO REGISTRADO: {servicio.obtener_resumen()}")
            return servicio
        except Exception as e:
            self.logger.error(f"ERROR AL REGISTRAR SERVICIO: {e}")
            raise

    def crear_y_procesar_reserva(self, id_reserva: str, cliente: Cliente, servicio: Servicio, duracion: float, descuento: float = 0.0) -> Reserva:
        try:
            reserva = Reserva(id_reserva, cliente, servicio, duracion)
            reserva.procesar_reserva(descuento=descuento)
            self.reservas.append(reserva)
            self.logger.info(f"RESERVA EXITOSA: {reserva.obtener_resumen()}")
            return reserva
        except SoftwareFJError as e:
            self.logger.error(f"ERROR EN RESERVA [{id_reserva}]: {e}")
            raise
        except Exception as e:
            self.logger.critical(f"ERROR INESPERADO EN RESERVA [{id_reserva}]: {e}", exc_info=True)
            raise
