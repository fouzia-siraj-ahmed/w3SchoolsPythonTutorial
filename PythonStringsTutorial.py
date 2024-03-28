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
