from csv import reader

with open("original.csv")as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)