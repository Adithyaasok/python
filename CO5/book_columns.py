
import csv
with open("book.csv","r") as f:
    for row in csv.reader(f):
        print(row[0], row[1], row[3])
