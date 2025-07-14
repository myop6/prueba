import pandas as pd
import config
import warnings
import tkinter as tk

from completo import completo
from imprimirVentana import imprimirVentana
from seleccionar import seleccionar
from tratarHorasEscaleras import tratarHorasEscaleras
from tratar_certificaciones import tratar_certificaciones
from tratar_nc import tratar_nc
from tratar_comentarios import tratar_comentarios
from completo_rep import completo_rep
from tratarHoras import tratarHoras
from tratarHorasCompleto import tratarHorasCompleto
from typing import Set
from incumplimientosCompleto import incumplimientosCompleto
from contar import contar

warnings.filterwarnings('ignore')

def main():

    while True:

        opcion_seleccionada=input('Selecciona una opción \n 1.Obtener certificaciones \n 2.Incumplimientos certificación ascensores \n 3.Incumplimientos certificación escaleras \n '
                                  '4.Incumplimientos certificación completo \n 5.Gestión NCs - Completo (Consolida en un fichero NCs y comentarios) \n 6.Gestión NCs - Completo con rep\n 7.Salir\n Introduzca opción:>>>')


        if opcion_seleccionada=='1':
            print("Busque y abra el fichero excel con las certificaciones\n")
            archivo_excel = seleccionar()
            print("Archivo abierto correctamente, ejecutando programa. Espere....\n")
            tratar_certificaciones(archivo_excel,opcion_seleccionada)
        elif opcion_seleccionada == '2':
            print("Seleccione el fichero excel con las horas en ascensores de cierre de mes \n")
            fichero = seleccionar()
            print("Seleccione el fichero excel con las horas en ascensores del mes en curso\n")
            horasMes = seleccionar()
            print("Seleccione el fichero excel con las certificaciones\n")
            certificacion = seleccionar()
            print("Seleccione el fichero excel del personal\n")
            personal= seleccionar()
            print("Seleccione el fichero excel con las notas\n")
            notas = seleccionar()
            print("Archivos abiertos correctamente, ejecutando programa. Espere....\n")
            tratarHorasCompleto(fichero, horasMes, certificacion,personal,opcion_seleccionada,notas)
        elif opcion_seleccionada == '3':
            print("Seleccione el fichero excel con las horas en escaleras, hoja1 12 meses y hoja2 mes en curso \n")
            fichero = seleccionar()
            print("Seleccione el fichero excel con las certificaciones \n")
            certificacion = seleccionar()
            print("Seleccione el fichero excel del personal\n")
            personal = seleccionar()
            print("Seleccione el fichero excel con las notas\n")
            notas = seleccionar()
            print("Archivos abiertos correctamente, ejecutando programa. Espere....\n")
            tratarHorasEscaleras(fichero, certificacion, personal, opcion_seleccionada,notas)
        elif opcion_seleccionada == '4':
            print("Seleccione el fichero excel con las horas en ascensores de cierre de mes\n")
            horasCierreAsc = seleccionar()
            print("Seleccione el fichero excel con las horas en ascensores del mes en curso\n")
            horasMesAsc = seleccionar()
            print("Seleccione el fichero excel con las horas en escaleras \n")
            horasEsc = seleccionar()
            print("Seleccione el fichero excel con las certificaciones\n")
            certificacion = seleccionar()
            print("Seleccione el fichero excel del personal\n")
            personal= seleccionar()
            print("Seleccione el fichero excel con las notas\n")
            notas = seleccionar()
            print("Archivos abiertos correctamente, ejecutando programa. Espere....\n")
            incumplimientosCompleto(horasCierreAsc, horasMesAsc,horasEsc, certificacion,personal,opcion_seleccionada,notas)
        elif opcion_seleccionada == '5':
            imprimirVentana(opcion_seleccionada)
            print("Busque y abre el fichero excel con las NCs\n")
            archivo_excel = seleccionar()
            print("Archivo abierto correctamente, ejecutando programa. Espere....\n")
            completo(archivo_excel)
        elif opcion_seleccionada == '6':
            print("Busque y abre el fichero excel con las NCs\n")
            archivo_excel = seleccionar()
            opcion_seleccionada = '7'
            print("Abierto correctamenete, ahora seleccione el fichero con los parte de reparación\n")
            archivo_rep = seleccionar()
            print("Archivo abierto correctamente, ejecutando programa. Espere....\n")
            completo_rep(archivo_excel,archivo_rep)
        elif opcion_seleccionada == '7':
            break
        elif opcion_seleccionada ==':':
            cantidad=int(input("Seleccione cantidad"))
            contar(cantidad)
        else:
            print('Error')


if __name__=="__main__":

    main()

