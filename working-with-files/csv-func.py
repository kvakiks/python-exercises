import csv

text = '''name,grade
Timur,5
Arthur,4
Anri,5'''

with open('test.csv', 'w', encoding='utf-8') as file:
    file.write(text)


def csv_columns(filename):                              # Column sort function
    with open(filename, encoding='utf-8') as file:
        reader = list(csv.reader(file))

        final = {}
        columns = reader[0]

        for i in range(len(columns)):
            col = columns[i]
            for row in reader:
                if row == columns:
                    continue
                final.setdefault(col, []).append(row[i])

    return final

print(csv_columns('test.csv'))

