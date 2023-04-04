'''
Prime Number or Not
Write a program to check whether the given number is prime number or not. 

'''
n = int(input("Enter the input number:"))
count = 0
for i in range(2,n):
    if n % i == 0:
        count += 1
print("Prime number" if count == 0 else ("Not Prime number"))
