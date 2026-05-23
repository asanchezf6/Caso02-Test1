from modelo.persona import Persona
from modelo.caja_atencion import CajaAtencion

def separador(titulo: str):
    print(f"\n{'─' * 45}")
    print(f"  {titulo}")
    print('─' * 45)


def main():
    caja = CajaAtencion()

    # 1. Crear 4 personas 
    separador("1. REGISTRO DE PERSONAS EN LA COLA")
    personas = [
        Persona("Ana Torres",    "1001234567"),
        Persona("Luis Gómez",    "0987654321"),
        Persona("María Pérez",   "1112223334"),
        Persona("Carlos Ruiz",   "5556667778"),
    ]
    for persona in personas:
        caja.agregar_persona(persona)

    print(f"\n  Turnos en espera: {caja.turnos_en_espera()}")

    # 2. Atender a las 2 primeras personas
    separador("2. ATENDIENDO A LAS PRIMERAS 2 PERSONAS")
    caja.atender_siguiente()
    caja.atender_siguiente()
    print(f"\n  Turnos restantes: {caja.turnos_en_espera()}")

    # 3. Mostrar el siguiente turno en espera 
    separador("3. PRÓXIMO TURNO EN ESPERA")
    proximo = caja.proximo_turno()
    if proximo:
        print(f"  Siguiente: {proximo}")

    # 4. Vaciar la cola para comprobar el caso borde 
    separador("4. VACIANDO LA COLA (CASO BORDE)")
    while not caja.esta_vacia():
        caja.atender_siguiente()
    caja.atender_siguiente()   # intento cuando ya está vacía

    separador("FIN DE LA SIMULACIÓN")
    print(f"  Cola vacía: {caja.esta_vacia()}\n")

if __name__ == "__main__":
    main()
  