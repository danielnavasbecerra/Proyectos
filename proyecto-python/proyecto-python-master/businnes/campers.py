import json
import os
from commons.utils import *
from commons.menus import menu_modificar_campers
from businnes.rutas import load_rutas_json, listar_rutas

# Load camper data from JSON file
def load_campers_json():
    try:
        with open(os.path.join("proyecto-python-master", "data", "campers.json"), 'r') as archivo_json:        
            # Load camper data from JSON file
            lista_campers = json.load(archivo_json)
            print("La lista de campers ha sido guardada")
            return lista_campers
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# Load the list of campers
lista_campers = load_campers_json()

# Create a new camper
def crear_camper():
    limpiar_pantalla()
    print("----------- Menú Campers -----------")
    numero_id = numero_valido("Ingrese el Numero de Identificacion del Camper: ")
    nombre = solo_letras("Ingrese el Nombre del Camper: ")
    apellidos = solo_letras("Ingrese Los Apellidos del Camper: ")
    direccion = no_vacio("Ingrese la Dirección del Camper: ")
    acudiente = solo_letras("Ingrese el nombre del Acudiente del Camper: ")
    nro_celular = numero_valido("Ingrese el Numero Celular del Camper: ")
    nro_fijo = numero_valido("Ingrese el Numero Fijo del Camper: ")     

    # Create a camper dictionary
    camper = {
        "ID": numero_id,
        "MODULOS": "",
        "NOMBRE": nombre,
        "APELLIDOS": apellidos,
        "DIRECCION": direccion,
        "ACUDIENTE": acudiente,
        "NRO_CELULAR": nro_celular,
        "NRO_FIJO": nro_fijo,
        "ESTADO": "Inscrito".upper(),
        "NOMBRE_RUTA": "",
        "EXPERTO_ENCARGADO": "",
        "FECHA_INICIO": "",
        "FECHA_FINALIZACION": "",
        "SALON_ENTRENAMIENTO": ""
    }
    
    # Add the new camper to the list
    lista_campers.append(camper)
    print("Se creó el camper con éxito\n")
    guardar_json()


