fruits=[]

fruits.append('바나나')

fruits.insert(0,'키위')

fruits[1:1]=['사과']

print(fruits)

===================================

fruits=['키위','사과','바나나']

del fruits[0]

fruits.remove('사과')

fruits[0:1]=[]

print(fruits)
