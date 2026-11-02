# Task #4
# Q1: Tuple Methods
# Scenario: Student Marks Record

# Creating a Tuple
marks = (85, 90, 75, 85, 95, 85, 80)

print("Original Tuple:", marks)


# 1. count() - Counts how many times a value occurs
result = marks.count(85)

print("\n1. count() Method:")
print("85 appears", result, "times")


# 2. index() - Returns the position of a specified value
result = marks.index(90)

print("\n2. index() Method:")
print("Position of 90:", result)


# Q2: Set Methods
# Scenario: Students enrolled in different courses

# Creating Sets
course_A = {"Ali", "Ahmed", "Usman", "Hassan"}
course_B = {"Usman", "Hassan", "Bilal", "Hamza"}


# 1. add() - Adds an element to the set
students = course_A.copy()
students.add("Zain")

print("\n1. add() Method:")
print(students)


# 2. clear() - Removes all elements from the set
students = course_A.copy()
students.clear()

print("\n2. clear() Method:")
print(students)


# 3. copy() - Returns a copy of the set
students = course_A.copy()

print("\n3. copy() Method:")
print(students)


# 4. difference() - Returns elements present in first set but not second
result = course_A.difference(course_B)

print("\n4. difference() Method:")
print(result)


# 5. difference_update() - Removes common elements from the original set
students = course_A.copy()
students.difference_update(course_B)

print("\n5. difference_update() Method:")
print(students)


# 6. discard() - Removes a specified element
students = course_A.copy()
students.discard("Ali")

print("\n6. discard() Method:")
print(students)


# 7. intersection() - Returns common elements between two sets
result = course_A.intersection(course_B)

print("\n7. intersection() Method:")
print(result)


# 8. isdisjoint() - Checks whether two sets have no common elements
result = course_A.isdisjoint({"Sara", "Ayesha"})

print("\n8. isdisjoint() Method:")
print(result)


# 9. pop() - Removes and returns an arbitrary element
students = course_A.copy()
removed_student = students.pop()

print("\n9. pop() Method:")
print("Removed Student:", removed_student)
print("Remaining Students:", students)


# 10. remove() - Removes a specified element
students = course_A.copy()
students.remove("Ahmed")

print("\n10. remove() Method:")
print(students)


# 11. union() - Combines elements of both sets
result = course_A.union(course_B)

print("\n11. union() Method:")
print(result)


# 12. update() - Adds elements of another set to the original set
students = course_A.copy()
students.update(course_B)

print("\n12. update() Method:")
print(students)