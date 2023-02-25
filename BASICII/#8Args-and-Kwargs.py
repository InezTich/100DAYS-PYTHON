# *args and **kwargs arguments
'''info
*args : can allow as to list of arguments [1,2,3,4,5]
**kwargs : can allow us to use keyword argument 
    (num1=1,num2=10)
Rule : rule of ordering
      (params, *args, defualt parameters, **kwargs)
'''


def super_funct(*args):
  return sum(args)


total = super_funct(1, 2, 3, 4, 5)
print(total)


def funct_args_kwarg(*args, **kwargs):
  print(kwargs)
  total = 0
  for item in kwargs.values():
    total += item
  return sum(args) + total


print(funct_args_kwarg(1, 2, 3, 4, 5, num1=1, num2=10))


# (params, *args, defualt parameters, **kwargs)
def super_funct_kwargs(name, *args, greet='hi', **kwargs):
  print('Params =', name)
  print('Args = ', args)
  print("Default Parameter = ", greet)
  print('Kwargs = ', kwargs)


super_funct_kwargs('Potter',
                   1,
                   2,
                   3,
                   4,
                   5,
                   greet='Hello',
                   id='001',
                   code='BS0022')
