'''
Niven Number
Write a program to accept a number and check and display whether it is a 
Niven Number or not.
Niven Number is that a number which is divisible by its sum of digits

'''
number = int(input("Enter the number:"))
temp = number
total = 0
while number != 0:
    d = number % 10
    total += d
    number = number // 10
print("Yes,it is Niven number" if temp%total == 0 else ("No,it is not Niven number"))

'''
Enter the number:126 ==> 1+2+6 = 9 126/9 = 14
Yes,it is Niven number

Enter the number:524
No,it is not Niven number

'''