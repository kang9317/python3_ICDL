f = open('todo.txt', 'wt')
f.write('2016-05-01\n')
f.write(' - [] 책 읽기\n')
f.write(' - [] 커피한잔\n')
f.write(' - [] 회의\n')
f.close()


=============================================================
f = open('todo.txt', 'r')

data = f.read()
print(data)
