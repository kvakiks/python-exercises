import csv

from datetime import datetime



def dt_conv(date_time):
    the_date = datetime.strptime(date_time, '%d/%m/%Y %H:%M')

    return the_date

def latest(email, biglist):
    result = [row[2] for row in biglist if email == row[1]]

    return max(result)




with open('name_log.csv', encoding='utf-8') as file:
    reader = list(csv.reader(file))
    columns = reader[0]     # Columns for insertion
    datas = reader[1:]      # Other data

    for row in datas:
        row[2] = dt_conv(row[2])


with open('new_name_log.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(columns)

    final = []
    for row in datas:
        pass