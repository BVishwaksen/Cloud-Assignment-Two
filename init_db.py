import sqlite3

connection = sqlite3.connect('cloudassignment.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username,firstname,lastname,email,userpassword) VALUES (?,?,?,?,?)",
            ('defaultname','defaultfirst','defaultlast','email@default.com','defaultpassword')
            )

connection.commit()
connection.close()