st = 'Korea'
print('*', format(st, '<10s'), format(st, 's'))

n = 10000
print('*', format(n, '8,d'), format(n,'#x'))

pi = 3.1415926

print('*', format(pi,'8.2f'), format(pi,'E'))

print('*','정수{:8,d} 실수{:8.2f}'.format(n,pi))
print('*', '{:#x} {:8.3E}'.format(n, pi))
      
print('*', '{0:d} {0:#o}'.format(n))
print('*', '{1:+5.2f} {0:#b}'.format(n,pi))

print('*', '{0:>8s} {0[2]}'.format(st))
