a = {'one':1, 'two':2, 'three':3}
print(a)
b = dict({'one':1, 'two':2, 'three':3})
print(b)
c = dict(one=1,two=2,three=3)
print(c)
d = dict([('two',2),('one',1),('three',3)])
print(d)

hash('key')

hash('new_key')

# 빈 딕셔너리 생성
numbers = {}
print(numbers)
# 추가, 변경
numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3
numbers.update({"one": "first"})
print(numbers)

# 삭제
del numbers['one']
print(numbers)
