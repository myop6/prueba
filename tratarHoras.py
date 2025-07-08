import pandas as pd

from datetime import datetime
from dateutil.relativedelta import relativedelta


from seleccionar_ruta import seleccionar_ruta

def tratarHoras (fichero,opcion_seleccionada):

    # Leer el archivo Excel
    df = pd.read_excel(fichero)
    df.rename(columns={"Employee id":"id","Statistical key figure description":"actividad","Year":"año","Month name short":"mes","Hour quantity actual MTD/YTD":"horas"}, inplace=True)
    df.columns = df.columns.str.strip().str.lower()

    map_actividad={"CBK: Callback n.c. - external influence":"cbk","CBK: Callbacks covered":"cbk",
                       "CBK: Callbacks not covered":"cbk","MNT: Inspection / Revision":"mantenimiento","MNT: Extensive Service":"extensivo"}

    df["actividad"]=df["actividad"].replace(map_actividad)

    '''print(df.head())'''

# ---------- 2. Mapear meses abreviados en inglés ----------
    meses_dict = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,
    'may': 5, 'jun': 6, 'jul': 7, 'aug': 8,
    'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }



    df["mes"] = df["mes"].astype(str).str.strip().str.lower()
    df["mes_num"] = df["mes"].map(meses_dict)

    '''print(df["mes"].unique())
    print(df["mes_num"].unique())'''

    # Verificar errores de mapeo
    if df["mes_num"].isnull().any():
        print("Algunos meses no se pudieron interpretar correctamente:")
        print(df["mes"].unique())
        exit()

    # ---------- 3. Crear columna de fecha ----------
    df["fecha"] = pd.to_datetime(dict(year=df["año"], month=df["mes_num"], day=1))

    # ---------- 4. Filtrar últimos 12 meses ----------

    fecha_corte = datetime.today() - relativedelta(months=12)
    df_12m = df[df["fecha"] >= fecha_corte]

    '''
    print(f"📅 Fecha de corte: {fecha_corte.strftime('%Y-%m-%d')}")
    print(f"📊 Filas antes del filtro: {len(df)}")
    print(f"📉 Filas después del filtro: {len(df_12m)}")'''

    # ---------- 5. Normalizar columnas ----------
    df_12m["actividad"] = df_12m["actividad"].astype(str).str.strip().str.lower()
    df_12m["horas"] = pd.to_numeric(df_12m["horas"], errors="coerce").fillna(0)

    # ---------- 6. Agrupar por id y actividad ----------
    resumen_12m = df_12m.pivot_table(
        index="id",
        columns="actividad",
        values="horas",
        aggfunc="sum",
        fill_value=0
    ).reset_index()

    # ---------- 7. Consolidar columnas ----------
    for col in ["mantenimiento", "extensivo", "cbk"]:
        if col not in resumen_12m.columns:
            resumen_12m[col] = 0

    resumen_12m["horas_cbk"] = resumen_12m["cbk"]
    resumen_12m["horas_extensivo"] = resumen_12m["extensivo"]
    resumen_12m["horas_mantenimiento"] = resumen_12m["mantenimiento"]

    # ---------- 8. Seleccionar columnas finales ----------
    resumen_final = resumen_12m[["id", "horas_mantenimiento", "horas_extensivo", "horas_cbk"]]

    # ---------- 9. Mostrar vista previa ----------

    print("\nResumen final de horas por id creado correctamente. Siguiendo programa\n")
    '''print(resumen_final.head())'''

    if(opcion_seleccionada==1):
        ruta_salida = seleccionar_ruta()
        if ruta_salida:
            resumen_final.to_excel(ruta_salida , index=False)
            print("Archivo creado")
        else:
            print('Guardado cancelado')
    else:
        return resumen_final
