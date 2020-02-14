>>> con= sqlite3.connect('population2.db')
>>> cur=con.cursor()
>>> cur.execute('''CREATE TABLE PopByRegion (
... Region TEXT NOT NULL,
... Population INTEGER NOT NULL,
... PRIMARY KEY (Region))''')
<sqlite3.Cursor object at 0x7fc0c81907a0>
>>> cur.execute('''
... CREATE TABLE PopByCountry(
... Region TEXT NOT NULL,
... Country TEXT NOT NULL,
... Population INTEGER NOT NULL,
... CONSTRAINT CountryKey PRIMARY KEY (Region, Country))''')
>>> con.commit()
>>> con.close


