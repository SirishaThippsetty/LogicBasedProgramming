'''
Celsius to Fahrenheit
Create a function/method to convert celsius to fahrenheit.

formula: F=(C*9/5)+32

'''

# print((int(input())*9//5)+32)

def Fahrenheit(celsius):
    return (celsius *(9/5)) + 32

number = int(input("Enter the Celsius:"))
print(Fahrenheit(number))