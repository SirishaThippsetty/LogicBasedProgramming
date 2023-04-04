'''
Check whether Leap year or not

conditions:
1. If it is not a century year and divisible by 4
2. If it is a century year and divisble by 400

'''

# year = int(input("Enter the year:"))

# # condition 1 ==> not a century year ==> year%100 != 0
# # condition 2 ==> Century year ==> year % 100 == 0

# if (year%100 != 0 and year % 4 == 0) or (year%100 == 0 and year % 400 == 0):
#     print("Given year",year,"is a Leap year")
# else:
#     print("Given year",year,"is not Leap year")

import calendar
print(calendar.isleap(int(input())))