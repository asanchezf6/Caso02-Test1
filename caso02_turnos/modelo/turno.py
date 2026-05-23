from modelo.persona import Persona


class Turno:
    """Representa un turno asignado a una persona al llegar a la caja."""

    def __init__(self, persona: Persona, numero: int):
        self.__persona = persona
        self.__numero = numero

    @property
    def persona(self) -> Persona:
        return self.__persona

    @property
    def numero(self) -> int:
        return self.__numero

    def __str__(self) -> str:
        return f"Turno #{self.__numero:03d} → {self.__persona}"
