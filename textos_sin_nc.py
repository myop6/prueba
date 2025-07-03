from buscar_palabras import buscar_palabras
from seleccionar_ruta import seleccionar_ruta


def textos_sin_nc(df, df1):

    # Selecciono los equipos con texto que no tienen nc para analizar esos textos
    df_combinado1 =df1.merge(df,on=['equipo'],how='left',indicator=True)

    resultado=df_combinado1[df_combinado1['_merge']=='left_only']

    resultado['palabra_clave'] = df_combinado1['texto_nc_x'].apply(buscar_palabras)


    print("Selecciona la ubicación para guardar el archivo de textos de equipos sin NCs \n")
    # Guardar el resultado en un nuevo archivo Excel
    nuevo_excel=seleccionar_ruta()
    #nuevo_excel= "/home/ariasmo/Escritorio/textos_sin_nc.xlsx"  # Nombre del nuevo archivo Excel

    if nuevo_excel:
        resultado.to_excel(nuevo_excel, index=False)
    else:
        print('Guardado cancelado')


    print("Archivo con textos de equipo sin NC creado exitosamente. Contiuando ejecución \n")

    return

