# 파일명: my_math.py
"""
My Math
=======
"""

__all__ = ['fib']
#__all__ = ['fib','sum'] # import * 에서 fib, sum을 export할 것을 명시,
# 모듈 버전
__version__ = 1.0

# 원주률
PI = 3.1415

def fib(n):
    "피보나치 수열 생성"
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a+b
#=========================================
===========      Result
'''
Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: C:/Users/coms/Desktop/test/my_math.py ===============
>>> import sys
>>> sys.path.insert(0, 'C:/Users/coms/Desktop/test')
>>> import my_math
>>> print('pi={}'.format(my_math.PI))
pi=3.1415
>>> print(list(my_math.fib(10)))
[1, 1, 2, 3, 5, 8]
>>> 
'''
