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





s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'],
                 dtype='string')
print(s)



df = pd.DataFrame([['María', 18], ['Luis', 22], ['Carmen', 20]], columns=['Nombre', 'Edad'])
print(df)