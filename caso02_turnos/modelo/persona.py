class Persona:
    """Representa a una persona que solicita atención."""

    def __init__(self, nombre: str, documento: str):
        self.__nombre = nombre
        self.__documento = documento

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def documento(self) -> str:
        return self.__documento

    def __str__(self) -> str:
        return f"{self.__nombre} (Doc: {self.__documento})"
