# 사전 생성
d = {}
d['k1'] = 'v1'
print('k1' in d)
print('k2' in d)

=========================================

# 사전 생성
d = {}
d['k1'] = 'v1'
d['k2'] = 'v2'
d['k3'] = 'v3'
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

========================================

d = {}
d['k1']='v1'
print(d)
d['k2']='v2'
print(d)
d['k3']='v3'
print(d)
d.pop('k1')
print(d)
d.popitem()
print(d)

