#a
>>> con = sqlite3.connect('census.db')
>>> cur=con.cursor
>>> cur=con.cursor()     
#b                                   
>>> cur.execute('CREATE TABLE Density(Province TEXT, Population INTEGER, Area REAL)')
<sqlite3.Cursor object at 0x7f88a81907a0>
>>> con.commit()
#c
>>> countries = [("Newfoundland and Labrador",512930,370501.69),("Prince Edward Island",135294,5684.39),("Nova Scotia",908007,52917.43),("New Brunswick",729498,71355.67),("Quebec",7237479,1357743.08),("Ontario",11410046,907655.59),("Manitoba",1119583,551937.87),("Saskatchewan",978933,586561.35),("Alberta",2974807,639987.12),("British Columbia",3907738,926492.48),("Yukon Territory",28674,474706.97),("Northwest Territories",37360,1141108.37),("Nunavut",26745,1925460.18)]
>>> for c in countries:
...     cur.execute('INSERT INTO Density VALUES (?, ?, ?)',(c[0], c[1], c[2]))
... 
<sqlite3.Cursor object at 0x7f88a81907a0>
<sqlite3.Cursor object at 0x7f88a81907a0>
<sqlite3.Cursor object at 0x7f88a81907a0>
<sqlite3.Cursor object at 0x7f88a81907a0>
<sqlite3.Cursor object at 0x7f88a81907a0>
<sqlite3.Cursor object at 0x7f88a81907a0>
<sqlite3.Cursor object at 0x7f88a81907a0>
<sqlite3.Cursor object at 0x7f88a81907a0>
<sqlite3.Cursor object at 0x7f88a81907a0>
<sqlite3.Cursor object at 0x7f88a81907a0>
<sqlite3.Cursor object at 0x7f88a81907a0>
<sqlite3.Cursor object at 0x7f88a81907a0>
<sqlite3.Cursor object at 0x7f88a81907a0>
>>> con.commit()
#d
>>> con.execute('SELECT * FROM Density')
<sqlite3.Cursor object at 0x7f88a8190500>
>>> cur.execute('SELECT * FROM Density')
<sqlite3.Cursor object at 0x7f88a81907a0>
>>> cur.fetchall()
[('Newfoundland and Labrador', 512930, 370501.69), ('Prince Edward Island', 135294, 5684.39), ('Nova Scotia', 908007, 52917.43), ('New Brunswick', 729498, 71355.67), ('Quebec', 7237479, 1357743.08), ('Ontario', 11410046, 907655.59), ('Manitoba', 1119583, 551937.87), ('Saskatchewan', 978933, 586561.35), ('Alberta', 2974807, 639987.12), ('British Columbia', 3907738, 926492.48), ('Yukon Territory', 28674, 474706.97), ('Northwest Territories', 37360, 1141108.37), ('Nunavut', 26745, 1925460.18)]
#e
>>> cur.execute('SELECT Population FROM Density')
<sqlite3.Cursor object at 0x7f88a81907a0>
>>> cur.fetchall()                             
[(512930,), (135294,), (908007,), (729498,), (7237479,), (11410046,), (1119583,), (978933,), (2974807,), (3907738,), (28674,), (37360,), (26745,)]
#f
>>> cur.execute('''
... SELECT Province FROM Density
... WHERE (Population < 1000000)''')
<sqlite3.Cursor object at 0x7f88a81907a0>
>>> cur.fetchall()
[('Newfoundland and Labrador',), ('Prince Edward Island',), ('Nova Scotia',), ('New Brunswick',), ('Saskatchewan',), ('Yukon Territory',), ('Northwest Territories',), ('Nunavut',)]
#g
>>> cur.execute('''
... SELECT Province FROM Density
... WHERE (Population < 1000000)
... OR (Population > 5000000)''')
<sqlite3.Cursor object at 0x7f88a81907a0>
>>> cur.fetchall()
[('Newfoundland and Labrador',), ('Prince Edward Island',), ('Nova Scotia',), ('New Brunswick',), ('Quebec',), ('Ontario',), ('Saskatchewan',), ('Yukon Territory',), ('Northwest Territories',), ('Nunavut',)]
#h
>>> cur.execute('''
... SELECT Province FROM Density
... WHERE NOT (Population < 1000000)
... OR (Population > 5000000)''')
<sqlite3.Cursor object at 0x7f88a81907a0>
>>> cur.fetchall()
[('Quebec',), ('Ontario',), ('Manitoba',), ('Alberta',), ('British Columbia',)]
#i
>>> cur.execute('''
... SELECT Province FROM Density
... WHERE (Area > 200000)''')
<sqlite3.Cursor object at 0x7f88a81907a0>
>>> cur.fetchall()
[('Newfoundland and Labrador',), ('Quebec',), ('Ontario',), ('Manitoba',), ('Saskatchewan',), ('Alberta',), ('British Columbia',), ('Yukon Territory',), ('Northwest Territories',), ('Nunavut',)]
#j
>>> cur.execute('''
... SELECT Province,(Population/Area) FROM Density
... ''')
<sqlite3.Cursor object at 0x7f88a81907a0>
>>> cur.fetchall()                               
[('Newfoundland and Labrador', 1.384420135843375), ('Prince Edward Island', 23.8009707286094), ('Nova Scotia', 17.15893988048928), ('New Brunswick', 10.223406212848959), ('Quebec', 5.330521736115201), ('Ontario', 12.570898175154742), ('Manitoba', 2.0284583842743027), ('Saskatchewan', 1.6689353978062142), ('Alberta', 4.648229483118348), ('British Columbia', 4.217776273802028), ('Yukon Territory', 0.060403579075318826), ('Northwest Territories', 0.03274009812056676), ('Nunavut', 0.013890185981410428)]
