import csv
with open('CSV File\FlieCSV.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    print("ID Name")
    print("--------------------")
    for row in data:
        print(row['Id'], row['Name'])
