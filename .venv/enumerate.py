#The enumerate() method adds counter to an iterable and returns it (the enumerate object).
#start is optional. enumerate() starts counting from this number. If start is omitted, 0 is taken as start.
grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)