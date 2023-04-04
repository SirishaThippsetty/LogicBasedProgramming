'''
Lucky Customer
An e-commerce website wishes to find the lucky customer who will be eligible 
for full value cash back. 
For this purpose,a number N is fed to the system. 
It will return another number that is calculated by an algorithm. 
In the algorithm, a seuence is generated, 
in which each number n the sum of the preceding number. 
initially the sequence will have two 1's in it. 
The System will return the Nth number from the generated sequence which is 
treated as the order ID. The lucky customer will be one who has placed that 
order. Write an alorithm to help the website find the lucky customer.

'''
def fib(n):
    if n==0 or n==1:
     return n
    else:
      return fib(n-1) + fib(n-2)

print(fib(int(input())))
