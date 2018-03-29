import happybase as hb

conn = hb.Connection()

powers = {
    'row key': dict(),
    'personal': dict(),
    'professional': dict(),
    'custom': dict()
}

conn.create_table('powers', powers)

food = {
    'row key': dict(),
    'nutrition': dict(),
    'taste': dict()
}

conn.create_table('food', food)

conn.close()
