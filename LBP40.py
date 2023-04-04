'''
A company wishes to transmit data to another server. 
The data consists of numbers only. 
To secure the data during transmission, they plan to reverse the data during 
transmission, 
they plan to reverse the data first.
Write an algorithm to reverse the data first
input -----> an integer data, representing the data to be transmitted
output ----> print an integer representing the given data in reverse form
'''
def reverse_data(data):
    rev_data = 0
    while data > 0:
        rev_data = rev_data * 10 + data % 10
        data = data // 10
    print(rev_data)
reverse_data(123456789)

# input_data = input("Enter the data:")
# print(input_data[::-1])