import csv

with open('salary_data.csv', encoding='utf-8') as file:
    file = csv.DictReader(file, delimiter=';')

    comp_salaries = {}
    for row in file:
        company = row['company_name']
        salary = int(row['salary'])

        data = comp_salaries.setdefault(company, [0, 0])
        data[0] += salary
        data[1] += 1

    for key, value in comp_salaries.items():
        x = value[0] / value[1]
        comp_salaries[key] = round(x, 2)

    result = sorted(comp_salaries, key=lambda company: (comp_salaries[company], company))

    print(*result, sep='\n')

    '''Calculating a top of average salaries in different companies in ASC'''