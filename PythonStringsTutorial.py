#  Quotes (single and double quotes can both be used)
print("Hello")
print('Hello')

#  assigning string to a variable
a = "Hello"
print(a)

#  Multiline String using double or single quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print('-----------------------------')

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

print('-----------------------------')

# STRINGS ARE ARRAYS
a = "Hello World"
print(a[1])  # 'e'

print('-----------------------------')

#  Looping through a String (using for loop just like an array)
for x in "banana":
    print(x)

print('-----------------------------')

#  Get the length of a string
a = "Hello World"
print(len(a))

print('-----------------------------')

#  Check String
#  To check if a certain phrase or character is present in a string, we can use the keyword 'in'
txt = "The best things in life are free"
print("free" in txt)

# or use an 'if' statement
if "free" in txt:
    print("Yes, 'free' is present.")

print('-----------------------------')

#  Check if a string or character is "NOT" present in string
print("expensive" not in txt)

# use it in an 'if' statement
if "expensive" not in txt:
    print("Not in txt")

print('-----------------------------')
#  slicing strings (start_index(included) : end_index (not incl)
b = "Hello, World!"
print(b[2:5])

#  slice from the start (blank : end_index(not incl)
print(b[:5])

#  slice to the end
print(b[2:])
print('-----------------------------')

#  NEGATIVE INDEXING
# to start the slice from the end of the string:
# start_index (5th from the end) to end_index (start excluding characters from the end by counting from 1 to end_index)
print(b[-5:-2])  # orl
print(b[-5:-3])  # or

print('-----------------------------')
#  -------- Modify String -----------

#  Upper Case
a = " Hello Python "
print(a.upper())  # _HELLO PYTHON_
# lower case
print(a.lower())  # _hello python_
# remove whitespace with strip() function
print(a.strip())  # Hello Python

# replace()
print(a.replace("P", "H"))  # Hello Hython

#  Split a string by a delimiter
a = "Hello World!"
print(a.split(","))  # ['Hello', 'World!']
b = ",Hello, ,World,!,"
print(b.split(","))  # ['', 'Hello', ' ', 'World', '!', '']

#  String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#  String concatenation
age = 29
txt = "My name is Fouzia, I'm "
# print(age + txt)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(txt.format(age))

#  format() takes unlimited arguments
quantity = 3
item_no = 343
price = 20.50
my_order = "I want {} pieces of item {} for {} dollars."

print(my_order.format(quantity, item_no, price))
#  index the arguments into the text using {0}

my_order_1 = "I want to pay {2} dollars for {0} pieces of item {1}"

print(my_order_1.format(quantity, item_no, price))

#  Escape characters
txt_1 = "Hello, this is \"Vikings\" and welcome to our land"
print(txt_1)

#  capitalize():
#  Upper case the first letter in the string (turns everything else to lower case)
txt = "hi and welcome to the world of my creation"
x = txt.capitalize()
print(x)

txt_2 = "python is FUN!"
y = txt_2.capitalize()
print(y)

txt_3 = "36 is your roll number"  # in this case, the first letter is a number so the string remains unchanged
z = txt_3.capitalize()
print(z)

# centre():
a = "banana"
x = a.center(20, "0")
print(x)

#  count():
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
y = txt.count("apple", 0, 25)
z = txt.count("apple")
print(x)
print(y)
print(z)

#  encode():
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
