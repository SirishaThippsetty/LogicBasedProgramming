'''
An e-Commerce company plans to give thier customers a discount for the 
newyears holiday. The discount will be calcualted on the basis of the bill 
amount of the order place. The discount amount is the productof the sum of 
all odd digits and the sum of all even digits of the customers total bill amount.
input ----> an integer bill amount, representing the total bill amount of the 
customer.
output ---> print an inteer representing the discount amount for the given total 
bill.

'''
# bill_amount = input("Enter the bill amount: ")
# total_bill = bill_amount
# odd_sum = 0
# even_sum = 0
# for each in bill_amount:
#     if int(each)%2 == 0:
#         even_sum += int(each)
#     else:
#         odd_sum += int(each)
# result = odd_sum * even_sum
# print("Discount for the given bill:",result)

n=int(input())
se=0
so=0
while n!=0:
 d=n%10
 if d%2==0:
        se=se+d
 else:
      so = so + d
 n=n//10
print(so*se)
  
 

