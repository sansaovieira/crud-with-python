# Importing SQLite...
import sqlite3 as lite

#Creating Connection...
con = lite.connect('data.db')

#Creating table...
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE form(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia DATE, estado TEXT, assunto TEXT)")