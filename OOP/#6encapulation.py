# Encapulation
'''Explain
Encapulation : idea of encapulation is binding of data and
               function that minipulate the data and we encapulate
               into one big object so that keep everything in this box
               that users or code or other machine can interact with.

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
player1.speak()
