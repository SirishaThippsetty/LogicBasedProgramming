# Ex: Read 3 int values and perform addition operation 

# First type

# x = int(input("Enter the number x:"))
# y = int(input("Enter the number y:"))
# z = int(input("Enter the number z:"))
# addition = x + y + z
# print("Sum of 3 numbers is:",addition)

# Second type

# print(sum([int(i) for i in input().split()]))

# LBP1: Check whether the number is odd or even?

number = int(input("Enter the number:")) # Version 1:

# if number >= 0:
#     if number % 2 == 0:
#         print("The given number",number,"is Even number")
#     else:
#         print("The given number",number,"is Odd number")
# else:
#     print("Invalid Number")

# Version 2:

print("Invalid" if number < 0 else ("Even Number" if number % 2 == 0 else "Odd Number"))