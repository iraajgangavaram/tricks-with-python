#In Python, an anonymous function is a function that is defined without a name. While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
# The following example is not recommended in Python if function is simple
def add(x, y):
  return x + y
print(add(2, 3))

# In such cases, it is advisable to use the lambda function instead of the def function
add = lambda x, y: x + Y
print(add(2, 3))