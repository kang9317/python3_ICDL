c = conn.cursor()
c.execute("""
    INSERT INTO Student VALUES
    (?,?,?)
""",('학생2',2,'서울'))

c.executemany(sql,data)
c.close()
conn.commit()
