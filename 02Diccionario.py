import pandas as pd

def estadisticas_notas(notas):
    notas=pd.Series(notas)
    estadistica= pd.Series([notas.min(), notas.max(), notas.mean(), notas.std], index=['Min','Max','Media','Desviacion Estandar'])
    return estadistica

notas = {'Juan':9,'Juanita':5.9,'Pedro':8.2,'Rosalba':6.9,'Federico':4.5,'Alberto':7.5,}

print(estadisticas_notas(notas))