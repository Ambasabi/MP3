import happybase as hb
import csv

conn = hb.Connection()

table = conn.table('powers')


def read_csv():
    csvfile = open('input.csv', "r")
    csvreader = csv.reader(csvfile)
    return csvreader, csvfile


def insert_row(table, row):
    data = {
        b'row key': row[0],
        b'personal:hero': row[1],
        b'personal:power': row[2],
        b'professional:name': row[3],
        b'professional:xp': row[4],
        b'custom:color': row[5]
    }
    table.put(row[0], data)


csvreader, csvfile = read_csv()

for row in csvreader:
    insert_row(table, row)


# data = {
#     b'personal:name': b'Raju',
#     b'personal:city': b'Hyderabad',
#     b'professional:designation': b'Manager',
#     b'professional:salary': b'50000'
# }
#
# table.put(b'row1', data)

print('Inserted data')

conn.close()