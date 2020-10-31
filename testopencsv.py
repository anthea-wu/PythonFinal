import csv

fn = 'output3.csv'
with open(fn) as csvFile:
    csvDictReader = csv.DictReader(csvFile)
    for row in csvDictReader:
        print(row)