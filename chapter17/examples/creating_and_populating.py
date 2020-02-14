>>> import sqlite3
>>> con=sqlite3.connect('population.db')
>>> cur = con.cursor()
>>> cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')
<sqlite3.Cursor object at 0x7f7f281927a0>
>>> cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
<sqlite3.Cursor object at 0x7f7f281927a0>
>>> cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", '
... '743112)')
<sqlite3.Cursor object at 0x7f7f281927a0>
>>> cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')
<sqlite3.Cursor object at 0x7f7f281927a0>
>>> cur.execute('INSERT INTO PopByRegion VALUES (?, ?)', ("Japan", 100562))
<sqlite3.Cursor object at 0x7f7f281927a0>
>>> con.commit()
>>> con.close()

