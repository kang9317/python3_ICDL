sql="""
    INSERT INTO Student VALUES
    (?,?,?)
"""
c = conn.cursor()
c.execute(sql,('학생2',2,'서울'))

data = [
    ('학생3',3,'서울'),
    ('학생4',4,'서울'),
    ('학생5',5,'서울')
]
c.executemany(sql,data)
c.close()
conn.commit()
