'''
Jackson, a math student, is developing an application on prime numbers. for 
the given two integers on the display of the application, the user has to identify 
all the prime numbers within the given range (including the given values). 
afterwards the application will sum all those prime numbers. Jackson has to 
write an algorithm to find the sum of all the prime numbers of the given range.
Write an algorithm to find the sum of all the prime numbers of the given range.
input -----> two space sepearted integers RL and RR.
output ----> sum of the prime numbers between RL and RR.
'''
def isprime(n):
     f=0
     for i in range(1,n+1):
            if n%i == 0:
                 f += 1
     return f == 2

   
n1=int(input())
n2=int(input())
s=0
for i in range(n1,n2+1):
 if isprime(i):
        s += i

print(s)