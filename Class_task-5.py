# Q1: Solve All Python Dictionary Methods
# Scenario: Student Management System

# Original Student Dictionary
student = {
    "name": "Ali",
    "age": 20,
    "course": "Computer Science",
    "marks": 85
}

print("Original Student Record:")
print(student)


# 1. clear() - Removes all elements from dictionary
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

student.clear()

print("\n1. clear() Method:")
print(student)


# 2. copy() - Returns a copy of dictionary
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

new_student = student.copy()

print("\n2. copy() Method:")
print(new_student)


# 3. fromkeys() - Creates dictionary with specified keys and value
keys = ["Ali", "Ahmed", "Usman"]

students = dict.fromkeys(keys, 0)

print("\n3. fromkeys() Method:")
print(students)


# 4. get() - Returns the value of specified key
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

result = student.get("marks")

print("\n4. get() Method:")
print(result)


# 5. items() - Returns all key-value pairs
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

result = student.items()

print("\n5. items() Method:")
print(result)


# 6. keys() - Returns all dictionary keys
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

result = student.keys()

print("\n6. keys() Method:")
print(result)


# 7. pop() - Removes element with specified key
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

student.pop("age")

print("\n7. pop() Method:")
print(student)


# 8. popitem() - Removes the last inserted key-value pair
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

student.popitem()

print("\n8. popitem() Method:")
print(student)


# 9. setdefault() - Returns value or inserts a new key
student = {
    "name": "Ali",
    "marks": 85
}

student.setdefault("grade", "A")

print("\n9. setdefault() Method:")
print(student)


# 10. update() - Updates dictionary with new values
student = {
    "name": "Ali",
    "marks": 85
}

student.update({"marks": 95})

print("\n10. update() Method:")
print(student)


# 11. values() - Returns all dictionary values
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

result = student.values()

print("\n11. values() Method:")
print(result)