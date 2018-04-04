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

print('Inserted data')

csvfile.close()
conn.close()
