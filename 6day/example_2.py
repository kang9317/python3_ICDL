import sqlite3
conn = sqlite3.connect('student.db')
print(type(conn))

sql="""
    INSERT INTO Student VALUES (
    "학생1",1,"서울 강남구 일동"
    )
"""
c = conn.cursor()
c.execute(sql)
c.close()
conn.commit()
