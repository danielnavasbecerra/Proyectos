from commons.utils import validar_opcion

def menu_principal():
    print("----------- Menú Principal -----------")
    print("1. Campers")
    print("2. Trainers")
    print("3. Matriculas")
    print("4. Rutas")
    print("5. Modulos")
    print("6. Reportes")
    print("7. Salir")       
    op=validar_opcion("Opcion: ",1,7)
    return op


def menu_campers():
    print("----------- Menú Campers -----------")
    print("1. Crear campers")
    print("2. Listar campers")
    print("3. Modificar campers")
    print("4. Registrar Prueba Inicial")
    print("5. Retroceder")
    op=validar_opcion("Opcion: ",1,5)
    return op

def menu_modificar_campers():
    print("\n----------- Menú Modificar Campers -----------")
    print("Seleccione que campo desea Modificar")
    print("1. Número Identificacion")
    print("2. ESTADO")
    print("3. Nombre")
    print("4. Apellidos")
    print("5. Direccion")
    print("6. Acudiente")
    print("7. Nro_Celular")
    print("8. Nro_Fijo")
    print("9. Regresar")
    op=validar_opcion("Opcion: ",1,9)
    return op
    
    
def menu_trainers():
    print("----------- Menú Trainers -----------")
    print("1. Crear trainer")
    print("2. Buscar trainer")
    print("3. Modificar trainer")
    print("4. Retroceder")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_modificar_trainers():
    print("\n----------- Menú Modificar Trainers -----------")
    print("Seleccione que campo desea Modificar")
    print("1. Nombre")
    print("2. Apellidos")
    print("3. Regresar")
    op=validar_opcion("Opcion: ",1,3)
    return op


def menu_matriculas():
    print("----------- Menú Matriculas -----------")
    print("1. Asigna el Camper a Ruta")
    print("2. Asigna el Fechas(Inicio-Final) a Camper")
    print("3. Listar Matriculas")
    print("4. Retroceder")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_rutas():
    print("----------- Menú Rutas -----------")
    print("1. Crear Rutas")
    print("2. Buscar Rutas")
    print("3. Modificar Rutas")
    print("4. Retroceder")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_modulos():
    print("----------- Menú Modulos -----------")
    print("1. Registrar Modulos")
    print("2. Listar Bajo Rendimiento")
    print("3. Retroceder")
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_reportes():
    print("----------- Menú Reportes -----------")
    print("1. Listar campers estado inscrito")
    print("2. Listar campers aprobaron examen")
    print("3. Listar trainers trabajando en campus")
    print("4. Retroceder")
    op=validar_opcion("Opcion: ",1,4)
    return op