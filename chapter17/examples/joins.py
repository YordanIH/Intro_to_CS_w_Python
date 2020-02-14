>>> import sqlite3                                        
>>> con=sqlite3.connect('population.db')                  
>>> cur=con.cursor()
>>> cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')
<sqlite3.Cursor object at 0x7fe3e818f7a0>
>>> cur.execute('CREATE TABLE PopByCountry(Region TEXT, Country TEXT, Population INTEGER)')
<sqlite3.Cursor object at 0x7fe3e818f7a0>
>>> countries = [("Eastern Asia", "China", 1285238), ("Eastern Asia","DPR Korea", 24056), ("Eastern Asia", "Hong Kong (China)", 8764), ("Eastern Asia", "Mongolia", 3407), ("Eastern Asia", "Republic of Korea", 41491), ("Eastern Asia", "Taiwan", 1433), ("North America", "Bahamas", 368), ("North America", "Canada", 40876), ("North America", "Greenland", 43), ("North America", "Mexico", 126875), ("North America", "United States", 493038)]
>>> regions = [('Southern Asia', 2051941), ('Eastern Asia', 1362955), ('Northern Africa', 1037463), ('Asia Pacific', 785468), ('Southeastern Africa', 743112), ('Middle East', 687630), ('North America', 661157), ('South America', 593121), ('Western Europe', 387933), ('Central Africa', 330993), ('Eastern Europe', 223427), ('Japan', 100562)]
>>> for c in countries:
...     cur.execute('INSERT INTO PopByCountry VALUES (?, ?, ?)', (c[0], c[1], c[2]))
... 
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
>>> for r in regions:
...     cur.execute('INSERT INTO PopByRegion VALUES(?, ?)', (r[0], r[1]))                                                     ... 
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
<sqlite3.Cursor object at 0x7fe3e818f7a0>
>>> cur.execute('''
... SELECT PopByRegion.Region, PopByCountry.Country
... FROM PopByRegion INNER JOIN PopByCountry
... WHERE (PopByRegion.Region = PopByCountry.Region)
... AND (PopByRegion.Population > 1000000)
... ''')
<sqlite3.Cursor object at 0x7fe3e818f7a0>
>>> cur.fetchall()
[('Eastern Asia', 'China'), ('Eastern Asia', 'DPR Korea'), ('Eastern Asia', 'Hong Kong (China)'), ('Eastern Asia', 'Mongolia'), ('Eastern Asia', 'Republic of Korea'), ('Eastern Asia', 'Taiwan')]