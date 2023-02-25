# Function Python


def say_hello():
  print("Helloooooo")


say_hello()

pictures = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0,
                                    0], [0, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]]


def show_tree():
  for image in pictures:
    for pixel in image:
      if (pixel):
        print('*', end="")
      else:
        print(' ', end="")
    print('')


show_tree()
show_tree()
show_tree()
