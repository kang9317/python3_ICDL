for n in range(2,10):
    if n != 2 and n % 2 == 0:
        continue
    for x in range(3,n):
        if n % x == 0:
            break
    else:
        print('{}는 소수임'.format(n))

        
        
''' Result
2는 소수임
3는 소수임
5는 소수임
7는 소수임
'''
==================================================================

밑은 잘못된 예시

for n in range(2,10):
    if n != 2 and n % 2 == 0:
        continue
    for x in range(3,n):
        if n % x == 0:
            break
        else:
            print('{}는 소수임'.format(n))
''' Result
5는 소수임
5는 소수임
7는 소수임
7는 소수임
7는 소수임
7는 소수임
'''
