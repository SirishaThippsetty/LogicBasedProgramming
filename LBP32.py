'''
Program to count number of special characters and white spaces in a given 
string.
input --------> A string from the user
constraint ---> non-empty string
output -------> number of special characters
a-z
A-Z
0-9
if(() or () or ())
continue
else

'''
string = input()
total = 0
for each in string:
    if not each.isalnum():
        total += 1
print("No of special characters:",total)