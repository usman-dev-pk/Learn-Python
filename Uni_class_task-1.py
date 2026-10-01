# # TASK # 01
# # Python Basics


# # Q1: Create a variable and check whether pip is working or not

name = "Usman"
print("Variable value:", name)

# Pip is properly working on my system.

# # Q2: Store multiple integer values and print their sum

num1 = 5
num2 = 10
num3 = 15

total = num1 + num2 + num3

print("Sum of numbers:", total)


# # Q3: Check datatype and perform type conversions

# # Create a variable

value = 10

print("Q3 - Datatype of value:", type(value))

# int to string
integer_value = 25
string_value = str(integer_value)

print("Int to String:", string_value)
print("Datatype:", type(string_value))

# string to int
string_number = "50"
integer_number = int(string_number)

print("String to Int:", integer_number)
print("Datatype:", type(integer_number))

# float to int
float_value = 25.75
integer_value = int(float_value)

print("Float to Int:", integer_value)
print("Datatype:", type(integer_value))

# int to float
integer_value = 20
float_value = float(integer_value)

print("Int to Float:", float_value)
print("Datatype:", type(float_value))



# # Q4: Global and Local Scope

a = "I am Global"


def my_function():
    x = "I am Local"

    print("Local Area:")
    print("a =", a)
    print("x =", x)


my_function()

print("Global Area:")
print("a =", a)


# Q5: Use Global keyword

a = "I am Global"
x = "I am Local"


def my_function():
    global x

    x = "Before I was Local. Now, I am Global"

    print("Local Area:")
    print("a =", a)
    print("x =", x)


my_function()



# # Q6: Create a string: Ali's a good boy

sentence = "Ali's a good boy"

print("Q6:", sentence)


# # Q7: Comments in Python

# # This is a single-line comment.

# """
# This is a
# multi-line comment.
# It can contain multiple lines.
# """

