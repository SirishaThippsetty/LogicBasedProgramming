'''
Sum of Digits divisible by 3
Implement a program to calculate sum of digits that are divisible by 3 in the 
given number


'''
number = input("Enter the number:")
# result = sum([int(i) for i in list(number) if int(i)%3 == 0])
result = sum([int(i) for i in list(number) if i in '369'])
print("Sum of Digits divisible by 3:",result)