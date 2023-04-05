'''
Next Prime
Given an integer, 
create a function that returns the next prime. 
If the number is prime, return the number itself.

'''

def is_prime(n):
    if n > 0:
        fact = 0
        for i in range(1,n):
            if n % i == 0:
                fact += 1
        return fact == 1


number = int(input("Enter the number:"))
while True:
    if is_prime(number):
        print(number)
        break
    number = number + 1
