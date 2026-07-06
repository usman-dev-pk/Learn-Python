# Search for number X in this tuple using loop
# data = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# rand_num = 9
# iterator = len(data) # 10
# x = 1
# while x < iterator:
#    impData = data[x]
#    rand_num == data[x]
#    print("The number is exists")
#    if(rand_num == impData):
    #   print("The numer", rand_num, "is available")
#    else:
#      print('This numer cannot exist.')
#    x += 1
# print(data[0])

#  For loop with range
num = 0
for i in range(1, 11):
#    x = num % 2 == 0
   if(num % 2 == 0):
      print(num)
   num = num + 1
#    print(i % 2 == 0)
