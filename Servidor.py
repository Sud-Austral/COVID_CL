#Autor: Ian M.
#Fecha: 21/06/2021

import pandas as pd

#************************************Bucle general********************************************************
def UpdateDatabase():
    print("Comenzó...")
    
    #primera dosis
    primera = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_1eraDosis.csv")
    Tprimera = pd.melt(primera, id_vars=["Region", "Codigo region", "Comuna", "Codigo comuna", "Poblacion"], var_name='Fecha', value_name='1era Dosis')
    del Tprimera["Region"]
    del Tprimera["Codigo region"]
    del Tprimera["Comuna"]
    del Tprimera["Poblacion"]
    Tprimera.dropna(axis = 0, inplace = True)
    
    #segunda dosis
    segunda = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_2daDosis.csv")
    Tsegunda = pd.melt(segunda, id_vars=["Region", "Codigo region", "Comuna", "Codigo comuna", "Poblacion"], var_name='Fecha', value_name='2da Dosis')
    del Tsegunda["Region"]
    del Tsegunda["Codigo region"]
    del Tsegunda["Comuna"]
    del Tsegunda["Poblacion"]
    Tsegunda.dropna(axis = 0, inplace = True)

    #Dosis única
    unica = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_UnicaDosis.csv")
    T_unica = pd.melt(primera, id_vars=["Region", "Codigo region", "Comuna", "Codigo comuna", "Poblacion"], var_name='Fecha', value_name='Dosis Única')
    del T_unica["Region"]
    del T_unica["Codigo region"]
    del T_unica["Comuna"]
    del T_unica["Poblacion"]
    T_unica.dropna(axis = 0, inplace = True)

    salida1 = pd.merge(Tprimera, Tsegunda, on = ["Codigo comuna","Fecha"])
    salida2 = pd.merge(salida1, T_unica, on = ["Codigo comuna","Fecha"])

    salida2.to_excel("Vacuna/Vacunacion_Consolidado.xlsx")
    print("Hola")
    return

#************************************Actualizar Datos de la organizacion*******************************************

if __name__ == '__main__':
    print('Iniciado proceso...')
    UpdateDatabase()
    print('Proceso finalizado.')