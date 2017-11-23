a=[1,2,3,4,5]
print(a)

b=a[:]
print(b)

c=a.copy()
print(c)

d=list(a)
print(d)

==================================

data = [1,[2,3,4],5]

# 얕은 복사
s_copied =data.copy()
print(s_copied)

# 깊은 복사
import copy
d_copied = copy.deepcopy(data)
print(d_copied)

# 원본 데이터 수정
data[1][1]='xx'
print(data)
