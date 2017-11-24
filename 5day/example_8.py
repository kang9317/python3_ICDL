def add(*args):
    total=0
    for i in args:
        total += i
    return total

vals = [1,2]
print(add(*vals))

##############################################

vals=add(1,2,3,4,5,6,7,8,9,10)
print(add(vals))

##############################################

def print_args(**kwlist):
    print(kwlist)

vals={'p3':'3','p1':'1','p2':'2'}
print_args(**vals)
