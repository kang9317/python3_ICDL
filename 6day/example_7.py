sql = 'select * from student order by no desc'
c = conn.cursor()
c.execute(sql)

# 모든 데이터를 가져온다.
for s in c.fetchall():
    print(s)
