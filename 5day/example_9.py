def myfunc():
    '''문서설명.
    
    
    이 함수는 아무일도 하지 않는 함수로 함수의 docstring을 설명하기
    위한 함수이다.
    
    파라미터: 없음
    리턴: 없음
    '''
    pass

print(myfunc.__doc__)
help(myfunc)
