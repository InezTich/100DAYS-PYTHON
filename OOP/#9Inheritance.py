class Users:

  def sign_in(self):
    print("logged in")


class Wizard(Users):

  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'Attacking of power {self.power}')


class Archer(Users):

  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'Attacking with arrow: arrow left {self.num_arrows}')


wizard1 = Wizard("Maline", 50)
archer1 = Archer("Maline", 500)
wizard1.sign_in()

wizard1.attack()
archer1.attack()
