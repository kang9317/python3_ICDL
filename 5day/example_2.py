for n in range(2,10):
    if n != 2 and n % 2 == 0:
        continue
    for x in range(3,n):
        if n % x == 0:
            break
    else:
        print('{}는 소수임'.format(n))
      
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
