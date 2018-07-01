import csv

with open("capitals.txt") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)