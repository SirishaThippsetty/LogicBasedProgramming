'''
Sum of digits between two numbers
Create a function that sums the total number of digits between two numbers 
inclusive. 
for example, 
if the numbers are 19 and 22, then (1+9)+(2+0)+(2+1)+(2+2)=19.

'''
number1 = int(input("Enter the number 1:"))
number2 = int(input("Enter the number 2:"))
total = 0
for i in range(number1,number2+1):
    total += sum([int(j) for j in str(i)])
print(total)