from modelo.persona import Persona
from modelo.turno import Turno


class CajaAtencion:
    """
    Gestiona la cola de turnos de atención.
    Opera bajo el principio FIFO: el primero en llegar es el primero en ser atendido.
    """

    def __init__(self):
        self.__turnos: list[Turno] = []
        self.__contador: int = 0

    def agregar_persona(self, persona: Persona) -> Turno:
        """Registra la llegada de una persona y le asigna un turno consecutivo."""
        self.__contador += 1
        turno = Turno(persona, self.__contador)
        self.__turnos.append(turno)
        print(f"  ✔ Turno asignado: {turno}")
        return turno

    def atender_siguiente(self) -> Turno | None:
        """
        Atiende al siguiente turno en la cola (FIFO).
        Retorna el turno atendido, o None si la cola está vacía.
        """
        if self.esta_vacia():
            print("  ⚠ No hay personas en espera.")
            return None
        turno = self.__turnos.pop(0)
        print(f"  ★ Atendiendo: {turno}")
        return turno

    def esta_vacia(self) -> bool:
        """Indica si no hay turnos pendientes en la cola."""
        return len(self.__turnos) == 0

    def proximo_turno(self) -> Turno | None:
        """Consulta el siguiente turno sin extraerlo de la cola."""
        if self.esta_vacia():
            return None
        return self.__turnos[0]

    def turnos_en_espera(self) -> int:
        """Retorna la cantidad de turnos pendientes."""
        return len(self.__turnos)
