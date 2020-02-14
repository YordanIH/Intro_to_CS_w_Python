>>> cur.execute('SELECT Region FROM PopByRegion WHERE Population>200000')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.fetchall
<built-in method fetchall of sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.fetchall()
[('Central Africa',), ('Southeastern Africa',)]
>>> cur.execute('''SELECT Region FROM PopByRegion WHERE Population > 200000 AND Region < "L"''')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.fetchall()
[('Central Africa',)]
>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.fetchone()
('Japan', 100562)
