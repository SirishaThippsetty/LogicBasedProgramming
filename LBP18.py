'''
Check Birth Day
Lisa always forgets her birthday which is on th 5th July. 
So develop a function/method which will be helpful to remember her birthday.
The function/method checkBirthday return an integer 1, if it is her birthday 
else return 0. 
the function/method checkBirthday accepts two arguments.
Month, a string representing the month of her birth and day, an integer 
representing the data of her birthday.

input -----------> month & day
output ----------> 1 or 0
'''
month = input("Enter the month:")
day = int(input("Enter the day:"))
if month == "july" and day == 5:
    print("1")
else:
    print("0")