import csv

# with open('filepath.csv', 'r') as csv_file:
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    print(csv_reader)