#vamos a crear un usario que pregunte al usariopor las ventas de un rango de años y muestre por pantalla 
#una serie con los datos de las ventas indexadas

import pandas as pd

inicio= int(input('Introduce el año inical de ventas: '))
fin= int(input('Introduce el año final de ventas: '))
ventas = {}
for i in range (inicio, fin+1):
    ventas[i]= float(input('Introduce las ventas del año '+ str(i)+ ': '))
    
ventas = pd.Series(ventas)
print('Ventas \n', ventas)
print('Ventas con descuento \n', ventas*0.9)