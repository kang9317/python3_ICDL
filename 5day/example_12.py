from pprint import pprint
import pickle

person1 = {
    'name': '김하나',
    'height': 170,
    'weight': 60
}
person2 = {
    'name': '이대호',
    'height': 200,
    'weight': 80
}

# 데이터를 리스트로 만들었다.
people = [person1,person2]

# 데이터를 저장한다.
with open('poeple.pickle', 'wb') as f:
    pickle.dump(people,f)
    
# 저장된 데이터를 읽는다.
with open('poeple.pickle', 'rb') as f:
    loaded_people = pickle.load(f)
    
pprint(loaded_people)
print(loaded_people)
