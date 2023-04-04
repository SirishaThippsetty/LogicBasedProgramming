'''
Sum of odd Digits
Implement a program to calculate sum of odd digits present in the given
number

'''

print(sum([int(i) for i in list(input()) if int(i)%2!=0]))