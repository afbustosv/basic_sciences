import pandas as pd

def clean_SNIES(df, inactive_df = 0, mode = 1):
    if mode == 1:
        df = df[["NOMBRE_INSTITUCIÓN", "CARÁCTER_ACADÉMICO", "SECTOR", "CÓDIGO_SNIES_DEL_PROGRAMA", "NOMBRE_DEL_PROGRAMA", "TITULO_OTORGADO", "ESTADO_PROGRAMA", "RECONOCIMIENTO_DEL_MINISTERIO", "RESOLUCIÓN_DE_APROBACIÓN", "FECHA_DE_RESOLUCIÓN", "VIGENCIA_AÑOS", "NIVEL_DE_FORMACIÓN", "MODALIDAD",  "DEPARTAMENTO_OFERTA_PROGRAMA", "MUNICIPIO_OFERTA_PROGRAMA", "COSTO_MATRÍCULA_ESTUD_NUEVOS"]]
        df.columns = ["INSTITUCION", "CARACTER", "SECTOR", "SNIES", "PROGRAMA", "TITULO", "ESTADO", "ACREDITACION", "RESOLUCION", "FECHA DE RESOLUCION", "VIGENCIA(AÑOS)", "NIVEL", "MODALIDAD", "DEPARTAMENTO", "MUNICIPIO", "COSTO" ]
        df["RESOLUCION"].fillna(0, inplace=True)
        df["VIGENCIA(AÑOS)"].fillna(0, inplace=True)
        df = df.astype({"SNIES":"int", "RESOLUCION": "int"})
        df.sort_values(by="ACREDITACION", inplace=True)
        return df
    elif mode == 2:
        df = df[["NOMBRE_INSTITUCIÓN", "SECTOR", "NOMBRE_DEL_PROGRAMA", "ESTADO_PROGRAMA", "RECONOCIMIENTO_DEL_MINISTERIO", "DEPARTAMENTO_OFERTA_PROGRAMA", "MUNICIPIO_OFERTA_PROGRAMA", "COSTO_MATRÍCULA_ESTUD_NUEVOS"]]
        df.columns = ["INSTITUCION",  "SECTOR",  "PROGRAMA",  "ESTADO", "ACREDITACION",  "DEPARTAMENTO", "MUNICIPIO", "COSTO" ]
        df.sort_values(by="ACREDITACION", inplace=True)
        return df
    else :
        print("Error Mode")

def save_excel(list_df, list_name, path):
    writer = pd.ExcelWriter( path, engine="xlsxwriter")
    for idx, df in enumerate(list_df):
        df.to_excel(writer, sheet_name=list_name[idx], index=False)
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            writer.sheets[list_name[idx]].set_column(col_idx, col_idx, column_width)
    writer.save()
    writer.close()

