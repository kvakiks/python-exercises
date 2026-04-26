import csv 

with open('sales.csv', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=';')
    next(data)

    for product, old_price, new_price in data:
        old = int(old_price)
        new = int(new_price)
        if old > new:
            print(product)


'''Data processing for getting changed lower prices of products'''
