# hello.py
def greet() :
    print('How are you?')

def greetName(name):
    print('How are you?', name)

# main.py
import hello
hello.greet()

name = input('이름 입력 :')
hello.greetName(name)

# main2.py
from hello import greetName
name = input("이름 입력: ")
greetName(name)
