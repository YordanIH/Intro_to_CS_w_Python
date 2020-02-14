>>> con=sqlite3.connect('population.db')
>>> cur=con.cursor()
>>> cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')
<sqlite3.Cursor object at 0x7f7f2816c880>
>>> cur.execute('INSERT INTO PopByRegion VALUES ("Mars", NULL)')
<sqlite3.Cursor object at 0x7f7f2816c880>
>>> cur.execute('CREATE TABLE Test (Region TEXT NOT NULL,Population INTEGER)')
<sqlite3.Cursor object at 0x7f7f2816c880>
>>> cur.execute('INSERT INTO Test VALUES (NULL, 456789)')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
sqlite3.IntegrityError: NOT NULL constraint failed: Test.Region
>>> 