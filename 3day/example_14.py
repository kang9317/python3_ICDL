print("The sum of 1 + 2 is {0}".format(1+2))

print("{0} * {1} is {2}".format(2,3,2*3))
print("{1} * {0} is {2}".format(2,3,2*3))
print("{x} * {y} is {result}".format(x=3, y=4,result=3*4))

print('{:f}'.format(3.14159265))
print('{:.8f}'.format(3.14159265))

print('{:d}'.format(123456789))

print('{:20d}'.format(123456789))

print('{:,d}'.format(123456789))

print('{:20,d}'.format(123456789))

print('{:020,d}'.format(123456789))

print('{:x}'.format(123456789))

print('{:#x}'.format(123456789))

print('{:+f} {:+f}'.format(-3.14,3.14))

print('{:-f} {:-f}'.format(-3.14,3.14))

print('{: f} {: f}'.format(-3.14,3.14))

print('{:>20d}|{:>20d}'.format(123456789,-123456789))

print('{:<20d}|{:<20d}'.format(123456789,-123456789))

print('{:=20d}|{:=20d}'.format(123456789,-123456789))

print('{:^20d}|{:^20d}'.format(123456789,-123456789))
