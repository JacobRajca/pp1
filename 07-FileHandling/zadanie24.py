import csv

with open('studentslist.txt','r') as file:
    csvreader = csv.reader(file,delimiter=',')
    for row in csvreader:
        print('|'.join(row))
    
with open('studentslist.csv',newline='') as csvfile:
    reader_new = csv.DictReader(csvfile)
    for row in reader_new:
        if int(row['age']) < 30:
            print(row['first_name'], row['last_name'], row['email'])