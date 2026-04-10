import csv

with open('titanic.csv', encoding='utf-8') as file:
    reader = list(csv.reader(file, delimiter=';'))
    del reader[0]

    # имена выживших пассажиров, которым было менее 18 лет, каждое на отдельной строке
    male = [row[1] for row in reader if int(row[0]) == 1 and row[2] == 'male' and float(row[-1]) < 18.0]
    female = [row[1] for row in reader if int(row[0]) == 1 and row[2] == 'female' and float(row[-1]) < 18.0]

    print(*male, sep='\n')
    print(*female, sep='\n')