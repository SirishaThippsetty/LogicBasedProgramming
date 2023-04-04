'''
Implement a program to calculate toggle case of each characters of a string
input -------> A String from user
constriant --> non-empty String
output ------> toggle case string
if A->a or a->A
A=65+32=97=a
a=97-32=65=A
'''
str1 = input("Enter the string:")
print(str1.swapcase())