import csv

data1= []
data2 = []

with open('bright_stars.csv','r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data1.append(row)

with open('sorted.csv','r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data2.append(row)

headers1 = data1[0]
planet_data1= data1[1:]

headers2 = data2[0]
planet_data2= data2[1:]

headers = headers1 + headers2

planet_datas = []
for index, data_row in enumerate(planet_data1):
    planet_datas.append(planet_data1[index] + planet_data2[index])

with open('main.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_datas)
