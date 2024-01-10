import json
import os
from commons.utils import *
from commons.menus import menu_modificar_trainers

def load_trainers_json():
    try:
        with open(os.path.join("proyecto-python-master", "data", "trainers.json"), 'r') as archivo_json:        
            lista_trainers = json.load(archivo_json)
            print("La lista de campers ha sido guardada")
            return lista_trainers
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

lista_trainers = load_trainers_json()

contador_trainer = max(trainer['ID'] for trainer in lista_trainers) if lista_trainers else 0

def crear_trainers():
    limpiar_pantalla()
    print("----------- Menú Trainers -----------")
    nombre = solo_letras("Ingrese el Nombre del Trainer: ")
    apellidos = solo_letras("Ingrese Los Apellidos del Trainer: ")
    
    global contador_trainer
    contador_trainer += 1
    trainer = {
        "ID": contador_trainer,
        "NOMBRE_TRAINER": nombre,
        "APELLIDOS_TRAINER": apellidos,
    }
    
    lista_trainers.append(trainer)
    print("Se creó el Trainer con éxito\n")
    guardar_json_trainers()
    

def guardar_json_trainers():
    try:
      with open(os.path.join("proyecto-python-master", "data", "trainers.json"), 'w') as archivo_json:
        json.dump(lista_trainers, archivo_json, indent=2)
        print("La lista de Trainers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")
        


def buscar_trainer():
    # Mostrar la lista de trainers inscritos
    limpiar_pantalla()
    print("----------- Buscar Trainer -----------")
    print("Lista de Trainers Registrados:")
    for trainer in lista_trainers:
        print(f"{trainer['NOMBRE_TRAINER']} {trainer['APELLIDOS_TRAINER']} (ID: {trainer['ID']})")
        


def modificar_trainers():
    limpiar_pantalla()
    print("----------- Modificar Trainer -----------")
    print("Listado de Trainers: ")
    for trainer in lista_trainers:
        print(trainer)
    buscar_id = numero_valido("Ingrese el ID del Trainer que desea Modificar: ")
        
    encontrado = False
    for trainer in lista_trainers:
        if trainer["ID"] == buscar_id:
            print("\nDatos del Trainer:")
            print(f"ID: {trainer['ID']}")
            print(f"Nombre: {trainer['NOMBRE_TRAINER']}")
            print(f"Apellidos: {trainer['APELLIDOS_TRAINER']}")
            encontrado = True
            
            op = menu_modificar_trainers()
            if op==1:
                trainer['NOMBRE_TRAINER'] = solo_letras("Ingrese un nuevo Nombre: ")
                print("Modificacion exitosa")
                guardar_json_trainers()
                break
            elif op==2:
                trainer['APELLIDOS_TRAINER'] = solo_letras("Ingrese nuevos Apellidos: ")
                print("Modificacion exitosa")
                guardar_json_trainers()
                break
            elif op==3:
                print("Regresando...")        
    if not encontrado:
        print(f"No se encontró un Trainer con ID {buscar_id}.")