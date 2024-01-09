import json
import os
from commons.utils import *
from businnes.trainers import load_trainers_json

lista_trainers = load_trainers_json()
def load_rutas_json():
    try:
        with open(os.path.join("proyecto-python-master", "data", "rutas.json"), 'r') as archivo_json:        
            lista_rutas = json.load(archivo_json)
            print("La lista de campers ha sido guardada")
            return lista_rutas
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

lista_rutas = load_rutas_json()

def crear_rutas():
    limpiar_pantalla()
    print("Creación de Ruta de Entrenamiento")

    nombre_ruta = solo_letras("Ingrese el nombre de la ruta: ")

    print("\nSeleccione la información para cada módulo:")
    
    # Fundamentos de Programación
    print("\n1. Fundamentos de Programación:")
    print("   a. Introducción a la algoritmia")
    print("   b. PSeInt")
    print("   c. Python")
    opciones = ['a', 'b', 'c']
    opcion_fundamentos = validar_opcion_rutas(opciones, "Seleccione la opción (a, b o c): ")
    
    # Programación Web
    print("\n2. Programación Web:")
    print("   a. HTML")
    print("   b. CSS")
    print("   c. Bootstrap")
    opciones = ['a', 'b', 'c']
    opcion_web = validar_opcion_rutas(opciones, "Seleccione la opción (a, b o c): ")

    # Programación Formal
    print("\n3. Programación Formal:")
    print("   a. Java")
    print("   b. JavaScript")
    print("   c. C#")
    opciones = ['a', 'b', 'c']
    opcion_formal = validar_opcion_rutas(opciones, "Seleccione la opción (a, b o c): ")

    # Bases de datos
    # SGDB principal y alternativo
    print("\n4. Bases de Datos:")
    print("   Seleccione el SGDB principal y alternativo:")
    print("   a. Mysql (principal) y MongoDb (alternativo)")
    print("   b. MongoDb (principal) y Postgresql (alternativo)")
    print("   c. Postgresql (principal) y Mysql (alternativo)")
    opciones = ['a', 'b', 'c']
    opcion_sgdb = validar_opcion_rutas(opciones, "Seleccione la opción (a, b o c): ")

    # Backend
    print("\n5. Backend:")
    print("   a. NetCore")
    print("   b. Spring Boot")
    print("   c. NodeJS")
    print("   d. Express")
    opciones = ['a', 'b', 'c', 'd']
    opcion_backend = validar_opcion_rutas(opciones, "Seleccione la opcion (a, b, c o d): ")
    
    # Selecciona el salon
    print("\nSeleccione el salon para la Ruta:")
    print("   a. ARTEMIS")
    print("   b. APOLO")
    print("   c. SPUTNIK")
    opciones = ['a', 'b', 'c']
    opcion_salon = validar_opcion_rutas(opciones, "Seleccione la opcion (a, b o c): ")
    
    # Selecciona el horario
    print("\nSeleccione el horario para la Ruta:")
    print("   a. 6:00 AM - 9:30 AM")
    print("   b. 10:00 AM - 1:30 PM")
    print("   c. 2:00 PM - 5:30 PM")
    print("   D. 6:00 PM - 9:30 PM")
    opciones = ['a', 'b', 'c', 'd']
    opcion_horario = validar_opcion_rutas(opciones, "Seleccione la opcion (a, b, c o d): ")
    
    # Mapeo de opciones seleccionadas a la información completa
    mapeo_fundamentos = {
        'a': 'Introducción a la algoritmia',
        'b': 'PSeInt',
        'c': 'Python',
    }
    mapeo_web = {
        'a': 'HTML',
        'b': 'CSS',
        'c': 'Bootstrap',
    }
    mapeo_formal = {
        'a': 'Java',
        'b': 'JavaScript',
        'c': 'C#',
    }
    mapeo_bases_datos = {
        'a': ('Mysql', 'MongoDb'),
        'b': ('MongoDb', 'Postgresql'),
        'c': ('Postgresql', 'Mysql'),
    }
    mapeo_backend = {
        'a': 'NetCore',
        'b': 'Spring Boot',
        'c': 'NodeJS',
        'd': 'Express',
    }
    mapeo_salones = {
        'a': 'ARTEMIS',
        'b': 'APOLO',
        'c': 'SPUTNIK',
    }
    mapeo_horario = {
        'a': '6:00 AM - 9:30 AM',
        'b': '10:00 AM - 1:30 PM',
        'c': '2:00 PM - 5:30 PM',
        'd': '6:00 PM - 9:30 PM',
    }
    
    print("\nLista de Profesores Disponibles:")
    
    for trainer in lista_trainers:
        print(f"ID: {trainer['ID']}, Nombre: {trainer['NOMBRE_TRAINER']} {trainer['APELLIDOS_TRAINER']}")

    id_profesor = numero_valido("Ingrese el ID del Profesor para la ruta seleccionada: ")
    nombre_profesor = obtener_nombre_profesor_por_id(id_profesor)

    # Crear diccionario para la nueva ruta
    ruta = {
        "NOMBRE_RUTA": nombre_ruta,
        "NOMBRE_TRAINER": nombre_profesor,
        "Fundamentos de Programacion": mapeo_fundamentos[opcion_fundamentos],
        "Programacion Web": mapeo_web[opcion_web],
        "Programacion Formal": mapeo_formal[opcion_formal],
        "SGDB Principal": mapeo_bases_datos[opcion_sgdb][0],
        "SGDB Alternativo": mapeo_bases_datos[opcion_sgdb][1],
        "Backend": mapeo_backend[opcion_backend],
        "SALON": mapeo_salones[opcion_salon],
        "HORARIO": mapeo_horario[opcion_horario]
    }

    # Agregar la nueva ruta a la lista de rutas
    lista_rutas.append(ruta)
    print(f"¡Ruta '{nombre_ruta}' creada exitosamente!\n")
    guardar_json_rutas()

