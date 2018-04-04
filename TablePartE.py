import happybase as hb

conn = hb.Connection()

table = conn.table('powers')
columns = (b'professional:name', b'custom:color', b'personal:hero', b'professional:xp', b'personal:power')

for key, data in table.scan(columns=columns, include_timestamp=True):
    print('Found: {}, {}'.format(key, data))

conn.close()