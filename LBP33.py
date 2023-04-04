'''
An e-commerce company plans to give their customers a discount for the 
newyears holiday. 
The discount will be calcualted on the basis of the bill amount of the order 
placed. 
The discount amount is the sum of all the odd digits in the customers total bill
amount. 
if no odd digits is present in the bill amount, then discount will be zero.
input ---------> the input consists of an integer bill amount, representing the 
customers total bill amount.
output -------> print an integer representing the dicount for the given total bill 
amount.

'''
# bill_amount = input("Enter the bill amount:")
# total = 0
# for each in bill_amount:
#     if each in '13579':
#         total += int(each)
# print("The discount for the given total bill amount:",total,"%")

print(sum([int(i) for i in list(input()) if int(i)%2!=0]))

