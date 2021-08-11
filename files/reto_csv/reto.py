import pandas as pd
import csv
from utils import get_tag

data = pd.read_csv("Curso_python/files/reto_csv/TSLA.csv")

with open('Curso_python/files/reto_csv/analisis_archivo.csv', 'w', encoding='utf-8') as file:
    print(data[['Date', 'Low']])
    writer = csv.DictWriter(file, fieldnames=['Fecha', 'Concepto'], delimiter=' ')
    writer.writeheader()

    for _, row in data[['Date', 'Low']].iterrows():
        writer.writerow({'Fecha': row['Date'], 'Concepto': get_tag(row['Low'])})

# descargar archivo
# guardarlo donde lo necesitemos
# leer el archivo
