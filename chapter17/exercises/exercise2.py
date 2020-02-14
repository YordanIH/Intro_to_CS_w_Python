

>>> import sqlite3
>>> con=sqlite3.connect('census.db')
>>> cur=con.cursor()
>>> cur.execute('''CREATE TABLE Capitals(Province TEXT, Capital TEXT, Popuation INTEGER)''')
<sqlite3.Cursor object at 0x7f98c0190810>
>>> table = [('Newfoundland and Labrador', "St. John's", 172918),('Prince Edward Island', 'Charlottetown', 58358),('Nova Scotia', 'Halifax', 359183),('New Brunswick', 'Fredericton', 81346),('Quebec', 'Qeubec City', 682757),('Ontario', 'Toronto', 4682897),('Manitoba', 'Winnipeg', 671274),('Saskatchewan', 'Regina', 192800),('Alberta', 'Edmonton', 937845),('British Columbia', 'Victoria', 311902),('Yukon Territory', 'Whitehorse', 21405),('Northwest Territories', 'Yellowknife', 16541),('Nunavut', 'Iqaluit', 5236)]
>>> for row in table:
...  cur.execute('INSERT INTO Capitals VALUES (?, ?, ?)', row)
... 
<sqlite3.Cursor object at 0x7f98c0190810>
<sqlite3.Cursor object at 0x7f98c0190810>
<sqlite3.Cursor object at 0x7f98c0190810>
<sqlite3.Cursor object at 0x7f98c0190810>
<sqlite3.Cursor object at 0x7f98c0190810>
<sqlite3.Cursor object at 0x7f98c0190810>
<sqlite3.Cursor object at 0x7f98c0190810>
<sqlite3.Cursor object at 0x7f98c0190810>
<sqlite3.Cursor object at 0x7f98c0190810>
<sqlite3.Cursor object at 0x7f98c0190810>
<sqlite3.Cursor object at 0x7f98c0190810>
<sqlite3.Cursor object at 0x7f98c0190810>
<sqlite3.Cursor object at 0x7f98c0190810>
>>> con.commit()

#a

>>> cur.execute('SELECT * FROM Capitals')
<sqlite3.Cursor object at 0x7f98c0190810>
>>> for row in cur.fetchall():
...     print(row)
... 
('Newfoundland and Labrador', "St. John's", 172918)
('Prince Edward Island', 'Charlottetown', 58358)
('Nova Scotia', 'Halifax', 359183)
('New Brunswick', 'Fredericton', 81346)
('Quebec', 'Qeubec City', 682757)
('Ontario', 'Toronto', 4682897)
('Manitoba', 'Winnipeg', 671274)
('Saskatchewan', 'Regina', 192800)
('Alberta', 'Edmonton', 937845)
('British Columbia', 'Victoria', 311902)
('Yukon Territory', 'Whitehorse', 21405)
('Northwest Territories', 'Yellowknife', 16541)
('Nunavut', 'Iqaluit', 5236)

#b

>>> cur.execute('''
... SELECT Density.Population,Capitals.Popuation
... FROM Density INNER JOIN Capitals
... WHERE Capitals.Province = Density.Province''')
<sqlite3.Cursor object at 0x7f98c0190810>
>>> cur.fetchall()
[(512930, 172918), (135294, 58358), (908007, 359183), (729498, 81346), (7237479, 682757), (11410046, 4682897), (1119583, 671274), (978933, 192800), (2974807, 937845), (3907738, 311902), (28674, 21405), (37360, 16541), (26745, 5236)]
>>> cur.execute('''
... ALTER TABLE Capitals RENAME Popuation TO Population
... ''')
<sqlite3.Cursor object at 0x7f98c0190810>

#c

>>> cur.execute('''
... SELECT Density.Area
... FROM Capitals INNER JOIN Density
... WHERE Capitals.Province = Density.Province
... AND Capitals.Population > 100000''')
<sqlite3.Cursor object at 0x7f98c0190810>
>>> cur.fetchall()
[(370501.69,), (52917.43,), (1357743.08,), (907655.59,), (551937.87,), (586561.35,), (639987.12,), (926492.48,)]

#d

>>> cur.execute('''
... SELECT Density.Province
... FROM Density INNER JOIN Capitals
... WHERE Density.Province = Capitals.Province
... AND Density.Population / Density.Area < 2
... AND Capitals.Population > 500000''')
<sqlite3.Cursor object at 0x7f98c0190810>
>>> cur.fetchall()
[]

#e
>>> cur.execute('''
... SELECT SUM(Density.Area)
... FROM Density
... ''')
<sqlite3.Cursor object at 0x7f98c0190810>
>>> cur.fetchall()
[(9012112.19,)]


#f
>>> cur.execute('SELECT AVG(Population) FROM Capitals')
<sqlite3.Cursor object at 0x7f98c0190810>
>>> cur.fetchall()
[(630343.2307692308,)]

#g
>>> cur.execute('SELECT MIN(Population) FROM Capitals')
<sqlite3.Cursor object at 0x7f98c0190810>
>>> cur.fetchall()
[(5236,)]

#h
>>> cur.execute('SELECT MAX(Population) FROM Density')
<sqlite3.Cursor object at 0x7f98c0190810>
>>> cur.fetchall()
[(11410046,)]

#i
>>> cur.execute('''SELECT A.Province, B.Province
... FROM Density A INNER JOIN Density B
... WHERE A.Province < B.Province
... AND ABS(A.Population / A.Area - B.Population / B.Area) <
... 0.5''')
<sqlite3.Cursor object at 0x7f98c0190810>
>>> cur.fetchall()
[('Newfoundland and Labrador', 'Saskatchewan'), ('Manitoba', 'Saskatchewan'), ('Alberta', 'British Columbia'), ('Northwest Territories', 'Yukon Territory'), ('Northwest Territories', 'Nunavut'), ('Nunavut', 'Yukon Territory')]