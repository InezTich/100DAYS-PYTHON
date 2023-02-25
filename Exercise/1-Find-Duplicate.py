# Exercise: Check for duplicate in list

some_list = ['a', 'b', 'c', 'b', 'd', 'e', 'm', 'n', 'n']

duplicated = []

for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicated:
      duplicated.append(value)

print(duplicated)