# Guardar la base de datos actualizada
def guardar_json_rutas():
    try:
      with open(os.path.join("proyecto-python-master", "data", "rutas.json"), 'w') as archivo_json:
        json.dump(lista_rutas, archivo_json, indent=2)
        print("La lista de rutas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")
        

def obtener_nombre_profesor_por_id(id_profesor):
    try:
        with open(os.path.join("proyecto-python-master", "data", "trainers.json"), 'r') as archivo_json:
            lista_trainers = json.load(archivo_json)

        for trainer in lista_trainers:
            if trainer["ID"] == id_profesor:
                return trainer["NOMBRE_TRAINER"], trainer["APELLIDOS_TRAINER"]
    except Exception as e:
        print(f"Error al obtener el nombre del profesor: {e}")
    return None


def listar_rutas():
    limpiar_pantalla()
    print("----------- Listado de Rutas -----------")
    for index, ruta in enumerate(lista_rutas, start=1):
        print(f"{index}. Nombre Ruta: {ruta['NOMBRE_RUTA']}")
        print(f"   - Fundamentos de Programación: {ruta['Fundamentos de Programacion']}")
        print(f"   - Programación Web: {ruta['Programacion Web']}")
        print(f"   - Programación Formal: {ruta['Programacion Formal']}")
        print(f"   - SGDB Principal: {ruta['SGDB Principal']}")
        print(f"   - SGDB Alternativo: {ruta['SGDB Alternativo']}")
        print(f"   - Backend: {ruta['Backend']}")
        print(f"   - Profesor: {ruta['NOMBRE_TRAINER']}")
        print(f"   - Salón: {ruta['SALON']}")
        print(f"   - Horario: {ruta['HORARIO']}")
        print("--------------------------------------")
        

def modificar_rutas():
    limpiar_pantalla()
    print("----------- Modificar Ruta -----------")
    listar_rutas()

    index_ruta = numero_valido("Ingrese el número de la ruta que desea modificar: ")

    if 1 <= index_ruta <= len(lista_rutas):
        ruta = lista_rutas[index_ruta - 1]

        print(f"\nDatos de la Ruta {ruta['NOMBRE_RUTA']}:")
        print(f"1. Nombre: {ruta['NOMBRE_RUTA']}")
        print(f"2. Profesor: {ruta['NOMBRE_TRAINER']}")
        print(f"3. Salon: {ruta['SALON']}")
        print(f"4. Horario: {ruta['HORARIO']}")

        opcion = numero_valido("Seleccione el número del campo que desea modificar (1-4): ")

        if opcion == 1:
            nuevo_nombre = solo_letras("Ingrese el nuevo nombre de la ruta: ")
            ruta['NOMBRE_RUTA'] = nuevo_nombre
        elif opcion == 2:
            print("\nLista de Profesores Disponibles:")
            for trainer in lista_trainers:
                print(f"ID: {trainer['ID']}, Nombre: {trainer['NOMBRE_TRAINER']} {trainer['APELLIDOS_TRAINER']}")
            nuevo_profesor = obtener_nombre_profesor_por_id(numero_valido("Ingrese el nuevo ID del profesor: "))
            ruta['NOMBRE_TRAINER'] = nuevo_profesor
        elif opcion == 3:
            # Selecciona el salon
            print("\nSeleccione el salon para la Ruta:")
            print("   a. ARTEMIS")
            print("   b. APOLO")
            print("   c. SPUTNIK")
            mapeo_salones = {
            'a': 'ARTEMIS',
            'b': 'APOLO',
            'c': 'SPUTNIK',
            }
            opciones = ['a', 'b', 'c']
            opcion_salon = validar_opcion_rutas(opciones, "Seleccione la opcion (a, b o c): ")
            ruta['SALON'] = mapeo_salones[opcion_salon]
        elif opcion == 4:
            # Selecciona el horario
            print("\nSeleccione el horario para la Ruta:")
            print("   a. 6:00 AM - 9:30 AM")
            print("   b. 10:00 AM - 1:30 PM")
            print("   c. 2:00 PM - 5:30 PM")
            print("   D. 6:00 PM - 9:30 PM")
            mapeo_horario = {
            'a': '6:00 AM - 9:30 AM',
            'b': '10:00 AM - 1:30 PM',
            'c': '2:00 PM - 5:30 PM',
            'd': '6:00 PM - 9:30 PM',
            }
            opciones = ['a', 'b', 'c', 'd']
            opcion_horario = validar_opcion_rutas(opciones, "Seleccione la opcion (a, b, c o d): ")
            ruta['HORARIO'] = mapeo_horario[opcion_horario]
        else:
            print("Opción no válida. Regresando al menú principal.")

        guardar_json_rutas()
        print("Modificación exitosa.")
    else:
        print("Número de ruta no válido. Regresando al menú principal.")