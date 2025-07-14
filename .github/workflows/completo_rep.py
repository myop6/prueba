
import pandas as pd

from completo import completo
from seleccionar_ruta import seleccionar_ruta


def completo_rep(fichero,fichero_rep):

    df_completo=completo(fichero)
    df_rep=pd.read_excel(fichero_rep)

    '''
    print(df_completo.dtypes)
    print(df_rep.dtypes)
    '''

    df_rep.rename(columns={'Equipo':'equipo'},inplace=True)

    df_completo['fecha_reporte']=pd.to_datetime(df_completo['fecha_reporte'], errors='coerce')
    df_completo['fecha_cierre'] = pd.to_datetime(df_completo['fecha_cierre'], errors='coerce')
    df_rep['Día actividad'] = pd.to_datetime(df_rep['Día actividad'], errors='coerce')

    df_completo['REP'] = 'No'

    #df_combinado = pd.merge(df_completo, df_rep, on='equipo', how='left')

    #condicion=(df_combinado['fecha_reporte']>=df_combinado['Día actividad'])&(df_combinado['Día actividad']<=df_combinado['fecha_cierre'])

    #df_completo.loc[condicion.groupby(df_combinado['equipo']).transform('any'),'REP']='Si'


    for index1,row1 in df_completo.iterrows():
        print(index1)
        for index2, row2 in df_rep.iterrows():
            if row1['equipo']==row2['equipo'] and row1['fecha_reporte']<=row2['Día actividad']<=row1['fecha_cierre']:
                df_completo.at[index1, 'REP'] = 'Si'
                break
        #if not df_rep[(df_rep['equipo']==row1['equipo']) & (df_completo['fecha_reporte']<=df_rep['Día actividad'])&(df_rep['Día actividad']<=df_completo['fecha_cierre'])].empty:
                #df_completo.at[index,'Rep']='Si'


    #print(df_completo)

    print("Seleccione la ubicación para guardar el archivo completo con las reparaciones incluidas \n")
    # Guardar el resultado en un nuevo archivo Excel
    nuevo_archivo_excel=seleccionar_ruta()
    #nuevo_archivo_excel = "/home/ariasmo/Escritorio/resultado_completo_rep.xlsx"  # Nombre del nuevo archivo Excel

    if nuevo_archivo_excel:
        df_completo.to_excel(nuevo_archivo_excel, index=False)
    else:
        print('Guardado cancelado')

    print("\nArchivo completo con rep creado exitosamente.\n\n")



