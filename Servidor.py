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

    salida2.to_excel("Vacuna/Vacunacion_Consolidado.xlsx", index = False)
    print("Hola")



    #Tratamiento de datos de Hospitales referentes a estadísticas Regionales de Covid-19 en Chile
    #Autor: Ian Meza
    #Fecha 28/06/2021
    
    print("Comenzó Hospitales...")

    #Archivo Regiones

    regiones = pd.read_excel("https://github.com/Sud-Austral/COVID_CL/blob/main/Hospitales/CodRegionesCL.xlsx?raw=true")


    #Lectura PCR
    
    pcr = pd.read_csv("https://raw.githubusercontent.com/Sud-Austral/Datos/master/Chile/MinCiencia/Input-minCiencia/ReporteDiario/PCR.csv")

    pcrT = pd.melt(pcr, id_vars=["Region", "Codigo region", "Poblacion"], var_name='Fecha', value_name='PCR')
    del pcrT["Region"]
    del pcrT["Poblacion"]
    dtx = pd.to_datetime(pcrT["Fecha"])
    pcrT["Fecha"] = dtx


    #Lectura UCI

    uci = pd.read_csv("https://raw.githubusercontent.com/Sud-Austral/Datos/master/Chile/MinCiencia/Input-minCiencia/ReporteDiario/UCI.csv")
    uciT = pd.melt(uci, id_vars=["Region", "Codigo region", "Poblacion"], var_name='Fecha', value_name='UCI')
    del uciT["Region"]
    del uciT["Poblacion"]
    dtx2 = pd.to_datetime(uciT["Fecha"])
    uciT["Fecha"] = dtx2


    #Lectura UCI Habilitadas

    ucih = pd.read_excel("https://github.com/MinCiencia/Datos-COVID19/raw/master/input/Camas_uci/last_uci.xlsx", sheet_name="UCI HABILITADA")
    ucihT = pd.melt(ucih, id_vars=["Camas UCI habilitadas"], var_name='Fecha', value_name='UCI Habilitada')
    ucihT = ucihT.rename(columns={'Camas UCI habilitadas':'Region'})
    ucihT = pd.merge(regiones, ucihT, on = 'Region')
    del ucihT["Region"]
    ucihD = ucihT.drop_duplicates()


    #Lectura UCI Ocupada Total

    ucio = pd.read_excel("https://github.com/MinCiencia/Datos-COVID19/raw/master/input/Camas_uci/last_uci.xlsx", sheet_name="UCI OCUPADA TOTAL")
    ucioT = pd.melt(ucio, id_vars=["Camas UCI ocupadas"], var_name='Fecha', value_name='UCI Ocupadas Total')
    ucioT = ucioT.rename(columns={'Camas UCI ocupadas':'Region'})
    ucioT = pd.merge(regiones, ucioT, on = 'Region')
    del ucioT["Region"]
    ucioD = ucioT.drop_duplicates()


    #Lectura UCI Ocupada No Covid-19

    ucionc = pd.read_excel("https://github.com/MinCiencia/Datos-COVID19/raw/master/input/Camas_uci/last_uci.xlsx", sheet_name="UCI OCUPADA NO COVID")
    ucioncT = pd.melt(ucionc, id_vars=["Camas UCI ocupadas no COVID-19"], var_name='Fecha', value_name='UCI Ocupadas No COVID-19')
    ucioncT = ucioncT.rename(columns={'Camas UCI ocupadas no COVID-19':'Region'})
    ucioncT = pd.merge(regiones, ucioncT, on = 'Region')
    del ucioncT["Region"]
    ucioncD = ucioncT.drop_duplicates()


    #Lectura Residencias

    res = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/input/ReporteDiario/ResidenciasSanitarias.csv")
    res = pd.merge(regiones, res, on = 'Region')
    cupos = res['Categoria'] == 'cupos totales'
    usres = res['Categoria'] == 'usuarios en residencia'
    residencias = res['Categoria'] == 'residencias'

    #Filtros
    resCupos = res[cupos]
    resCupos = pd.melt(resCupos, id_vars=["Region", "CodReg", "Categoria"], var_name='Fecha', value_name='Residencias_Cupos totales')

    resUsuarios = res[usres]
    resUsuarios = pd.melt(resUsuarios, id_vars=["Region","CodReg", "Categoria"], var_name='Fecha', value_name='Residencias_Usuarios en residencia')

    resRes = res[residencias]
    resRes = pd.melt(resRes, id_vars=["Region","CodReg", "Categoria"], var_name='Fecha', value_name='Residencias_Residencias')

    #Depuración de columnas
    del resCupos["Categoria"]
    del resCupos["Region"]
    del resUsuarios["Categoria"]
    del resUsuarios["Region"]
    del resRes["Categoria"]
    del resRes["Region"]

    #Conversión de formato de columnas de Fecha
    dt2 = pd.to_datetime(resCupos["Fecha"])
    resCupos["Fecha"] = dt2
    dt3 = pd.to_datetime(resUsuarios["Fecha"])
    resUsuarios["Fecha"] = dt3
    dt4 = pd.to_datetime(resRes["Fecha"])
    resRes["Fecha"] = dt4


    #Lectura Positividad

    positividad = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/input/UC/Positividad%20por%20region.csv")
    positividad = positividad.rename(columns={'codigo_region':'CodReg','fecha':'Fecha','positividad':'Positividad'})

    dt = pd.to_datetime(positividad["Fecha"])
    positividad["Fecha"] = dt
    del positividad["region_residencia"]
    positividad.dropna(axis = 0, inplace = True)

    
    #--------------------------------------------------------#
    # ------------------> Unión de tablas <------------------#
    #--------------------------------------------------------#

    salida = pd.merge(pcrT, uciT, on = ['Codigo region', 'Fecha'], how = 'outer')
    salida = salida.rename(columns={'Codigo region':'CodReg'})

    salida = pd.merge(salida, ucihD, on =['CodReg','Fecha'], how = 'outer')

    salida = pd.merge(salida, ucioD, on =['CodReg','Fecha'], how = 'outer')
    
    salida = pd.merge(salida, ucioncD, on =['CodReg','Fecha'], how = 'outer')
    
    salida = pd.merge(salida, resCupos, on =['CodReg','Fecha'], how = 'outer')
    
    salida = pd.merge(salida, resUsuarios, on =['CodReg','Fecha'], how = 'outer')
    
    salida = pd.merge(salida, resRes, on =['CodReg','Fecha'], how = 'outer')
    
    salida = pd.merge(salida, positividad, on =['CodReg','Fecha'], how = 'outer')

    salida.to_excel("Hospitales/Hospitales.xlsx", index = False)
    
    return

#************************************Actualizar Datos de la organizacion*******************************************

if __name__ == '__main__':
    print('Iniciado proceso...')
    UpdateDatabase()
    print('Proceso finalizado.')