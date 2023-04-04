'''
Create PIN using Three given numbers
"Secure Assets Private Ltd", a small company that deals with lockers has 
recently started manufacturing digital locks which can be locked and unlocked 
using PINs (passwords). 
You have been asked to work on the module that is expected to generate PINs 
using three input numbers.
The three given input numbers will always consist of three digits each
i.e. each of them will be in the range >=100 and <=999.
Bellow are the rules for generating the PIN.
1. The PIN should made up of 4 digits.
2. The unit (ones) position of the PIN should be the least of the units position 
of the three numbers.
3. The tens position of the PIN should be the least of the tens position of the 
three input numbers.
4. The hundreds position of the PIN should be least of the hundreds position of 
the three numbers.
5. The thousands position of the PIN should be the max of all digits in the three 
input numbers.
input ----------> three numbers
constraints ----> all the numbers must be in the range of >=100 and <=999
output ---------> PIN value

'''

number1 = [int(i) for i in input().split()]
number2 = [int(i) for i in input().split()]
number3 = [int(i) for i in input().split()]

a = min(number1[2],number2[2],number3[2])
b = min(number1[1],number2[1],number3[1])
c = min(number1[0],number2[0],number3[0])
d = max(max(number1),max(number2),max(number3))
pin = d * 1000 + c * 100 + b * 10 + a
print("Pin Number:",pin)