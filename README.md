# Caso de Estudio 02 – Gestión de Turnos de Atención

**Asignatura:** Programación Orientada a Objetos  
**Docente:** Ing. Ernesto Guaman  
**Universidad:** Universidad Estatal de Milagro (UNEMI)

---

## Descripción

Sistema que simula la atención en orden de llegada (FIFO) en una oficina estudiantil.
Cada persona recibe un ticket con número consecutivo y espera en una cola hasta ser atendida.

## Estructura del proyecto

```
caso02_turnos/
├── modelo/
│   ├── persona.py        # Clase Persona (nombre, documento)
│   ├── turno.py          # Clase Turno (persona, número)
│   └── caja_atencion.py  # Clase CajaAtencion (cola FIFO)
├── uml/
│   └── caso02_turnos.puml
└── main.py
```

## Requisitos

- Python 3.10 o superior
- No requiere librerías externas

## Ejecución

```bash
python main.py
```

## Clases principales

| Clase | Responsabilidad |
|-------|----------------|
| `Persona` | Almacena nombre y documento |
| `Turno` | Asocia una Persona a un número consecutivo |
| `CajaAtencion` | Gestiona la cola FIFO de turnos |

## Comportamiento FIFO

- `agregar_persona()` → inserta al **final** de la cola
- `atender_siguiente()` → extrae del **frente** de la cola
