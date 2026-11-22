# UNAD - Curso Programación (213023) - Componente Práctico (Fase 4)

## Solución Software FJ - Gestión de Reservas POO

Este repositorio contiene la solución completa para la **Fase 4 (Prácticas simuladas)** de la empresa **Software FJ**, desarrollada aplicando los principios de la Programación Orientada a Objetos (POO) en Python y un robusto sistema de gestión de excepciones y registros de auditoría (logs).

---

## Arquitectura del Proyecto

```text
UNAD-SoftwareFJ-Fase4/
├── logs/
│   └── sistema_software_fj.log     # Registro automático de eventos y errores
├── src/
│   ├── __init__.py                 # Inicialización del paquete
│   ├── excepciones.py              # Excepciones personalizadas del dominio
│   ├── entidad.py                  # Clase abstracta base EntidadBase
│   ├── cliente.py                  # Entidad Cliente con encapsulamiento y regex
│   ├── servicios.py                # Jerarquía POO de servicios (ReservaSala, AlquilerEquipo, Asesoria)
│   ├── reserva.py                  # Gestión de reservas y cálculo de costos con polimorfismo
│   └── sistema_gestor.py           # Controlador principal y logger
├── main.py                         # Simulación de 10 operaciones de prueba
├── README.md                       # Documentación del proyecto
└── .gitignore                      # Configuración de exclusión para Git
```

---

## Requerimientos Cumplidos

1. **Abstracción e Herencia**: Clase base abstracta `EntidadBase` y clase abstracta `Servicio` de la cual heredan `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada`.
2. **Encapsulamiento**: Propiedades privadas/protegidas con getters y setters validados (e.g., validación de correo mediante expresiones regulares y validación de teléfono).
3. **Polimorfismo y Sobrecarga**: Implementación diferenciada del método `calcular_costo()` en cada servicio derivado con parámetros opcionales de descuento e impuestos.
4. **Manejo Completo de Excepciones**:
   - Excepciones personalizadas (`SoftwareFJError`, `ClienteInvalidoError`, `ServicioNoDisponibleError`, `ReservaInvalidaError`).
   - Uso de bloques `try / except / else / finally`.
   - Encadenamiento de excepciones con `raise ... from ...`.
5. **Auditoría y Logging**: Registro automático en `logs/sistema_software_fj.log` sin interrumpir la ejecución del programa.
6. **Tolerancia a Fallos**: Ejecución de 10 operaciones simuladas (exitosas y fallidas).

---

## Instrucciones de Ejecución

Para ejecutar la simulación de las 10 operaciones en consola:

```bash
python main.py
```

---

## 👥 Equipo de Trabajo
- **Curso**: Programación (213023)
- **Grupo**: 558
- **Universidad**: Universidad Nacional Abierta y a Distancia (UNAD)
- **Escuela**: ECBTI
