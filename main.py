"""
Punto de Entrada Principal: Ejecuta la simulación de 10 operaciones completas
(exitosas y fallidas) demostrando la estabilidad y el manejo de excepciones del sistema.
"""
from src.sistema_gestor import SistemaSoftwareFJ
from src.servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from src.excepciones import SoftwareFJError

def ejecutar_simulacion():
    sistema = SistemaSoftwareFJ()
    print("===============================================================")
    print("      SOFTWARE FJ - SISTEMA INTEGRAL DE GESTIÓN DE RESERVAS    ")
    print("===============================================================\n")

    # OPERACIÓN 1: Registro correcto de Cliente 1 (ÉXITO)
    print("--- Operación 1: Registro válido de cliente ---")
    c1 = None
    try:
        c1 = sistema.registrar_cliente("C001", "Carlos Mendoza", "carlos@mail.com", "3001234567")
        print(" -> Éxito:", c1.obtener_resumen())
    except SoftwareFJError as e:
        print(" -> Error capturado:", e)

    # OPERACIÓN 2: Registro inválido de Cliente (FALLO - Correo erróneo)
    print("\n--- Operación 2: Registro inválido de cliente (Correo sin formato) ---")
    try:
        sistema.registrar_cliente("C002", "Ana Gómez", "correo_invalido_sin_arroba", "3119876543")
    except SoftwareFJError as e:
        print(" -> Excepción capturada correctamente:", e)

    # OPERACIÓN 3: Registro de Servicio 1 - Reserva de Sala (ÉXITO)
    print("\n--- Operación 3: Registro de servicio (Reserva de Sala) ---")
    s1 = ReservaSala("S001", "Sala de Conferencias A", tarifa_base=50000.0, capacidad_personas=20)
    sistema.registrar_servicio(s1)
    print(" -> Éxito:", s1.describir_servicio())

    # OPERACIÓN 4: Registro de Servicio 2 - Alquiler de Equipo (ÉXITO)
    print("\n--- Operación 4: Registro de servicio (Alquiler de Equipo) ---")
    s2 = AlquilerEquipo("S002", "Kit de Streaming 4K", tarifa_base=80000.0, incluye_seguro=True)
    sistema.registrar_servicio(s2)
    print(" -> Éxito:", s2.describir_servicio())

    # OPERACIÓN 5: Registro de Servicio 3 - Asesoría (ÉXITO)
    print("\n--- Operación 5: Registro de servicio (Asesoría Especializada) ---")
    s3 = AsesoriaEspecializada("S003", "Arquitectura en la Nube", tarifa_base=120000.0, consultor="Ing. Farfán")
    sistema.registrar_servicio(s3)
    print(" -> Éxito:", s3.describir_servicio())

    # OPERACIÓN 6: Reserva válida (ÉXITO - Sala por 4 horas con 10% descuento)
    print("\n--- Operación 6: Crear Reserva exitosa (Sala Conferencias) ---")
    try:
        r1 = sistema.crear_y_procesar_reserva("R001", c1, s1, duracion=4.0, descuento=0.10)
        print(" -> Reserva Procesada:", r1.obtener_resumen())
    except SoftwareFJError as e:
        print(" -> Error:", e)

    # OPERACIÓN 7: Reserva fallida (FALLO - Duración excedida > 12 horas)
    print("\n--- Operación 7: Intentar reserva con parámetro inválido (> 12h) ---")
    try:
        sistema.crear_y_procesar_reserva("R002", c1, s1, duracion=15.0)
    except SoftwareFJError as e:
        print(" -> Excepción capturada correctamente:", e)

    # OPERACIÓN 8: Registro correcto de Cliente 2 y Reserva de Equipo (ÉXITO)
    print("\n--- Operación 8: Registro Cliente 2 y Reserva de Equipo por 3 días ---")
    try:
        c2 = sistema.registrar_cliente("C003", "Laura Restrepo", "laura@tech.org", "3205554433")
        r2 = sistema.crear_y_procesar_reserva("R003", c2, s2, duracion=3.0)
        print(" -> Reserva Procesada:", r2.obtener_resumen())
    except SoftwareFJError as e:
        print(" -> Error:", e)

    # OPERACIÓN 9: Reserva en servicio no disponible (FALLO)
    print("\n--- Operación 9: Intentar reserva en servicio marcado como no disponible ---")
    s3.disponible = False
    try:
        sistema.crear_y_procesar_reserva("R004", c1, s3, duracion=2.0)
    except SoftwareFJError as e:
        print(" -> Excepción capturada correctamente:", e)

    # OPERACIÓN 10: Cancelación de reserva y reintento de cancelación doble (FALLO CONTROLADO)
    print("\n--- Operación 10: Cancelación de reserva y prueba de error por doble cancelación ---")
    try:
        r1.cancelar()
        print(" -> Estado tras cancelación:", r1.estado)
        r1.cancelar()  # Debe fallar
    except SoftwareFJError as e:
        print(" -> Excepción capturada correctamente en cancelación:", e)

    print("\n===============================================================")
    print(" SIMULACIÓN COMPLETADA EXITOSAMENTE SIN CAÍDAS DEL SISTEMA")
    print(" Revisa el archivo 'logs/sistema_software_fj.log' para auditoría.")
    print("===============================================================")

if __name__ == "__main__":
    ejecutar_simulacion()
