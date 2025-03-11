import pandas as pd

df= pd.read_csv('./EstadisticaDescriptiva/housing.csv')

print(df.head()) #primeras 5 filas
print(df.tail()) #ultimas 5 filas
print(df.iloc[7]) #fila en especfico
print(df["ocean_proximity"]) #columna por su nombre

mediacuartos = df["total_rooms"].mean()
print('Media de cuartos: ', mediacuartos)

medianapoblacion = df["population"].median()
print('Mediana de poblacion: ', medianapoblacion)

std_age = df["housing_median_age"].std()
print('desviacion estandar de años: ', std_age)

filtrodeloceano = df[df['ocean_proximity']=="ISLAND"]#filtrar
print('Filtro de proximidad: ', filtrodeloceano)
