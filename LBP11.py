'''
Sum of prime Digits 
Implement a program to calculate sum of prime digits present in the given 
number

'''

number = input("Enter the input number:")
result = sum([int(i) for i in list(number) if i in '2357'])
print("Sum of prime digits:",result)

