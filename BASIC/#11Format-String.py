# Formatted String

name = 'Johnny'
age = 56

print('Hi '+ name + '. You are'+ str(age) + ' year old.')

print(f'Hi {name}, You are {age} year old.')

print("Hi {} You are {} year old.".format(name,age))

print(f"Hi {name}, You are {age} year old.")

print(f'hi {1} You are {0} year old!'.format(name='Peer',age=34))