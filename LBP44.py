'''
There is a great war between the even and odd numbers. 
Many numbers already lost thier life in this war and its your task to end this. 
You have to determine which group sums larger. the even, or the odd, the 
larger group wins.
Create a function that takes an array of integers , sums the even and odd 
numbers seperately, 
then return the difference between sum of even and odd numbers.
input --------> number and array elements
constraint ---> no
output -------> difference between sum of even and odd numbers
'''
number = int(input("Enter the number:"))
array = list(map(int,input("Enter the array elements:").split()))
even_sum = 0
odd_sum = 0
for i in array:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"The difference between sum of even and odd numbers is {even_sum - odd_sum}")