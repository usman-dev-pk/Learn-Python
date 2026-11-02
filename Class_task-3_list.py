# Task #3
# Q1: Python Programming Questions


# I. Simple Guessing Game
# Scenario: User has to guess a number between 1 and 100

# import random

# secret_number = random.randint(1, 100)

# guess = int(input("Guess a number between 1 and 100: "))

# while guess != secret_number:

#     if guess < secret_number:
#         print("Too low! Try again.")

#     else:
#         print("Too high! Try again.")

#     guess = int(input("Enter your guess again: "))

# print("Congratulations! You guessed the correct number.")


# II. Check if Number is Greater Than 10

number = int(input("\nEnter a number: "))

if number > 10:
    print("The number is greater than 10.")

else:
    print("The number is not greater than 10.")


# III. Create a List of First Five Prime Numbers

prime_numbers = [2, 3, 5, 7, 11]

print("\nFirst Five Prime Numbers:")
print(prime_numbers)


# IV. Create an Instance of Car Class and Display Details

class Car:

    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    def display_details(self):
        print("Car Brand:", self.brand)
        print("Car Color:", self.color)
        print("Car Model:", self.model)


my_car = Car("Toyota", "Black", "Corolla")

print("\nCar Details:")
my_car.display_details()


# V. Append Number 7 to the List

numbers = [1, 2, 3, 4, 5, 6]

numbers.append(7)

print("\nList After Appending 7:")
print(numbers)

# Q2: Python List Methods
# Scenario: Student Marks Management System


# Original List
marks = [85, 90, 75, 85, 95]

print("Original List:", marks)


# 1. append() - Adds an element at the end
marks = [85, 90, 75]
marks.append(100)

print("\n1. append():")
print(marks)


# 2. clear() - Removes all elements
marks = [85, 90, 75]
marks.clear()

print("\n2. clear():")
print(marks)


# 3. copy() - Returns a copy of the list
marks = [85, 90, 75]
new_marks = marks.copy()

print("\n3. copy():")
print(new_marks)


# 4. count() - Counts occurrences of a value
marks = [85, 90, 85, 75, 85]
result = marks.count(85)

print("\n4. count():")
print("85 appears", result, "times")


# 5. extend() - Adds elements of another list
marks = [85, 90, 75]
marks.extend([95, 100])

print("\n5. extend():")
print(marks)


# 6. index() - Returns the position of a value
marks = [85, 90, 75, 95]
result = marks.index(75)

print("\n6. index():")
print("Position of 75:", result)


# 7. insert() - Adds an element at a specific position
marks = [85, 90, 75]
marks.insert(1, 100)

print("\n7. insert():")
print(marks)


# 8. pop() - Removes an element at a specific position
marks = [85, 90, 75, 95]
marks.pop(2)

print("\n8. pop():")
print(marks)


# 9. remove() - Removes a specified value
marks = [85, 90, 75, 95]
marks.remove(90)

print("\n9. remove():")
print(marks)


# 10. reverse() - Reverses the list
marks = [85, 90, 75, 95]
marks.reverse()

print("\n10. reverse():")
print(marks)


# 11. sort() - Sorts the list in ascending order
marks = [85, 90, 75, 95, 80]
marks.sort()

print("\n11. sort():")
print(marks)