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

