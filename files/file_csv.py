import csv

with open('example.csv', newline='') as File:
    reader = csv.reader(File) 

for row in reader:
    print(row) 


import csv
with open('name.csv') as csvfile:
    reader = csv.DictReader(csvfile)
for row in reader:
      print(row['first_name'], row['last_name'])





