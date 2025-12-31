
import csv
with open("name.csv","r") as f:
    for row in csv.reader(f):
        print(row)
