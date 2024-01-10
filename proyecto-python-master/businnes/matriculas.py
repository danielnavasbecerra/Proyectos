import json
import os
from datetime import datetime, timedelta
from commons.utils import *
from businnes.campers import load_campers_json, listar_campers
from businnes.rutas import load_rutas_json, listar_rutas

lista_campers = load_campers_json()
lista_rutas = load_rutas_json()

def guardar_json():
    try:
      with open(os.path.join("proyecto-python-master", "data", "campers.json"), 'w') as archivo_json:
        json.dump(lista_campers, archivo_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")

def asignar_camper_a_ruta():
    limpiar_pantalla()
    lista_campers = load_campers_json()
    print("----------- Asignar Camper a Ruta -----------")
    
    listar_campers()
    buscar_id = numero_valido("Ingrese el ID del Camper que desea asignar a una ruta: ")
    encontrado = False
    for camper in lista_campers:
        if camper["ID"] == buscar_id:
            print("\nDatos del Camper:")
            print(f"ID: {camper['ID']}")
            print(f"Nombre: {camper['NOMBRE']}")
            print(f"Apellidos: {camper['APELLIDOS']}")
            print(f"Estado: {camper['ESTADO']}")
            print(f"Nombre Ruta: {camper['NOMBRE_RUTA']}")
            
            if camper["ESTADO"] == "APROBADO":
                             
                print("\nSeleccione una ruta para el camper:")
                listar_rutas()

                id_ruta = numero_valido("Ingrese el número de la ruta que desea asignar: ")
                
                if 1 <= id_ruta <= len(lista_rutas):
                    ruta = lista_rutas[id_ruta - 1]
                    
                    if verificar_capacidad_ruta(ruta):
                        camper['ESTADO'] = "ASIGNADO"
                        camper['NOMBRE_RUTA'] = ruta['NOMBRE_RUTA']
                        camper['EXPERTO_ENCARGADO'] = ruta['NOMBRE_TRAINER']
                        camper['SALON_ENTRENAMIENTO'] = ruta['SALON']
                        print(f"Camper {camper['NOMBRE']} {camper['APELLIDOS']} asignado a la ruta '{ruta['NOMBRE_RUTA']}' exitosamente.")
                        guardar_json()
                        print("\nDatos del Camper:")
                        print(f"ID: {camper['ID']}")
                        print(f"Nombre: {camper['NOMBRE']}")
                        print(f"Apellidos: {camper['APELLIDOS']}")
                        print(f"Estado: {camper['ESTADO']}")
                        print(f"Nombre Ruta: {camper['NOMBRE_RUTA']}")
                        print(f"Experto Encargado: {camper['EXPERTO_ENCARGADO']}")
                        print(f"Salon Entrenamiento: {camper['SALON_ENTRENAMIENTO']}")
                        print(f"Fecha Inicio: {camper['FECHA_INICIO']}")
                        print(f"Fecha Finalizacion: {camper['FECHA_FINALIZACION']}")
                        encontrado = True
                    else:
                        print(f"La ruta '{ruta['NOMBRE_RUTA']}' ha alcanzado su capacidad máxima. Asignación fallida.")
                else:
                    print("Número de ruta no válido. Asignación fallida.")
            else:
                print("Verifique si el camper ya esta ASIGNADO o no esta APROBADO")
    if not encontrado:
        print(f"No se encontró un Camper con ID {buscar_id}.")

def verificar_capacidad_ruta(ruta):
    # Verificar si la ruta ha alcanzado la capacidad máxima (33 campers)
    campers_en_ruta = [camper for camper in lista_campers if camper['NOMBRE_RUTA'] == ruta['NOMBRE_RUTA']]
    return len(campers_en_ruta) < 33


def asignar_fechas_matricula():
    limpiar_pantalla()
    print("----------- Asignar Fechas(Inicio-Salida) a Camper -----------")
    
    listar_campers()
    buscar_id = numero_valido("Ingrese el ID del Camper que desea asignar las fechas: ")
    encontrado = False
    for camper in lista_campers:
        if camper["ID"] == buscar_id:
            print("\nDatos del Camper:")
            print(f"ID: {camper['ID']}")
            print(f"Nombre: {camper['NOMBRE']}")
            print(f"Apellidos: {camper['APELLIDOS']}")
            print(f"Estado: {camper['ESTADO']}")
            print(f"Nombre Ruta: {camper['NOMBRE_RUTA']}")
            encontrado = True
            if camper["ESTADO"] == "APROBADO" or camper["ESTADO"] == "ASIGNADO":                
                while True:    
                    try:
                        # Obtener la fecha de inicio
                        fecha_inicio_str = input("Ingrese la fecha de inicio de matrícula para el Camper (YYYY-MM-DD) (Con los giones): ")
                        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')

                        # Calcular la fecha de finalización sumando 1 año a la fecha de inicio
                        fecha_finalizacion = fecha_inicio + timedelta(days=10 * 30)  # Asumiendo 30 días por mes

                        # Asignar las fechas al camper
                        camper['FECHA_INICIO'] = fecha_inicio.strftime('%Y-%m-%d')
                        camper['FECHA_FINALIZACION'] = fecha_finalizacion.strftime('%Y-%m-%d')
                        guardar_json()
                        print("Fechas de matrícula asignadas correctamente.")
                        break
                        
                    except ValueError:
                        print("Error: Formato de fecha incorrecto.")
                
                print("\nDatos del Camper:")
                print(f"ID: {camper['ID']}")
                print(f"Nombre: {camper['NOMBRE']}")
                print(f"Apellidos: {camper['APELLIDOS']}")
                print(f"Estado: {camper['ESTADO']}")
                print(f"Nombre Ruta: {camper['NOMBRE_RUTA']}")
                print(f"Experto Encargado: {camper['EXPERTO_ENCARGADO']}")
                print(f"Salon Entrenamiento: {camper['SALON_ENTRENAMIENTO']}")
                print(f"Fecha Inicio: {camper['FECHA_INICIO']}")
                print(f"Fecha Finalizacion: {camper['FECHA_FINALIZACION']}")
            else:
                print("El camper No esta Aprobado")
    if not encontrado:
        print(f"No se encontró un Camper con ID {buscar_id}.")
        
        
def enlistar_matriculas():
    limpiar_pantalla()
    print("Lista Matriculas: ")
    for index, camper in enumerate(lista_campers, start=1):
        print(f"{index}.  ID: {camper['ID']}")
        print(f"    Nombre: {camper['NOMBRE']}")
        print(f"    Apellidos: {camper['APELLIDOS']}")
        print(f"    Estado: {camper['ESTADO']}")
        print(f"    Nombre Ruta: {camper['NOMBRE_RUTA']}")
        print(f"    Experto Encargado: {camper['EXPERTO_ENCARGADO']}")
        print(f"    Salon Entrenamiento: {camper['SALON_ENTRENAMIENTO']}")
        print(f"    Fecha Inicio: {camper['FECHA_INICIO']}")
        print(f"    Fecha Finalizacion: {camper['FECHA_FINALIZACION']}")
        print("--------------------------------------")