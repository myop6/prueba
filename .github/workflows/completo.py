import pandas as pd

from comentarios_sin_nc import comentarios_sin_nc
from seleccionar_ruta import seleccionar_ruta
from tratar_comentarios import tratar_comentarios
from tratar_nc import tratar_nc


def completo(fichero):

    df_nc=tratar_nc(fichero)
    df_comentarios=tratar_comentarios(fichero)

    df_comentarios['fecha_reporte'] = pd.to_datetime(df_comentarios['fecha_reporte'], dayfirst="True")

    # Combinar los DataFrames en uno solo basado en la columna de equipo y fecha d  apertura
    df_combinado = pd.merge(df_nc, df_comentarios, on=['equipo', 'fecha_reporte'], how='left',suffixes=('_principal', '_secundaria'))


    # Ordenar los datos por equipo y fecha de apertura para facilitar el procesamiento
    df_combinado.sort_values(by=['equipo', 'fecha_reporte'], inplace=True)

    # Agrupar textos asociados en una lista para cada fecha y equipo
    df_combinado['textos_asociados_nc1'] = df_combinado.groupby(['equipo', 'fecha_reporte'])['Comment'].transform(lambda x: x.tolist())

    # Obtener textos asociados que coincidan con el equipo y la fecha de cierre
    df_combinado['textos_cierre'] = df_combinado.apply(lambda row: df_comentarios[(df_comentarios['equipo'] == row['equipo']) & (df_comentarios['fecha_reporte'] == row['fecha_cierre'])]['Comment'].tolist(), axis=1)

    # Filtrar textos asociados que estén entre la fecha de apertura y cierre para cada equipo
    df_combinado['textos_entre'] = df_combinado.apply(lambda row: df_comentarios[(df_comentarios['equipo'] == row['equipo']) & (df_comentarios['fecha_reporte'] > row['fecha_reporte']) & (df_comentarios['fecha_reporte'] < row['fecha_cierre'])]['Comment'].tolist(), axis=1)

    # Obtener textos asociados que coincidan con el equipo y la fecha posterior a la fecha de cierre
    df_combinado['textos_post_cierre'] = df_combinado.apply(lambda row: df_comentarios[(df_comentarios['equipo'] == row['equipo']) & (df_comentarios['fecha_reporte'] > row['fecha_cierre'])]['Comment'].tolist(), axis=1)

    # Obtener textos asociados que coincidan con el equipo y sean anteriores a la fecha de apertura
    df_combinado['textos_pre_apertura'] = df_combinado.apply(lambda row: df_comentarios[(df_comentarios['equipo'] == row['equipo']) & (df_comentarios['fecha_reporte'] < row['fecha_reporte'])]['Comment'].tolist(), axis=1)

    # Seleccionar las columnas requeridas para el resultado final
    #columnas_resultado = ['equipo', 'calle', 'poblacion', 'estado', 'fecha_reporte', 'tipo_nc', 'textos_asociados_nc','textos_entre', 'fecha_cierre', 'textos_cierre', 'textos_post_cierre', 'textos_pre_apertura']

    columnas_resultado = ['equipo', 'emplazamiento', 'poblacion','calle', 'estado', 'fecha_reporte', 'tipo_nc', 'NC RI', 'textos_asociados_nc', 'textos_entre', 'fecha_cierre', 'textos_cierre', 'textos_post_cierre', 'textos_pre_apertura','razon cierre manual']

    df_resultado = df_combinado[columnas_resultado]

    #buscar los comentarios en los equipos que no tienen NC marcadno los importantes
    comentarios_sin_nc(df_nc,df_comentarios)
    '''
    # Guardar el resultado en un nuevo archivo Excel
    nuevo_archivo_excel = "/home/ariasmo/Escritorio/resultado_completo.xlsx"  # Nombre del nuevo archivo Excel
    df_resultado.to_excel(nuevo_archivo_excel, index=False)
    '''

    print("\nArchivo completo creado exitosamente. Continuando programa...\n\n")

    return df_resultado