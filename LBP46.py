'''
Magic Date
Program to read date, month and year from the user and check whether it is 
magic date or not. 
Here are the rules for magic date.
1) mm*dd is a 1-digit number that matches the last digit in YYYY
2) mm*dd is a 2-digit number that matches the last two digits in YYYY
3) mm*dd is a 3-digit number that matches the last three digits in YYY

input --------> three int values
output -------> true or false

'''
l = [i for i in input().split("-")]
test_md = int(l[0])* int(l[1])
final = str(l[2]).endswith(str(test_md))
print("Magic Date:",final)