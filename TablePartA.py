import happybase as hb

conn = hb.Connection()

powers = {
    'row key': dict(),
    'personal': dict(),
    'professional': dict(),
    'custom': dict()
}

conn.create_table('Powers', powers)
print('Created table Powers')

food = {
    'row key': dict(),
    'nutrition': dict(),
    'taste': dict()
}

conn.create_table('Food', food)
print('Created table Food')

conn.close()
