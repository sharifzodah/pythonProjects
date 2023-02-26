import csv

with open('files/weather.csv', 'r') as f1:
    data = list(csv.reader(f1))
print(data)

city = input("Enter a city: ")
for row in data[1:]:
    if row[0] == city:
        print(row[1])

