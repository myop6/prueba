import pandas as pd

from comentarios_sin_nc import comentarios_sin_nc


def tratar_comentarios(fichero):


    # Carga el archivo Excel
    df_comentarios = pd.read_excel(fichero, sheet_name="Hoja3")

    df_comentarios.sort_values(by=['equipo', 'fecha_reporte'], inplace=True)

    hoja_comentarios = {}


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


    resultado_comentarios = [value for value in hoja_comentarios.values()]
    df_resultado_comentarios = pd.DataFrame(resultado_comentarios)



    '''
    # Guardar el resultado en un nuevo archivo Excel
    nuevo_archivo_excel = "/home/ariasmo/Escritorio/resultado_comentarios.xlsx"  # Nombre del nuevo archivo Excel
    df_resultado_comentarios.to_excel(nuevo_archivo_excel, index=False)
    '''

    print("\nArchivo resultado comentarios creado exitosamente. Continuando programa...\n\n")

    return df_resultado_comentarios

