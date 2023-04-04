'''
Christmas offer
An e-commerce company plans to give their customers a special discount for 
the Christmas, 
they are planning to offer a flat discount. 
The discount value is calculated as the sum of all prime digits in the total bill 
amount.
Write an algorithm to find the discount value for the given total bill amount.

'''

'''
input ----> the input consists of an integer order value representing the total 
bill amount
output ---> print an integer representing discount value for the given total bill 
amount

12500.00 ====> 2+5=7%
12540.00 ====> 2+5=7%
sum of prime digits

'''

# print(sum([int(i) for i in list(input()) if i in '2357']))


bill = input("Enter the bill amount:")
list_1 = [int(n) for n in bill if n in '2357']
print("Discount Value:",sum(list_1),"%")
