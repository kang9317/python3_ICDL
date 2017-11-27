sql = 'select * from student'
c = conn.cursor()
c.execute(sql)

# 하나의 데이터만
print(c.fetchone())

# 10개의 데이터를
for s in c.fetchmany(10):
    print(s)


==============================================

sql = 'select * from student'
c = conn.cursor()
c.execute(sql)

# 모든 데이터를 가져온다.
for s in c.fetchall():
    print(s)
