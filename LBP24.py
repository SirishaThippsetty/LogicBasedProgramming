'''
Sum of even numbers
Implement a program to find sum of even number between x and y both are 
inclusive

input -----> two int values
output ----> sum of even numbers between x and y
'''
x = int(input("Enter the value x:"))
y = int(input("Enter the value y:"))
total = 0
for i in range(x,y+1):
    if i % 2 == 0:
        total += i
print("Sum of even numbers between",x,"and",y,"is",total)