'''
Given an integer n,
If n is odd,print weird
if n is even ,in range 2-5,print Not Weird
if n is even,in range 6-20,print Weird
if n is even, range > 20,print Not Weird

'''

n = int(input("Enter the number n:"))
if n >= 1 and n <= 100:
    if n%2 != 0:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")