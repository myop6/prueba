import pandas as pd
import config

from seleccionar_ruta import seleccionar_ruta


def tratar_certificaciones(archivo_excel,opcion_seleccionada):

    print("Filtrando y ordenando certificaciones\n")
    df = pd.read_excel(archivo_excel,header=1)
    df_filtrado = df[df['Status'] == 'Certified']

    def sustituir(cadena):
        if 'S1' in cadena:
            return cadena.replace(cadena, '1')
        elif 'S2' in cadena:
            return cadena.replace(cadena, '2')
        elif 'S3' in cadena:
            return cadena.replace(cadena, '3')
        elif 'S4' in cadena:
            return cadena.replace(cadena, '4')
        elif 'L1' in cadena:
            return cadena.replace(cadena, '1')
        elif 'L2' in cadena:
            return cadena.replace(cadena, '2')
        elif 'L3' in cadena:
            return cadena.replace(cadena, '3')
        elif 'L4' in cadena:
            return cadena.replace(cadena, '4')
        elif 'Cinturón blanco' in cadena:
            return cadena.replace(cadena, '0')
        return cadena

    df_filtrado['Certification'] = df_filtrado['Certification'].apply(sustituir)

    # print(df_filtrado)

    df_ascensores = df_filtrado[(df_filtrado['Certification Program'] == 'EI Service Technician Elevator') | (
            df_filtrado['Certification Program'] == 'Assistant Service Technician')]
    df_escaleras = df_filtrado[df_filtrado['Certification Program'] == 'EI Service Technician Escalator']

    nivel_max_ascensores = df_ascensores.loc[df_ascensores.groupby('Personal ID')['Certification'].idxmax()]
    nivel_max_escaleras = df_escaleras.loc[df_escaleras.groupby('Personal ID')['Certification'].idxmax()]

    if opcion_seleccionada=="1":
        print("Seleccione ruta y nombre para el fichero con el resultado\n")
        nuevo_arhivo_excel=seleccionar_ruta()
        #nuevo_archivo_excel = "/home/ariasmo/Escritorio/Certificaciones.xlsx"  # Nombre del nuevo archivo Excel
        if nuevo_arhivo_excel:
            with pd.ExcelWriter(nuevo_arhivo_excel) as writer:
                nivel_max_ascensores.to_excel(writer, sheet_name='hoja1', index=False)
                nivel_max_escaleras.to_excel(writer, sheet_name='hoja2', index=False)
        else:
            print('Guardado cancelado\n')

    print("Archivo certificaciones filtrado creado exitosamente.\n\n")

    if config.variable==1:
        return nivel_max_ascensores
    elif config.variable==2:
        return  nivel_max_escaleras

