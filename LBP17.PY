'''
Paliandrome Number
Program to check whether the given number is paliandrome or not

'''
number = input("Enter the number:")
result = "Yes" if number == number[::-1] else "No"
print(result)