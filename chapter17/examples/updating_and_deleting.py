>>> cur.execute('''UPDATE PopByRegion SET Population=100600 WHERE Region = "Japan"''')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.fetchone()
('Japan', 100600)
>>> cur.execute('DELETE FROM PopByRegion WHERE Region < "L"')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.execute('SELECT * FROM PopByRegion')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.fetchall()
[('Southeastern Africa', 743112)]
>>> cur.execute('INSERT INTO PopByregion VALUES ("Japan", 100562)')
<sqlite3.Cursor object at 0x7f7f281921f0>
>>> cur.execute('DROP TABLE PopByRegion')
<sqlite3.Cursor object at 0x7f7f281921f0>