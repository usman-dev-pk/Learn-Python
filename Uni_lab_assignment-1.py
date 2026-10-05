# Task 1: Hospital Patient Card
patient_name = "Usman"
patient_id = 101
age = 20
ward = "Emergency"

print(patient_name, patient_id, age, ward)



# Task 2: Bank Account
account_holder_name = "Usman"
balance = 5000

balance = balance + 2000
print(account_holder_name, "has balance:", balance)

balance = balance - 1500
print(account_holder_name, "has balance:", balance)




# Task 3: Fix the Variable Names
# Corrected variable names
first_name = "Usman"
last_name = "Jutt"
my_age = 21

print(first_name, last_name, my_age)




# Task 4: Many Values, One Line
subject1, subject2, subject3 = "Python", "Physics", "Islamic Studies"

print(subject1)
print(subject2)
print(subject3)




# Task 5: One Value, Many Variables
team_a = team_b = team_c = 0

print(team_a, team_b, team_c)

team_b = 4

print(team_a, team_b, team_c)





# Task 6: Swap Two Winners
first_place = "Usman"
second_place = "Zain"
print(first_place, second_place)
first_place, second_place = second_place, first_place

print(first_place, second_place)




# Task 7: Printing Two Ways
city = "Lahore"
country = "Pakistan"
students = 120

print(city + " " + country)
print(city, country, students)





# Task 8: Local vs. Global
message = "I am global"

def show():
    message = "I am local"
    print(message)

show()
print(message)





# Task 9: Parking Lot Counter
cars_parked = 0

def park_car():
    global cars_parked
    cars_parked = cars_parked + 1

def leave_car():
    global cars_parked
    cars_parked = cars_parked - 1

park_car()
park_car()
park_car()
park_car()
park_car()

leave_car()
leave_car()

print(cars_parked)





# Task 10: Cricket Scoreboard
team_name = "Pakistan"
runs = 0
wickets = 0
overs = 0

print(team_name, runs, wickets, overs)

def hit_six():
    global runs
    runs = runs + 6

def wicket():
    global wickets
    wickets = wickets + 1

hit_six()
hit_six()
hit_six()

wicket()
wicket()

print(team_name, runs, wickets, overs)