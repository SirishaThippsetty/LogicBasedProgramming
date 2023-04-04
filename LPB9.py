'''
Sum of even Digits
Implement a program to calculate sum of even digits present in the given
number


'''

print(sum([int(i) for i in list(input()) if int(i)%2==0]))
