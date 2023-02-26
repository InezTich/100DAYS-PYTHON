# OOP
'''Explain
__init__ : is a spcial method or often call constructor 
           method or init method, this is automatically call
           anytime we instanciate object from class.
self     : refer to class its self

The way to access class object attribute need to call self.membership or
call the class name for access all property

'''


class PlayerCharectors:
  # class object attribute
  membership = True

  def __init__(self, name, age):
    if (self.membership):  # or can use (PlayerCharectors.membership)
      self.name = name  # attribute or property
      self.age = age

  def run(self):
    print("run")
    return "done"


player1 = PlayerCharectors("Cindy", 56)
player2 = PlayerCharectors("Tome", 88)
print(player1)  # return the object in memory location
print(player1.name, player1.age)
print(player2.name, player2.age)

print(player1.run())

player2.attack = 50

print(player2.attack)
# print(player1.attack)  # get error because player1 have no attribute attack
