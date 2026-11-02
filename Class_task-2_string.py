# Q2: Python String Methods
# Scenario: Student Information System


# 1. capitalize() - Converts first character to uppercase
text = "hello world"
print("1. capitalize():", text.capitalize())


# 2. casefold() - Converts string into lowercase
text = "HELLO WORLD"
print("2. casefold():", text.casefold())


# 3. center() - Returns a centered string
text = "Ali"
print("3. center():", text.center(10, "*"))


# 4. count() - Counts occurrences of a value
text = "hello hello world"
print("4. count():", text.count("hello"))


# 5. encode() - Returns encoded version of string
text = "Hello"
print("5. encode():", text.encode())


# 6. endswith() - Checks if string ends with specified value
text = "Hello World"
print("6. endswith():", text.endswith("World"))


# 7. expandtabs() - Sets tab size
text = "Name\tAge"
print("7. expandtabs():", text.expandtabs(10))


# 8. find() - Finds position of specified value
text = "Hello World"
print("8. find():", text.find("World"))


# 9. format() - Formats specified values
text = "My name is {} and my age is {}"
print("9. format():", text.format("Ali", 20))


# 10. format_map() - Formats values using a dictionary
text = "My name is {name} and my age is {age}"
student = {"name": "Ali", "age": 20}
print("10. format_map():", text.format_map(student))


# 11. index() - Finds position of specified value
text = "Hello World"
print("11. index():", text.index("World"))


# 12. isalnum() - Checks if all characters are letters or numbers
text = "Ali123"
print("12. isalnum():", text.isalnum())


# 13. isalpha() - Checks if all characters are alphabets
text = "Hello"
print("13. isalpha():", text.isalpha())


# 14. islower() - Checks if all letters are lowercase
text = "hello"
print("14. islower():", text.islower())


# 15. isnumeric() - Checks if all characters are numeric
text = "12345"
print("15. isnumeric():", text.isnumeric())


# 16. isupper() - Checks if all letters are uppercase
text = "HELLO"
print("16. isupper():", text.isupper())


# 17. join() - Joins elements of an iterable
names = ["Ali", "Ahmed", "Usman"]
separator = ", "
print("17. join():", separator.join(names))


# 18. lower() - Converts string into lowercase
text = "HELLO WORLD"
print("18. lower():", text.lower())


# 19. lstrip() - Removes spaces from the left side
text = "   Hello World"
print("19. lstrip():", text.lstrip())


# 20. replace() - Replaces specified value
text = "Hello Ali"
print("20. replace():", text.replace("Ali", "Usman"))


# 21. rsplit() - Splits string from the right side
text = "Ali,Ahmed,Usman"
print("21. rsplit():", text.rsplit(",", 1))


# 22. upper() - Converts string into uppercase
text = "hello world"
print("22. upper():", text.upper())