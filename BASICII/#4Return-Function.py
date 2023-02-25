# Return keyword
'''
return keyword will automatic exit code
'''


def cal_two_number(n1, n2):
  return n1 + n2


def sum(s1, s2):
  return s1 + s2


total = cal_two_number(1, 5)
print(total)
print(sum(10, total))


def funct_1(num1, num2):

  def funct_2(n1, n2):
    return n1 + n2

  return funct_2(num1, num2)


grand_total = funct_1(2, 3)
print(grand_total)
