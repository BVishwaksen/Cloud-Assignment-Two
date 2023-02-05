import sqlite3

connection = sqlite3.connect('cloudassignment.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username,firstname,lastname,email,userpassword,fname,count) VALUES (?,?,?,?,?,?,?)",
            ('defaultname','defaultfirst','defaultlast','email@default.com','defaultpassword','defaultfile.txt',6)
            )

connection.commit()
connection.close()