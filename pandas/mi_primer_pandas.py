import pandas as pd 

# Estructura tipo Series
# serie = pd.Series(data, index=index)

nombres = pd.Series(['Camilo','Tatiana', 'Villa'], index=[1,2,3])
print(nombres)
print(type(nombres))

mi_primer_df = pd.DataFrame({
    'name': ['Camilo', 'Tatiana', 'Villa'],
    'pais': ['Colombia', 'Peru', 'Argentina']
},
    columns=['name', 'pais']
)

print(mi_primer_df)
mi_primer_df.loc[2] = ['Maria', 'Uruguay']
print(mi_primer_df.loc[2])



