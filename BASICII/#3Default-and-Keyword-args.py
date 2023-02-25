# Positional Parameters
'''docs
- positional argument are required to be in the proper position
- keyword arguments sometime call default parameters
- default parameters make you easily control your logic code when
  you call the function forget it's arguments.
'''


def say_hello(name, emoji):
  print(f'Hello {name} {emoji}')


# positional arguments
say_hello("Andrie", '😍')  # Andrie😍
say_hello('😎', "Emma")  # 😎Emma

# keyword arguments
say_hello(emoji='😍', name='Maisa')


# default parameters
def greeting_users(name='Bruno', emoji='😎'):
  print("Greeting Users")
  print(f'Hello {name}{emoji}')


# invoke defualt parameters
greeting_users()
greeting_users("Harry Poter", '😎')
