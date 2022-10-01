import pandas as pd

def clean_SNIES(df):
    df = df[["NOMBRE_INSTITUCIÓN", "CARÁCTER_ACADÉMICO", "SECTOR", "CÓDIGO_SNIES_DEL_PROGRAMA", "NOMBRE_DEL_PROGRAMA", "TITULO_OTORGADO", "ESTADO_PROGRAMA", "RECONOCIMIENTO_DEL_MINISTERIO", "RESOLUCIÓN_DE_APROBACIÓN", "FECHA_DE_RESOLUCIÓN", "VIGENCIA_AÑOS", "NIVEL_DE_FORMACIÓN", "MODALIDAD",  "DEPARTAMENTO_OFERTA_PROGRAMA", "MUNICIPIO_OFERTA_PROGRAMA", "COSTO_MATRÍCULA_ESTUD_NUEVOS"]]
    df.columns = ["INSTITUCION", "CARACTER", "SECTOR", "SNIES", "PROGRAMA", "TITULO", "ESTADO", "ACREDITACION", "RESOLUCION", "FECHA DE RESOLUCION", "VIGENCIA(AÑOS)", "NIVEL", "MODALIDAD", "DEPARTAMENTO", "MUNICIPIO", "COSTO" ]
    df["RESOLUCION"].fillna(0, inplace=True)
    df["VIGENCIA(AÑOS)"].fillna(0, inplace=True)
    df = df.astype({"SNIES":"int", "RESOLUCION": "int"})

    df.sort_values(by="ACREDITACION", inplace=True)
    return df

def save_excel(df, name, path):
    if path.exists():
        writer = pd.ExcelWriter(path, engine="openpyxl", mode="a")
        df.to_excel(writer, sheet_name=name, index=False)
        writer.save()
        writer.close()
    else:
        print("here")
        df.to_excel(path, sheet_name=name, index=False)


    # writer = pd.ExcelWriter(path, mode= "w")

    # for column in df:
    #     column_width = max(df[column].astype(str).map(len).max(), len(column))
    #     col_idx = df.columns.get_loc(column)
    #     writer.sheets[name].set_column(col_idx, col_idx, column_width)
    # writer.save()
    # writer.close()
    
def resize_column_width (path):
    if path.exists():
        print("si")
        writer = pd.ExcelWriter(path, mode= "w")
        writer.sheets
    else:
        print("No")
        


