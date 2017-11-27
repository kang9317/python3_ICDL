import sqlite3
conn = sqlite3.connect('student.db')
print(type(conn))

sql="""
    CREATE TABLE Student (
    name varchar(30),
    no integer,
    addr varchar(100)
    )
"""
c = conn.cursor()
c.execute(sql)
c.close()
