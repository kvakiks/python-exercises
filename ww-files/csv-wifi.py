import csv

with open('wifi.csv', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter=';'))
    del data[0]

    final = {}
    for address in data:
        district = address[1]
        acpoints = address[-1]
        final[district] = final.get(district, 0) + int(acpoints)

    result = sorted(final.items(), key=lambda row: (-row[1], row[0]))

    for d, a in result:
        print(f'{d}: {a}')
