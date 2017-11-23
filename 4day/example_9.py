# 사전 생성
d = {}
print(d)
# 사전에 데이터를 저장하는 일반적인 방식
d['k1']='v1'
print(d)
d['k2']='v2'

# 사전에서 데이터를 조회하는 일반적인 방식
print(d['k1'])
print(d['k2'])
try:
    print(d['k3'])
except KeyError:
    pass

print(d.get('k1'))
print(d.get('k1'),'default_value')
