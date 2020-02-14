#aggregation

>>> cur.execute('SELECT SUM (Population) FROM PopByRegion')
<sqlite3.Cursor object at 0x7f88a81907a0>
>>> cur.fetchone()
(8965762,)

#grouping

>>> cur.execute('''SELECT Region, SUM (Population) FROM PopByCountry GROUP BY Region''')
<sqlite3.Cursor object at 0x7f88a8190810>
>>> cur.fetchall()
[('Eastern Asia', 1364389), ('North America', 661200)]
>>> cur.execute('''SELECT SUM (Population) FROM PopByCountry WHERE Region = "North America"''')
<sqlite3.Cursor object at 0x7f88a8190810>
>>> cur.fetchall()
[(661200,)]
>>> cur.execute('''SELECT SUM (Population) FROM PopByCountry WHERE Region = "Eastern Asia"''')
<sqlite3.Cursor object at 0x7f88a8190810>
>>> cur.fetchall()
[(1364389,)]

#self-joins

>>> cur.execute('''
... SELECT A.Country, B.Country
... FROM   PopByCountry A INNER JOIN PopByCountry B
... WHERE  (ABS(A.Population - B.Population) <=1000)
... AND    (A.Country != B.Country)''')
<sqlite3.Cursor object at 0x7f88a8190810>
>>> cur.fetchall()
[('Republic of Korea', 'Canada'), ('Bahamas', 'Greenland'), ('Canada', 'Republic of Korea'), ('Greenland', 'Bahamas')]
>>> cur.execute('''
... SELECT A.Country, B.Country
... FROM   PopByCountry A INNER JOIN PopByCountry B
... WHERE  (ABS(A.Population - B.Population) <=1000)
... AND    (A.Country < B.Country)''')
<sqlite3.Cursor object at 0x7f88a8190810>
>>> cur.fetchall()
[('Bahamas', 'Greenland'), ('Canada', 'Republic of Korea')]

#Nested Queries

>>> cur.execute('''SELECT DISTINCT Region
... FROM PopByCountry
... WHERE (PopByCountry.Population != 8764)''')
<sqlite3.Cursor object at 0x7f88a8190810>
>>> cur.fetchall()
[('Eastern Asia',), ('North America',)]
>>> cur.execute('''SELECT DISTINCT Region
... FROM PopByCountry
... WHERE (PopByCountry.Population != 8764)''')
<sqlite3.Cursor object at 0x7f88a8190810>
>>> cur.fetchall()
[('Eastern Asia',), ('North America',)]
>>> cur.execute('''
... SELECT DISTINCT Region
... FROM PopByCountry
... WHERE (PopByCountry.Population = 8764)
... ''')
<sqlite3.Cursor object at 0x7f88a8190810>
>>> cur.fetchall()
[('Eastern Asia',)]
>>> cur.execute('''
... SELECT DISTINCT Region
... FROM PopByCountry
... WHERE Region NOT IN
...     (SELECT DISTINCT Region
...     FROM PopByCountry
...     WHERE (PopByCountry.Population = 8764))
... ''')
<sqlite3.Cursor object at 0x7f88a8190810>
>>> cur.fetchall()
[('North America',)]


# Transactions

>>>cur.execute('SELECT SignedOut FROM Books WHERE ISBN = ?', isbn) 
>>>signedOut = cur.fetchone()[0]
>>>cur.execute('''UPDATE Books SET SignedOut = ?
...            WHERE ISBN = ?''', signedOut + 1, isbn)
>>>cur.commit()

>>>cur.execute('SELECT SignedOut FROM Books WHERE ISBN = ?', isbn) 
>>>signedOut = cur.fetchone()[0]
>>>cur.execute('''UPDATE Books SET SignedOut = ?
...         WHERE ISBN = ?''', signedOut - 1, isbn)
>>>cur.commit()





