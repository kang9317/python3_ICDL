# 리스트 리터럴로 생성하기
data = [
    ['a','b','c','d','e'],
    ['f','g','h','i','j'],
    ['k','l','m','n','o'],
    ['p','q','r','s','t']
]

# 조회 방법
data[0]

data[0][1]

# 조작 방법
data[0][1] = 'z'

print(data)

# 데이터 정렬
data[0].sort()

print(data)
