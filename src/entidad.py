"""
Clase Abstracta Base para Entidades del Sistema.
"""
from abc import ABC, abstractmethod

class EntidadBase(ABC):
    def __init__(self, id_entidad: str):
        self._id_entidad = id_entidad

    @property
    def id_entidad(self) -> str:
        return self._id_entidad

    @abstractmethod
    def obtener_resumen(self) -> str:
        """Devuelve una representación textual resumida de la entidad."""
        pass
