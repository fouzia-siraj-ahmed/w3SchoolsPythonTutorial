import random

#  Python Data Types
x = 5
print(x, type(x))  # <class 'int'>

x = "Hello World"
print(x, type(x))  # <class 'str'>

x = 20.5
print(x, type(x))  # <class 'float'>

x = 1j
print(x, type(x))  # <class 'complex'>

x = ["apple", "banana", "cherry"]
print(x, type(x))  # <class 'list'>

x = ("apple", "banana", "cherry")
print(x, type(x))  # <class 'tuple'>

x = range(6)
print(x, type(x))  # <class 'range'>

x = {"name": "John", "age": 36}
print(x, type(x))  # <class 'dict'>

x = {"apple", "banana", "cherry"}
print(x, type(x))  # <class 'set'>

x = frozenset({"apple", "banana", "cherry"})
print(x, type(x))  # <class 'frozenset'>

x = True
print(x, type(x))  # <class 'bool'>

x = b"Hello"
print(x, type(x))  # <class 'bytes'>

x = bytearray(5)
print(x, type(x))  # <class 'bytearray'>

x = memoryview(bytes(5))
print(x, type(x))  # <class 'memoryview'>

x = None
print(x, type(x))  # <class 'NoneType'>

#  Setting specific data type
x = str("Hello World")

x = int(20)
print(x)  # 20

x = float(20.5)
print(x)  # 20.5

x = complex(1j)
print(x)  # 1j

x = list(("apple", "banana", "cherry"))
print(x)  # ['apple', 'banana', 'cherry']

x = tuple(("apple", "banana", "cherry"))
print(x)  # ('apple', 'banana', 'cherry')

x = range(6)
print(x)  # range(0, 6)

x = dict(name="John", age=36)
print(x)  # {'name': 'John', 'age':36}

x = set(("apple", "banana", "cherry"))
print(x)  # {'banana', 'cherry', 'apple'}
#  note the set values are not ordered


x = frozenset(("apple", "banana", "cherry"))
print(x)  # frozenset({'banana', 'cherry', 'apple'})

x = bool(5)
print(x)  # True

x = bytes(5)
print(x)  # b'\x00\x00\x00\x00\x00\x00'

x = bytearray(5)
print(x)  # bytearray(b'\x00\x00\x00\x00\x00\x00')

x = memoryview(bytes(5))
print(x)  # <memory at 0x100410c40>

#  PYTHON NUMERICS

x = 1  # int
y = 2.8  # float
z = 1j  # complex
print(type(x))
print(type(y))
print(type(z))

#  int - integers
x = 1
y = 35863487563498537458
z = -2348938947

print(type(x))
print(type(y))
print(type(z))

#  float

x = 1.10  # 1.1
y = 1.0  # 1.0
z = -35.98  # -35.98

a = 35e3  # 35000.0
b = 12E4  # 120000.0
c = -87.7e100  # -8.77e+101

print(x, type(x))
print(y, type(y))
print(z, type(z))
print(a, type(a))
print(b, type(b))
print(c, type(c))

#  complex
x = 3 + 5j  # (3+5j)
y = 5j  # 5j
z = -5j  # (-0-5j)

print(x, type(x))
print(y, type(y))
print(z, type(z))

#  type conversion
x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b =int(y)

# convert from int to complex:
c = complex(x)

print(a)  # 1.0
print(b)  # 2
print(c)  # (1+0j)

print(type(a))  # <class 'float'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'complex'>

#  random number (using built-in module 'random')
#  import random (see line 1 since import statements must be at the top of the page)

print(random.randrange(1, 10))  # random number between 1 and 10. Example: 7
print("**********************")
#  Python Casting
#  int()
x = int(1)  # x will be 1
y = int(2.8)  # y will be a 2
z = int("3")  # z will be 3

print(x)
print(y)
print(z)
print("**********************")

#  float()
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(x)
print(y)
print(z)
print(w)
print("**********************")
#  str()
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print(x)
print(y)
print(z)