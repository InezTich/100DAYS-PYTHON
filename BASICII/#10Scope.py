'''
Scope : mean how you can access variable in ouer program
global variable : we can access anytime anywhere we want


1 - start check with local scope variable
2 - Parent check with Parent local scrope variable
3 - Global 
4 - build-in function python.

'''
# Scope - what variable do I have access to?

# that mean variable total is global scope
total = 100


def some_funct():

  number = 20  # private variable can use only in function


print(total)
# print(number) # error number is not define

a = 1


def confusion():
  a = 5
  return a


print(a)
print(confusion())
