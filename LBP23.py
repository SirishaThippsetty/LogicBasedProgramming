'''
A Special two digit number
A special two digit number is a number such that when 
the sum of its digits is added to the product of its digits, the result should be 
equal to the original two-digit number.
Implement a program to accept a two digit number and check whether it is a 
special two digit number or not.

'''
'''
Example: Consider the number 59.
Sum of digits = 5 + 9 = 14
Product of digits = 5 * 9 = 45
Sum of the sum of digits and product of digits = 14 + 45 = 59

12 ====> (1+2)+(1*2) =3+2=5 No
59 ====> (5+9)+(5*9) =14+45=59 Yes


'''

digit = input("Enter the number:")
a,b = int(digit[0]),int(digit[1])
result = (a+b) + (a*b)
print("Special 2 digit number" if result == int(digit) else ("Not a special number"))

# n=int(input())
# a=n%10
# b=(n//10)%10
# c=(a+b)+(a*b)
# print("Yes" if c==n else "No")
