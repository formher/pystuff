import csv


with open ('2.csv', 'r') as csv_file:
    csvr = csv.reader(csv_file)
    next(csvr)
    bsr = []
    timestamp = []
    for line in csvr:
        bsr.append(line[1])
        timestamp.append(line[7])
        # print(line[1])

print(bsr)
print(timestamp)