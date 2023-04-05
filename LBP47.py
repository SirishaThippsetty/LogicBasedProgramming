'''
Oddish or Evenish
Create a function that determines whether a number is Oddish or Evenish. 
A number is Oddish if the sum of all of its digits is Odd, 
and number is Evenish if the sum of all of its digits is even, 
if a number is Oddish return Oddish else return Evenish.
input ----------> a number
constraint -----> n>0
output ---------> Oddish or Evenish
sum of digits % 2 ==0 then Evenish else Oddish


'''

number = input("Enter the number:")
a = int(number)
if a > 0:
    total = 0
    for each in number:
        i = int(each)
        total += i
else:
    print("It is negative number")
if total % 2 == 0:
    print("Evenish")
else:
    print("Oddish")