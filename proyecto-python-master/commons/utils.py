import os

def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')    


def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            opcion = int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")
            

def validar_opcion_rutas(opciones_validas, mensaje):
    while True:
        opcion = input(mensaje).strip().lower()
        if opcion in opciones_validas:
            return opcion
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            
            
def numero_valido(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")


def solo_letras(mensaje):
    while True:
        texto = input(mensaje)
        if texto.strip() and texto.replace(" ", "").isalpha():
            return texto
        else:
            print("Por favor, ingrese un valor válido (solo letras).")


def no_vacio(mensaje):
    while True:
        texto = input(mensaje)
        if texto.strip():
            return texto
        else:
            print("No puedes dejar vacío, ingresa caracteres validos.")



def salir():
    print("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⢟⣛⣿⣿⡿⠿⠛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⢫⣵⣾⣿⢟⣫⣵⣾⣿⣿⣿⣿⣿⣿⣾⣝⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⢰⣿⣿⣿⢡⣿⣿⣿⣿⣿⡿⢿⣿⡿⠯⠿⢿⣿⣮⡻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠧⣿⣿⣿⡏⣿⣿⣿⣿⣿⣵⣿⣿⣿⣿⣖⡻⣽⣷⣶⣿⣹⣿⣿⣿⣿⣿⣿
⢟⢻⢸⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⡿⠿⣟⣫⣾⣾⣿⣿⣿⣇⢿⣿⣿⣿⣿⣿
⣁⡉⣭⣭⣟⣋⢸⣿⣿⣿⣿⣿⣿⡷⠿⢿⣿⣹⣿⣿⢲⣶⣶⣮⢸⣿⣿⣿⣿⣿
⣿⣿⣹⣿⣿⣿⡜⣿⣿⣿⣿⣿⣟⣣⣤⣴⣮⣿⣿⣿⣏⣀⣂⣿⣸⣿⣿⣿⣿⣿
⣿⣿⣇⢿⣿⣿⡗⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡻⣿⣿⣿⡇⣿⣿⣿⣿⣿
⣿⣿⣿⣧⢻⣿⡟⣿⣦⣝⢿⣿⣿⣯⡿⣛⣋⠽⠿⣿⠟⣼⣿⣿⣳⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢸⣿⣷⡹⣿⣿⡇⠝⢿⣿⣷⣤⣙⣿⠿⠿⢿⣛⣿⣳⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢸⣿⣿⢸⣬⡻⢢⠸⠡⠩⠻⣿⣿⣿⣭⣽⣿⣿⣣⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠇⣿⣿⣿⣾⣿⣿⣦⡁⠲⣶⣆⢮⡙⡛⢛⣛⣫⣵⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⢟⣼⣿⠟⣥⣾⣿⣿⣿⣿⣰⡺⣭⣄⢴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⣶⣾⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿""")