# This is a sample Python script.

import pandas as pd


from completo import completo
from imprimirVentana import imprimirVentana
from seleccionar import seleccionar
from tratar_certificaciones import tratar_certificaciones
from tratar_nc import tratar_nc
from tratar_comentarios import tratar_comentarios
from completo_rep import completo_rep
from tratarHoras import tratarHoras 
from typing import Set


def main():

    import pandas as pd
    '''
    archivo_excel = "/home/ariasmo/Escritorio/NC.xlsx"
    archivo_rep="/home/ariasmo/Escritorio/REP.xlsx"
    '''

    while True:
        opcion_seleccionada=input('Selecciona una opción \n 1.Obtener certificaciones \n 2.Tratar fichero de Nc (Combina lo textos de las NCs que tiene mismo equipo y fechas) \n 3.Tratar fichero de comentarios (Combina lo textos de los comentarios que tiene mismo equipo y fecha) \n '
                                  '4.Completo (Consolida en un fichero NCs y comentarios) \n 5.Completo rep\n 6.Salir\n Introduzca opción:>>>')
        #archivo_excel=input("Propocione dirección del fichero a tratar: ")

        if opcion_seleccionada=='1':
            imprimirVentana(opcion_seleccionada)
            print("Busque y abra el fichero excel con las certificaciones\n")
            archivo_excel = seleccionar()
            print("Archivo abierto correctamente, ejecutando programa. Espere....\n")
            tratar_certificaciones(archivo_excel)
        elif opcion_seleccionada=='2':
            imprimirVentana(opcion_seleccionada)
            print("Busque y abra el fichero excel con las NCs\n")
            archivo_excel = seleccionar()
            print("Archivo abierto correctamente, ejecutando programa. Espere....\n")
            tratar_nc(archivo_excel)
        elif opcion_seleccionada == '3':
            imprimirVentana(opcion_seleccionada)
            print("Busque y abre el fichero excel con las NCs\n")
            archivo_excel = seleccionar()
            print("Archivo abierto correctamente, ejecutando programa. Espere....\n")
            tratar_comentarios(archivo_excel)
        elif opcion_seleccionada == '4':
            imprimirVentana(opcion_seleccionada)
            print("Busque y abre el fichero excel con las NCs\n")
            archivo_excel = seleccionar()
            print("Archivo abierto correctamente, ejecutando programa. Espere....\n")
            completo(archivo_excel)
        elif opcion_seleccionada == '5':
            imprimirVentana(opcion_seleccionada)
            print("Busque y abre el fichero excel con las NCs\n")
            archivo_excel = seleccionar()
            opcion_seleccionada = '6'
            print("Abierto correctamenete, ahora seleccione el fichero con los parte de reparación\n")
            imprimirVentana(opcion_seleccionada)
            archivo_rep = seleccionar()
            print("Archivo abierto correctamente, ejecutando programa. Espere....\n")
            completo_rep(archivo_excel,archivo_rep)
        elif opcion_seleccionada=='7':
            imprimirVentana(opcion_seleccionada)
            print("Busque y abra el fichero excel con las horas de cierre\n")
            archivo_excel = seleccionar()
            print("Archivo abierto correctamente, ejecutando programa. Espere....\n")
            tratarHoras(archivo_excel) 
        elif opcion_seleccionada == '6':
            break
        else:
            print('Error')



if __name__=="__main__":

    main()

