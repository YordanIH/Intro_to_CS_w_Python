import sqlite3 as dbapi

con=dbapi.connect("database.db")
cur=con.cursor()
cur.execute('CREATE TABLE Numbers(Val INTEGER)')
cur.execute('INSERT INTO Numbers Values(1)')
cur.execute('INSERT INTO Numbers Values(2)')
cur.execute('SELECT * FROM Numbers')
cur.execute('SELECT * FROM Numbers WHERE 1/0')
cur.execute('SELECT * FROM Numbers WHERE 1/0 AND Val > 0 ')
cur.execute('SELECT * FROM Numbers WHERE Val > 0 AND 1/0')

for rows in cur.fetchall():
    print(rows)

