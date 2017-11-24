f = open('todo.txt', 'r+')
f.seek(15,0)
f.write('X')
f.close()

############ Result
'''
2016-05-01
 - X] 책 읽기
 - [] 커피한잔
 - [] 회의
'''
