import csv

with open('data.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)

    result = {}
    for row in reader:
        *evr, adress = row
        name, domain = adress.split('@')
        result[domain] = result.setdefault(domain, 0) + 1
    
    final = [[key, value] for key, value in result.items()]
    final.sort(key=lambda row: (row[1], row[0]))
    final.insert(0, ['domain', 'count'])



with open('domain_usage.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final)
