tuple1 = (1,2,3,4,5,6)
print(tuple1)
tuple2 = tuple([1,2,3,4,5,6])
print(tuple2)
tuple3 = tuple(range(0,10))
print(tuple3)
tuple4 = tuple()
print(tuple4)


==============================================

odd_list = (1,3,5,7,9,11,13,15,17,19)
even_list = (2,4,6,8,10,12,14,16,18,20)

2 in even_list

1 not in even_list

all_list = odd_list + even_list
print(all_list)

odd_list * 2

2 * odd_list

odd_list[0]

odd_list[0:5]

odd_list[0:5:2]

len(odd_list)

min(odd_list)

max(odd_list)

odd_list.index(3)

odd_list.index(2)     #ValueError 

odd_list.count(5)
