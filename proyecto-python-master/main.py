from commons.utils import limpiar_pantalla,salir
from commons.menus import menu_principal,menu_trainers,menu_campers,menu_matriculas,menu_rutas,menu_reportes,menu_modulos
from businnes.campers import crear_camper,listar_campers,modificar_campers,registrar_notas
from businnes.trainers import crear_trainers,buscar_trainer,modificar_trainers
from businnes.rutas import crear_rutas,listar_rutas,modificar_rutas
from businnes.matriculas import asignar_camper_a_ruta, asignar_fechas_matricula, enlistar_matriculas
from businnes.modulos import registrar_modulos, enlistar_modulos_bajo_rendimiento
from businnes.reportes import listar_campers_inscritos, listar_campers_aprobados, listar_trainers
# Hello guys, today I am going to show you the code of my project.
# funtions
def campers():      
    limpiar_pantalla()
    op=menu_campers()
    if op==1:
       crear_camper()
       input("Clic tecla Enter [continuar]: ")
       limpiar_pantalla()
       campers()
    elif op==2:
       listar_campers()
       input("Clic tecla Enter [continuar]: ")
       limpiar_pantalla()
       campers()
    elif op==3:
       modificar_campers()
       input("Clic tecla Enter [continuar]: ")
       limpiar_pantalla()
       campers()
    elif op==4:
       registrar_notas()
       input("Clic tecla Enter [continuar]: ")
       limpiar_pantalla()
       campers()
       
def trainers():
    limpiar_pantalla()    
    op=menu_trainers()
    if op==1:
        crear_trainers()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        trainers()
    elif op==2:
        buscar_trainer()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        trainers()
    elif op==3:
        modificar_trainers()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        trainers()
        
def matriculas():
    limpiar_pantalla()    
    op=menu_matriculas()
    if op==1:
        asignar_camper_a_ruta()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        matriculas()
    elif op==2:
        asignar_fechas_matricula()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        matriculas()
    elif op==3:
        enlistar_matriculas()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        matriculas()
    
def rutas():
    limpiar_pantalla()    
    op=menu_rutas()
    if op==1:
        crear_rutas()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        rutas()
    elif op==2:
        listar_rutas()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        rutas()
    elif op==3:
        modificar_rutas()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        rutas()
        
def modulos():
    limpiar_pantalla()    
    op=menu_modulos()
    if op==1:
        registrar_modulos()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        modulos()
    elif op==2:
        enlistar_modulos_bajo_rendimiento()
        input("Clic tecla Enter [continuar]: ")
        limpiar_pantalla()
        modulos()
    
def reportes():
    limpiar_pantalla()    
    op=menu_reportes()
    if op==1:
       listar_campers_inscritos()
       input("Clic tecla Enter [continuar]: ")
       limpiar_pantalla()
       reportes()
    elif op==2:
       listar_campers_aprobados()
       input("Clic tecla Enter [continuar]: ")
       limpiar_pantalla()
       reportes()
    elif op==3:
       listar_trainers()
       input("Clic tecla Enter [continuar]: ")
       limpiar_pantalla()
       reportes()

    
#start
while True: 
    limpiar_pantalla()
    op=menu_principal()
    if  op==1:
       campers()
    elif op==2:
       trainers()
    elif op==3:
       matriculas()
    elif op==4:
       rutas()
    elif op==5:
       modulos()
    elif op==6:
       reportes()
    elif op==7:
       print("\nSaliendo...")
       salir()
       break