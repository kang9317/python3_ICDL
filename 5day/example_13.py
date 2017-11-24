import json

person1 = {
    'name': '김하나',
    'height': 170,
    'weight': 60
}

print(json.dumps(person1))

with open('test.json','w') as f:
    json.dump(person1,f)
    
    
===================================================================

from pprint import pprint
import json

json_data='''{"height": 170, "name": "\uae40\ud558\ub098", "weight": 60}'''
obj = json.loads(json_data)

print('load from string:', end='')

pprint(obj)

with open('test.json','r') as f:
    obj=json.load(f)
    
    print('load from file :', end='')
    pprint(obj)
