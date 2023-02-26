# OOP
# @classmethod and @staticmethod
'''Explain
@classmethod : idea of @classmethod is then we create @classmethod
               we need to provide the arguements (cls) by default
               cls stand for class after we can give other arguments
               like example (:1 below

@staticmethod: idea of @staticmethod is we can access to @staticmethod
               without cls just like example below
               

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

  @classmethod
  def adding_things(cls, num1, num2):
    return cls("Cloudea", num1 + num2)

  @staticmethod
  def adding_things2(num1, num2):
    return num1 + num2


player1 = PlayerCharectors("Cindy", 56)
print(player1.adding_things(2, 3))

# access @classmethod {1}

player3 = PlayerCharectors.adding_things(2, 3)
print(player3.age)
print(player3.name)
