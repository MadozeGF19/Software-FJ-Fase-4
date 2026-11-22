"""
Módulo de Excepciones Personalizadas para Software FJ.
"""

class SoftwareFJError(Exception):
    """Excepción base para el sistema Software FJ."""
    pass

class ClienteInvalidoError(SoftwareFJError):
    """Se lanza cuando los datos del cliente no cumplen con las validaciones."""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando un servicio no está disponible o los parámetros son inválidos."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando ocurre un error al procesar o confirmar una reserva."""
    pass
