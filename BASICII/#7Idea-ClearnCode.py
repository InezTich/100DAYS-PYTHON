# Idea for clean code


def is_event(num):
  if num % 2 == 0:
    return True
  elif num % 2 == 1:
    return False


print(is_event(6))


#1 clean more litle bit
def is_event(num):
  if num % 2 == 0:
    return True
  else:
    return False


print(is_event(7))


#2 clean more
def is_event(num):
  if num % 2 == 0:
    return True
  return False


print(is_event(10))


#3 clean more
def is_event(num):
  return num % 2 == 0


print(is_event(11))