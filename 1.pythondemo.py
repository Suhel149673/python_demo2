print("hello world")
# Addition
result_add = 5 + 3
print("Addition:", result_add)

# Subtraction
result_sub = 7 - 4
print("Subtraction:", result_sub)

# Multiplication
result_mul = 2 * 6
print("Multiplication:", result_mul)

# Division
result_div = 10 / 2
print("Division:", result_div)

#modulus
result_mod = 5%1
print("modulus:" , result_mod)

#even or odd
number = 7
if number%2==0:
    print("number is even")
else:
    print("number is odd")

#factorial using function
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num =5
print("factorial of" , num ,"is",factorial(num))

#reversing a string
def reverse_string(string):
    return string[::-1]

input_string = "Python"
reversed_string = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)

#string operations examples
#string concatination or addition
str1="hello"
str2="world"
result = str1+ " "+ str2
print(result)

#string length
str1= "Python is fun to learn"
length = len(str1)
print(length)

#string slicing
str1="python programming is learning by suhel"
length = len(str1)
print(length)
print(str1[15:38])

# Creating Strings
my_string = 'Hello, World!'
another_string = "Python is awesome!"
multi_line = """This
is a 
multi-line
string"""

# Accessing Characters
print(my_string[0])  # Output: 'H'
print(my_string[7])  # Output: 'W'
print(my_string[3:7])  # Output: 'lo, '

# String Methods
print(my_string.lower())  # Output: 'hello, world!'
print(my_string.upper())  # Output: 'HELLO, WORLD!'
print(my_string.find('World'))  # Output: 7
print(my_string.replace('Hello', 'Hi'))  # Output: 'Hi, World!'
print(my_string.split(','))  # Output: ['Hello', ' World!']
print('-'.join(['Hello', 'World']))  # Output: 'Hello-World'

# String Formatting
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

# String Concatenation
greeting = "Hello"
audience = "World!"
combined = greeting + " " + audience
print(combined)  # Output: 'Hello World!'
