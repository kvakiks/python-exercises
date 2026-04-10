import csv

column = int(input())

with open('deniro.csv', encoding='utf-8') as file:
    reader = csv.reader(file)

    result = list(reader)
    for row in result:
        for i in range(len(row)):
            row[1] = int(row[1])
            row[2] = int(row[2])
    result.sort(key=lambda row: row[column-1])

    for row in result:
        print(*row, sep=',')
