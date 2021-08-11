import pandas as pd
from utils import get_tag

data = pd.read_csv("Curso_python/files/reto_csv/TSLA.csv")
new_data = {}
new_data  = data['Low'].apply(get_tag)
new_data = {'Fecha': data['Date'],'Concepto': new_data}
df = pd.DataFrame(new_data)
print(df)
new_file = df.to_csv("Curso_python/files/reto_csv/analisis_archivo_con_pandas.csv", sep = ',')
