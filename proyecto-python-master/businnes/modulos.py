import json
import os
from commons.utils import *
from businnes.campers import load_campers_json

lista_campers = load_campers_json()

def load_modulos_json():
    try:
        with open(os.path.join("proyecto-python-master", "data", "modulos.json"), 'r') as archivo_json:        
            lista_modulos = json.load(archivo_json)
            print("La lista de campers ha sido guardada")
            return lista_modulos
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


lista_modulos = load_modulos_json()

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


def guardar_json_modulos():
    try:
      with open(os.path.join("proyecto-python-master", "data", "modulos.json"), 'w') as archivo_json:
        json.dump(lista_modulos, archivo_json, indent=2)
        print("La lista de notas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")


def registrar_modulos():
    # Mostrar la lista de campers aprobados
    limpiar_pantalla()
    print("----------- Registra Modulos -----------")
    print("Lista de Campers Aprobados:")
    for camper in lista_campers:
        if camper["ESTADO"] == "APROBADO" or camper["ESTADO"] == "ASIGNADO":
            print(f"{camper['NOMBRE']} {camper['APELLIDOS']} (ID: {camper['ID']})")

    # Solicitar el ID del camper al que se le registrará la nota
    id_camper = numero_valido("Ingrese el ID del camper al que desea registrar la nota: ")

    # Buscar el camper en la base de datos
    encontrado = False
    for camper in lista_campers:
        if camper["ID"] == id_camper and (camper["ESTADO"] == "APROBADO" or camper["ESTADO"] == "ASIGNADO"):
            encontrado = True
            # Registrar las notas del camper
            while True:
                try:
                    nota_teorica = float(input("Ingrese la Nota teórica del camper: "))
                    nota_practica = float(input("Ingrese la Nota práctica del camper: "))
                    nota_quices = float(input("Ingrese la Nota Promediada de los quices del camper: "))
                    calcular_nota_final(nota_teorica, nota_practica, nota_quices)
                    break
                except ValueError:
                    print("Error: Las notas deben ser valores numéricos.")

            nota_final = calcular_nota_final(nota_teorica, nota_practica, nota_quices)

            # Imprimir la nota final
            print(f"Nota Final: {nota_final}")

            # Verificar si el modulo es aprobado
            if nota_final >= 60:
                print(f"¡Módulo Aprobado! El camper {camper['NOMBRE']} {camper['APELLIDOS']} aprobo el modulo.")
                camper['MODULOS'] = "APROBADO"
                modulo = "APROBADO"
            else:
                print("Módulo No Aprobado. Es necesario repetir el módulo.")
                modulo = "RENDIMIENTO BAJO"
                camper['MODULOS'] = "RENDIMIENTO BAJO"
            
            guardar_json()
            crear_modulos(id_camper, nota_teorica, nota_practica, nota_quices, nota_final, modulo)

    if not encontrado:
        print("Camper no está Inscrito o no esta Aprobado.")


def crear_modulos(id_camper, nota_teorica, nota_practica, nota_quices, nota_final, modulo):
    for camper in lista_campers:
        if camper['ID'] == id_camper:
            camper_modulos = {
                "ID": camper['ID'],
                "NOMBRE": camper['NOMBRE'],
                "APELLIDOS": camper['APELLIDOS'],
                "NOTA_TEORICA": nota_teorica,
                "NOTA_PRACTICA": nota_practica,
                "NOTA_QUICES": nota_quices,
                "NOTA_FINAL": nota_final,
                "MODULOS": modulo
            }
            lista_modulos.append(camper_modulos)
            guardar_json_modulos()
            break


def calcular_nota_final(nota_teorica, nota_practica, nota_quices):
    # Validar que las notas estén en el rango correcto (0-100)
    if not (0 <= nota_teorica <= 100) or not (0 <= nota_practica <= 100) or not (0 <= nota_quices <= 100):
        raise ValueError("Las notas deben estar en el rango de 0 a 100.")

    # Calcular la nota final con los pesos dados
    peso_teorico = 0.3
    peso_practico = 0.6
    peso_quices = 0.1

    nota_final = (nota_teorica * peso_teorico) + (nota_practica * peso_practico) + (nota_quices * peso_quices)
    return nota_final


def enlistar_modulos_bajo_rendimiento():
    limpiar_pantalla()
    encontrado = False
    for index, camper_modulos in enumerate(lista_modulos, start=1):
        if camper_modulos['MODULOS'] == "RENDIMIENTO BAJO":
            print("Lista Modulos Bajo Rendimiento: ")
            encontrado = True
            print(f"{index}.  ID: {camper_modulos['ID']}")
            print(f"    Nombre: {camper_modulos['NOMBRE']}")
            print(f"    Apellidos: {camper_modulos['APELLIDOS']}")
            print(f"    Nota Teorica: {camper_modulos['NOTA_TEORICA']}")
            print(f"    Nota Practica: {camper_modulos['NOTA_PRACTICA']}")
            print(f"    Nota Quices: {camper_modulos['NOTA_QUICES']}")
            print(f"    NOTA FINAL(promediado): {camper_modulos['NOTA_FINAL']}")
            print(f"    Modulo: {camper_modulos['MODULOS']}")
            print("--------------------------------------")
    if not encontrado:
        print("No Hay camper con Bajo Rendimiento")