# Program to convert fahrenheit to celsius.
# formula: C = (F-32)*5/9

fah = int(input("Enter the Fahrenheit value:"))
C = (fah-32)*(5/9)
print("Fahrenheit to Celsius:",C)

# print((int(input())-32)*(5//9)) ==> Float value
# print(int(((int(input())-32)*5)/9)) ==> Int value
