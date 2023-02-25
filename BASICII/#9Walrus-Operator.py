# Walrus Operator :=
'''
Walrus operator or Assignment expression (:=)
'''

a = 'Hellooooooooo'

if ((n := len(a)) > 10):
  print(f'too long {n} elements.')

while ((n := len(a)) > 1):
  print(n)
  a = a[:-1]

print(a)
