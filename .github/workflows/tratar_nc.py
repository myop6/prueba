from time import strptime
import pandas as pd

from seleccionar_ruta import seleccionar_ruta
from textos_sin_nc import textos_sin_nc


def tratar_nc(fichero):


    # Carga el archivo Excel

    df_principal = pd.read_excel(fichero, sheet_name="Hoja1")
    df_secundaria = pd.read_excel(fichero, sheet_name="Hoja2")



    #df_comentarios.sort_values(by=['equipo', 'fecha_reporte'], inplace=True)

    hoja_nc={}
    hoja_textos={}


    #combinar los datos en la hoja de las NCs
    for index, row in df_principal.iterrows():
        key=(row['equipo'],row['fecha_reporte'],row['fecha_cierre'])
        #row['fecha_cierre']=str(row['fecha_cierre'])

        if key in hoja_nc:
            hoja_nc[key]['tipo_nc']+= ' '+row['tipo_nc']
            #hoja_nc[key]['fecha_cierre']+= ' '+row['fecha_cierre']
        else:
            hoja_nc[key]={
                'equipo':row['equipo'],
                'emplazamiento':row['Emplazamiento'],
                'poblacion': row['Población'],
                'calle':row['Calle'],
                'estado': row['Estado de la NC'],
                'fecha_reporte': row['fecha_reporte'],
                'tipo_nc': row['tipo_nc'],
                'NC RI':row['NC Riesgo Inmediato'],
                'fecha_cierre': row['fecha_cierre'],
                'razon cierre manual': row['Razón Cierre Manual']
            }


    #combinar los datos en la hoja de los textos asociados a los equipos con NCs
    for index, row in df_secundaria.iterrows():
        key=(row['equipo'],row['fecha_reporte'])
        #row['fecha_reporte']=str(row['fecha_reporte'])
        row['texto_nc'] = str(row['texto_nc'])

        if key in hoja_textos:
            hoja_textos[key]['texto_nc']+=' '+row['texto_nc']
            #hoja_textos[key]['fecha_texto']+= ' '+row['fecha_texto']
        else:
            hoja_textos[key]={
                'equipo':row['equipo'],
                'fecha_reporte': row['fecha_reporte'],
                'texto_nc': row['texto_nc'],
            }


    '''
    # combinar los datos en la hoja de los textos en todas las instalaciones
    for index, row in df_comentarios.iterrows():
        key = (row['equipo'], row['fecha_reporte'])
        # row['fecha_texto']=str(row['fecha_texto'])
        row['Comment'] = str(row['Comment'])

        if key in hoja_comentarios:
            hoja_comentarios[key]['Comment'] += ' ' + row['Comment']
                # hoja_textos[key]['fecha_texto']+= ' '+row['fecha_texto']
        else:
            hoja_comentarios[key] = {
                'equipo': row['equipo'],
                'fecha_reporte': row['fecha_reporte'],
                'Comment': row['Comment'],
                'tipo':row['ID'],
                }

    '''

    resultado_nc=[value for value in hoja_nc.values()]
    resultado_textos= [value for value in hoja_textos.values()]
    #resultado_comentarios = [value for value in hoja_comentarios.values()]



    df_resultado_nc=pd.DataFrame(resultado_nc)
    df_resultado_textos = pd.DataFrame(resultado_textos)
    #df_resultado_comentarios = pd.DataFrame(resultado_comentarios)

    #cambiar el tipo de datos de una columna en un dataframe
    #df_resultado_textos['fecha_reporte']=pd.to_datetime(df_resultado_textos['fecha_reporte'], dayfirst="True")


    #df_resultado_textos.rename(columns={'fecha_texto':'fecha_reporte'})

    '''
    print(df_resultado_nc.dtypes)
    print(df_principal.dtypes)
    print(df_secundaria.dtypes)
    print(df_resultado_textos.dtypes)
    

    #print(df_resultado_nc)
    #print(df_resultado_textos)


    # Guardar el resultado en un nuevo archivo Excel
    #nuevo_archivo_excel = "/home/ariasmo/Escritorio/resultado_nc.xlsx"  # Nombre del nuevo archivo Excel
    #df_resultado_textos.to_excel(nuevo_archivo_excel, index=False)

    nuevo_archivo_excel = "/home/ariasmo/Escritorio/resultado_nc.xlsx"  # Nombre del nuevo archivo Excel
    df_resultado_nc.to_excel(nuevo_archivo_excel, index=False)
    '''



    # Combinar los DataFrames en uno solo basado en la columna de equipo y fecha d  apertura
    df_combinado =pd.merge(df_resultado_nc, df_resultado_textos,on=['equipo','fecha_reporte'],how='left',suffixes=('_principal', '_secundaria'))

    # Ordenar los datos por equipo y fecha de apertura para facilitar el procesamiento
    df_combinado.sort_values(by=['equipo', 'fecha_reporte'], inplace=True)

    # Agrupar textos asociados en una lista para cada fecha y equipo
    df_combinado['textos_asociados_nc'] = df_combinado.groupby(['equipo', 'fecha_reporte'])['texto_nc'].transform(lambda x: x.tolist())

    # Obtener textos asociados que coincidan con el equipo y la fecha de cierre
    df_combinado['textos_cierre'] = df_combinado.apply(lambda row: df_resultado_textos[(df_resultado_textos['equipo'] == row['equipo']) & (df_resultado_textos['fecha_reporte'] == row['fecha_cierre'])]['texto_nc'].tolist(), axis=1)

    # Filtrar textos asociados que estén entre la fecha de apertura y cierre para cada equipo
    df_combinado['textos_entre'] = df_combinado.apply(lambda row: df_resultado_textos[(df_resultado_textos['equipo'] == row['equipo']) & (df_resultado_textos['fecha_reporte'] > row['fecha_reporte']) & (df_resultado_textos['fecha_reporte'] < row['fecha_cierre'])]['texto_nc'].tolist(), axis=1)

    # Obtener textos asociados que coincidan con el equipo y la fecha posterior a la fecha de cierre
    df_combinado['textos_post_cierre'] = df_combinado.apply(lambda row: df_resultado_textos[(df_resultado_textos['equipo'] == row['equipo']) & (df_resultado_textos['fecha_reporte'] > row['fecha_cierre'])]['texto_nc'].tolist(), axis=1)

    # Obtener textos asociados que coincidan con el equipo y sean anteriores a la fecha de apertura
    df_combinado['textos_pre_apertura'] = df_combinado.apply(lambda row: df_resultado_textos[(df_resultado_textos['equipo'] == row['equipo']) & (df_resultado_textos['fecha_reporte'] < row['fecha_reporte'])]['texto_nc'].tolist(), axis=1)

    #obtener los textos de los equipos que no tienen NC marcando los importantes
    textos_sin_nc(df_combinado,df_resultado_textos)


    # Ordenar los datos por equipo y fecha de apertura para facilitar el procesamiento
    df_combinado.sort_values(by=['equipo', 'fecha_reporte'], inplace=True)


    # Seleccionar las columnas requeridas para el resultado final
    columnas_resultado = ['equipo','emplazamiento','poblacion','calle','estado', 'fecha_reporte', 'tipo_nc','NC RI', 'textos_asociados_nc', 'textos_entre', 'fecha_cierre', 'textos_cierre', 'textos_post_cierre', 'textos_pre_apertura','razon cierre manual']

    df_resultado = df_combinado[columnas_resultado]

    '''
    print("Selecciona la ubicación para guardar el archivo de NCs combinadas \n")
    # Guardar el resultado en un nuevo archivo Excel

    nuevo_excel = seleccionar_ruta()
    # nuevo_excel= "/home/ariasmo/Escritorio/textos_sin_nc.xlsx"  # Nombre del nuevo archivo Excel

    if nuevo_excel:
        df_resultado.to_excel(nuevo_excel, index=False)
    else:
        print('Guardado cancelado')
    '''

    print("\nArchivo resultado NC creado exitosamente. Continuando programa...\n\n")

    return df_resultado