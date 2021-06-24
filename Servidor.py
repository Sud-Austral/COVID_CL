import pandas as pd

#************************************Bucle general********************************************************
def UpdateDatabase():
    print("Comenzo...")
    df = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto80/vacunacion_comuna_1eraDosis.csv")
    df.to_excel("Vacuna/Vacunacion2.xlsx")
    print("Hola")
    return

#************************************Actualizar Datos de la organizacion*******************************************

if __name__ == '__main__':
    print('Iniciado proceso...')
    UpdateDatabase()
    print('Proceso finalizado.')