# Save the list of campers to the JSON file
def guardar_json():
    try:
      with open(os.path.join("proyecto-python-master", "data", "campers.json"), 'w') as archivo_json:
        # Save the list of campers to the JSON file
        json.dump(lista_campers, archivo_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")
      
# Display the list of campers
def listar_campers():
    limpiar_pantalla()
    print("Listado de campers: ")
    for index, camper in enumerate(lista_campers, start=1):
        print(f"{index}. ID: {camper['ID']}, Nombre: {camper['NOMBRE']} {camper['APELLIDOS']}, Ruta: {camper['NOMBRE_RUTA']}, Estado: {camper['ESTADO']}")


# Modify camper information
def modificar_campers():
    limpiar_pantalla()
    print("----------- Modificar Camper -----------")
    print("Lista Campers:")
    listar_campers()
    buscar_id = numero_valido("Ingrese el Numero de Identificacion del Camper que desee editar: ")
    encontrado = False
    for camper in lista_campers:
        if camper["ID"] == buscar_id:
            print("\nDatos del Camper:")
            print(f"ID: {camper['ID']}")
            print(f"Nombre: {camper['NOMBRE']}")
            print(f"Apellidos: {camper['APELLIDOS']}")
            print(f"Dirección: {camper['DIRECCION']}")
            print(f"Acudiente: {camper['ACUDIENTE']}")
            print(f"Nro Celular: {camper['NRO_CELULAR']}")
            print(f"Nro Fijo: {camper['NRO_FIJO']}")
            print(f"Estado: {camper['ESTADO']}")
            print(f"Nombre Ruta: {camper['NOMBRE_RUTA']}")
            encontrado = True
            
            op = menu_modificar_campers()
            if op==1:
                camper['ID'] = numero_valido("Ingrese un nuevo ID: ")
                print("Modificacion exitosa")
                guardar_json()
                break
            elif op==2:
                camper['ESTADO'] = solo_letras("Ingrese un nuevo ESTADO: ").upper()
                print("Modificacion exitosa")
                guardar_json()
                break
            elif op==3:
                camper['NOMBRE'] = solo_letras("Ingrese un nuevo Nombre: ")
                print("Modificacion exitosa")
                guardar_json()
                break
            elif op==4:
                camper['APELLIDOS'] = solo_letras("Ingrese un nuevo Apellido: ")
                print("Modificacion exitosa")
                guardar_json()
                break
            elif op==5:
                camper['DIRECCION'] = no_vacio("Ingrese una nueva Direccion: ")
                print("Modificacion exitosa")
                guardar_json()
                break
            elif op==6:
                camper['ACUDIENTE'] = solo_letras("Ingrese un nuevo Acudiente: ")
                print("Modificacion exitosa")
                guardar_json()
                break
            elif op==7:
                camper['NRO_CELULAR'] = numero_valido("Ingrese un nuevo Numero Celular: ")
                print("Modificacion exitosa")
                guardar_json()
                break
            elif op==8:
                camper['NRO_FIJO'] = numero_valido("Ingrese un Numero Fijo: ")
                print("Modificacion exitosa")
                guardar_json()
                break
            elif op==9:
                print("Regresando...")        
    if not encontrado:
        print(f"No se encontró un Camper con ID {buscar_id}.")
        



def load_notas_json():
    try:
        with open(os.path.join("proyecto-python-master", "data", "notas.json"), 'r') as archivo_json:        
            lista_campers = json.load(archivo_json)
            print("La lista de campers ha sido guardada")
            return lista_campers
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

lista_notas = load_notas_json()


def registrar_notas():
    # Mostrar la lista de campers inscritos
    limpiar_pantalla()
    print("----------- Registra Notas -----------")
    print("Lista de Campers Inscritos:")
    for camper in lista_campers:
        if camper["ESTADO"] == "INSCRITO":
            print(f"{camper['NOMBRE']} {camper['APELLIDOS']} (ID: {camper['ID']})")

    # Solicitar el ID del camper al que se le registrará la nota
    id_camper = numero_valido("\nIngrese el ID del camper al que desea registrar la nota: ")

    # Buscar el camper en la base de datos
    encontrado = False
    for camper in lista_campers:
        if camper["ID"] == id_camper and camper["ESTADO"] == "INSCRITO":
            encontrado = True
            # Registrar las notas del camper
            while True:
                try:
                    nota_teorica = float(input("Ingrese la Nota teórica del camper: "))
                    nota_practica = float(input("Ingrese la Nota práctica del camper: "))
                    break
                except ValueError:
                    print("Error: Las notas deben ser valores numéricos.")

            # Calcular el promedio de las notas
            promedio = (nota_teorica + nota_practica) / 2

            # Determinar si el camper aprobó la prueba
            # Actualizar la base de datos con las notas y el estado del camper
            if promedio >= 60:
                print(f"\nEl camper {camper['NOMBRE']} {camper['APELLIDOS']} ha aprobado la prueba con un promedio de {promedio}.")
                camper['ESTADO'] = "APROBADO"
            else:
                print(f"\nEl camper {camper['NOMBRE']} {camper['APELLIDOS']} no ha aprobado la prueba con un promedio de {promedio}.")
                camper['ESTADO'] = "NO APROBADO"
            
            guardar_json()
            crear_notas(id_camper, nota_teorica, nota_practica)

   
    if not encontrado:
        print("Camper no está Inscrito o ya esta Aprobado.")



def guardar_json_notas():
    try:
      with open(os.path.join("proyecto-python-master", "data", "notas.json"), 'w') as archivo_json:
        json.dump(lista_notas, archivo_json, indent=2)
        print("La lista de notas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")
        


def crear_notas(id_camper, nota_teorica, nota_practica):
    for camper in lista_campers:
        if camper['ID'] == id_camper:
            camper_notas = {
                "ID": camper['ID'],
                "NOMBRE": camper['NOMBRE'],
                "APELLIDOS": camper['APELLIDOS'],
                "NOTA_TEORICA": nota_teorica,
                "NOTA_PRACTICA": nota_practica,
                "ESTADO": camper['ESTADO'],
            }
            lista_notas.append(camper_notas)
            guardar_json_notas()
            break