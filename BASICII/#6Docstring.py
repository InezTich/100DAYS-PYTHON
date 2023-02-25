# Docstring
'''
docstring is use to show info when you use some function but you don't know how many arguement needed, just call function and hover on it those info that we write docstring in function will appear.
'''


def show_info(name, age):
  '''
  Info: this function take two argument (name,age)
  '''
  print(f"Hellooooo {name}, you are {age} year old.")


show_info('Harry Potter', 45)

print(show_info.__doc__)
