def print_args(p1,p2='p2',p3='p3'):
    print(p1,p2,p3)
print_args()            # TypeError발생 argument 부족

print_args('p1')

print_args('p1','new_p2','new_p3')

print_args('p1',p3='new_p3')
