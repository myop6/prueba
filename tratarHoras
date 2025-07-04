import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tratarHoras import tratarHoras 

def tratarHoras (fichero):

# Leer el archivo Excel
df = pd.read_excel(fichero)
df.rename(columns={"Employee id":"Id"}, inplace=True)
# Asegurarse de que los nombres de columnas estén limpios df.columns = df.columns.str.strip().str.lower()

# Crear columna fecha a partir de año y mes df["fecha"] = pd.to_datetime(df["Year"].astype(str) + "-" + df["Month"].astype(str) + "-01")

# Filtrar últimos 12 meses
hoy = datetime.today()
hace_12_meses = hoy - relativedelta(months=12) df_12m = df[df["fecha"] >= hace_12_meses]

# Normalizar actividad en minúsculas
df_12m["Statistical Key figure description"] = df_12m["Statistical Key figure description"].str.strip().str.lower()

# Clasificar actividades
df_12m["es_mantenimiento"] = df_12m["Statistical Key figure description"] == "MNT: Inspection / Revision"
df_12m["es_extensivo"] = df_12m["actividad"] == "MNT: Extensive Service"
df_12m["es_cbk"] = df_12m["actividad"].isin(["CBK: Callback n.c. - external influence", "CBK: Callbacks covered", "CBK: Callbacks not covered"])

# Agrupar y sumar por Id y nombre
resumen = df_12m.groupby(["Id"]).apply(lambda x: pd.Series({
    "horas_mantenimiento": x.loc[x["es_mantenimiento"], "Hour quantity actual MTD/YTD"].sum(),
    "horas_extensivo": x.loc[x["es_extensivo"], "Hour quantity actual MTD/YTD"].sum(),
    "horas_cbk": x.loc[x["es_cbk"], "Hour quantity actual MTD/YTD"].sum()
})).reset_index()


return resumen

