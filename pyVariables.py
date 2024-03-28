# . Python Variables
x = 5
y = "John"
print(x)
print(y)

#  variables do not need to be declared with any
#  particular type
#  can even change type after they have been set

x = 4
#  x is of type int
x = "Sally"
x = "Molly"
#  x is now of type str
print(x)

#  Casting
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

#  Get the Type of the variable using the type() function
x = 5
y = "John"
print(type(x))
print(type(y))

#  Quotes
x = "John"
# is the same as
x = 'John'

#  Case sensitive
a = 4
A = "Sally"
#  A will not overwrite a
print(a)
print(A)

#  multiple values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#  one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
print("______________________________")
#  Unpacking a collection (extracting values into variables)
#  eg: Unpacking a list

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#  output variables
x = "Python is awesome"
print(x)

#  output multiple variables separated by a comma
x = "Python"
y = "is"
z = "awesome!"
print(x, y, z)

#  use the + operator to output multiple variables:
print(x + y + z)

#  using + operator for mathematical operations
x = 5
y = 10
print(x + y)

x = 5
y = "John"
#  print(x + y) - TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(x, y)

#  ============ GLOBAL VARIABLES ============================

#  assigning a global variable 'a'
a = "awesome!!!!!!"


# creating a function 'myfunc' to print local variable 'a'


def myfunc():
    a = "fantastic...!"
    print("Python is " + a)  # local variable a will be used


myfunc()

print("Python is " + a)  # global variable a will be used

#  'global' keyword


def myfunc1():
    global b
    b = "fantastic"


myfunc1()

print("python is " + b)

#  global keyword can also be used to change the global variable inside a function

c = "awesome"


def myfunc2():
    global c
    c = "fantastic"  # value of global variable c is changed to 'fantastic' here


myfunc2()

print("Python is " + c)
