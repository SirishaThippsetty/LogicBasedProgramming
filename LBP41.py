'''
One Time Password
A company wishes to devise an order confirmation procedure. 
They plan to require an extra confirmation instead of simply auto-confirming 
the order at the time it is placed.
for this purpose, the system will generate one time password to be shared with 
the customer.
The customer who is placing the order has to enter the OTP to confirm the 
order. 
The OTP generated for the requested order ID, as the product of the digits in 
orderID. 
Write an algorithm to find the OTP for the OrderID.
input -----> an intger representing order id
output ----> an integer representing OTP
p=1;
while(n!=0)
{
d=n%10;
p=p*d;
n=n/10;
}
print p

'''
import math
input_data = input("Integer representing order id:")
result = math.prod([int(i) for i in input_data])
print("Integer representing OTP:",result)