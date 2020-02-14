>>> con=sqlite3.connect('population.db')
>>> cur=con.cursor()
>>> cur.execute('SELECT Region, Population FROM PopByRegion')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.fetchone()
('Central Africa', 330993)
>>> cur.fetchall()
[('Southeastern Africa', 743112), ('Japan', 100562), ('Japan', 100562)]
>>> cur.fetchone()
>>> cur.fetchall()
[]
>>> cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Region')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.fetchall()
[('Central Africa', 330993), ('Japan', 100562), ('Japan', 100562), ('Southeastern Africa', 743112)]
>>> cur.execute('''SELECT Region, Population FROM PopByRegion ORDER BY Population DESC''')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.fetchall()
[('Southeastern Africa', 743112), ('Central Africa', 330993), ('Japan', 100562), ('Japan', 100562)]
>>> cur.execute('SELECT Region FROM PopByRegion')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.fetchall()
[('Central Africa',), ('Southeastern Africa',), ('Japan',), ('Japan',)]
>>> cur.execute('SELECT * FROM PopByRegion')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.fetchall()
[('Central Africa', 330993), ('Southeastern Africa', 743112), ('Japan', 100562), ('Japan', 100562)]