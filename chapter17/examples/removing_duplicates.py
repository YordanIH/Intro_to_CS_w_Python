>>> cur.execute('''SELECT PopByRegion.Region 
... FROM PopByRegion INNER JOIN PopByCountry 
... WHERE (PopByRegion.Region = PopByCountry.Region)
... AND ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)''')
<sqlite3.Cursor object at 0x7fe3e818f7a0>
>>> cur.fetchall()
[('Eastern Asia',), ('North America',), ('North America',)]

>>> cur.execute('''SELECT DISTINCT PopByRegion.Region
... FROM PopByRegion INNER JOIN PopByCountry... WHERE (PopByRegion.Region = PopByCountry.Region)                      ... AND ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)''')
<sqlite3.Cursor object at 0x7fe3e818f7a0>
>>> cur.fetchall()
[('Eastern Asia',), ('North America',)]