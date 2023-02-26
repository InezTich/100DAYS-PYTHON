# private and public variable
'''Explain
private and public :  idea is still modify it

'''


class PlayerOfMeme:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    print("Run")

  def speak(self):
    print(f"My name is {self.name}, and i am {self.age} year old.")


player1 = PlayerOfMeme("Massa", 34)
player1.name = "!!!!!"
player1.speak = "BOOOO"

print(player1.speak)
