import happybase as hb

conn = hb.Connection()

table = conn.table('powers')

row = table.row(b'row1')
hero = row[b'personal:hero']
power = row[b'personal:power']
name = row[b'professional:name']
xp = row[b'professional:xp']
color = row[b'custom:color']

print('hero: {} power: {} name: {} xp: {}, color: {}'.format(hero, power, name, xp, color))

conn.close()