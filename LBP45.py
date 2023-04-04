'''
Perfect Number
Create a function that tests whether or not an integer is a perfect number. 
A perfect number is a number that can be written as sum of its factors. 
(equal to sum of its proper divisors) excluding the number itself.
input ------> a number from the user
constraint -> n>0
output -----> true or false
4 ===> 1,2,4 ===> 1,2 ===> 1+2=3
6 ===> 1,2,3,6 => 1,2,3 => 1+2+3=6

'''
n = int(input("Enter the number:"))
total = 0
for i in range(1,n):
    if n%i == 0:
        total += i
print("True" if total == n else "False")