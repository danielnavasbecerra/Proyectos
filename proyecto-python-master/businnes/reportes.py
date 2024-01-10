import json
import os
from commons.utils import *
from businnes.campers import load_campers_json
from businnes.trainers import load_trainers_json

lista_campers = load_campers_json()
lista_trainers = load_trainers_json()

def listar_campers_inscritos():
    limpiar_pantalla()
    print("Listado de campers con estado Inscrito: ")
    for index, camper in enumerate(lista_campers, start=1):
        if camper['ESTADO'] == "INSCRITO":
            print(f"{index}. ID: {camper['ID']}, Nombre: {camper['NOMBRE']} {camper['APELLIDOS']}, Ruta: {camper['NOMBRE_RUTA']}, Estado: {camper['ESTADO']}")
            
def listar_campers_aprobados():
    limpiar_pantalla()
    print("Listado de campers con estado Aprobado: ")
    for index, camper in enumerate(lista_campers, start=1):
        if camper['ESTADO'] == "APROBADO":
            print(f"{index}. ID: {camper['ID']}, Nombre: {camper['NOMBRE']} {camper['APELLIDOS']}, Ruta: {camper['NOMBRE_RUTA']}, Estado: {camper['ESTADO']}")

def listar_trainers():
    # Mostrar la lista de trainers inscritos
    limpiar_pantalla()
    print("Lista de Trainers Registrados:")
    for index, trainer in enumerate(lista_trainers, start=1):
        print(f"{index}. Nombre:{trainer['NOMBRE_TRAINER']} {trainer['APELLIDOS_TRAINER']} (ID: {trainer['ID']})")