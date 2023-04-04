'''
Implement a program to return First capital letter in a String

input -------> A string from the user
constraint --> non-empty string
output ------> First Capital letter
'''

string = input("Enter the string:")
lst = [i for i in string if i.isupper()]
print(lst[0])
