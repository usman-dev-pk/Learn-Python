first_number = int(input("Enter first number: "))
sec_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

if first_number > sec_number and first_number > third_number:
    print("The largest number is:", first_number)

elif sec_number > first_number and sec_number > third_number:
    print("The largest number is:", sec_number)

elif third_number > first_number and third_number > sec_number:
    print("The largest number is:", third_number)