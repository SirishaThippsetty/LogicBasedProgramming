'''
Duck Number
Program to read a number and check whether it is duck number or not.

'''

'''
Hint: A duck number is a number which has zeros present in it, 
but no zero present in the begining of the number.
If any number begin with 0 then it is said to be octal

1234 ----> No
1203 ----> Yes
5026 ----> Yes
1000 ----> Yes
4444 ----> No

'''
number = input("Enter the number:")
# count = 0
# for each in number:
#     if int(each) == 0:
#         count += 1
# print("Yes" if count > 0 else "No")
print("Yes" if "0" in number else "No")