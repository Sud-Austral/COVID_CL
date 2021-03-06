import pandas as pd

def ConvertirFecha(fecha):
    return fecha[-2:] + "-" + fecha[5:-3] + "-" + fecha[:4]

def DescargarPasoAPaso():
    d = pd.read_csv("https://github.com/MinCiencia/Datos-COVID19/raw/master/input/Paso_a_paso/paso_a_paso.csv")
    dfinal = d.melt(id_vars=d.columns[:5], var_name='Fecha', value_name='Etapa')
    #dfinal["Fecha"] = dfinal["Fecha"].apply(ConvertirFecha) 
    dfinal["Fecha"] = pd.to_datetime(dfinal["Fecha"]).dt.date
    dfinal.to_excel("COVID/Paso a Paso.xlsx", index=False)
    return

def UpdateDatabase():
    print("Comenzó...")
    DescargarPasoAPaso()





if __name__ == '__main__':
    print('Iniciado proceso...')
    UpdateDatabase()
    print('Proceso finalizado.')
