a={1:'a',2:'b'}

# key, val을 동시에 조회한다
for k,v in a.items():
    print(k,v)

# a의 key 목록만 조회한다
for k in a.keys():
    print(k)

# a의 값만 조회한다
for v in a.values():
    print(v)
