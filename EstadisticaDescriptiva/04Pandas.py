import pandas as pd
import matplotlib.pyplot as plt

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

plt.scatter(df["ocean_proximity"][:10], df["median_house_value"][:10])

plt.xlabel('Proximidad')
plt.ylabel('Precio')

plt.title('Grafico de Dispersion de Proximidad del oceano vs Precio')
plt.show()