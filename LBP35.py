'''
The IT company "Soft ComInfo" has decided to transfer its messages through 
the N/W using 
new encryption technique. 
The company has decided to encrypt the data using the non-prime number 
concept. 
The message is in the form of a number and the sum of non-prime digits 
present in the message is used as the encryption key.
Write an algorithm to determine the encryption key.
input ------> The input consists of an integer numMsg representing the numeric 
form of the message.
output ------> print an integer representing the encryption key.
note: Digit 1 and 0 are considered as a prime number.
'''

print(sum([int(i) for i in input() if i in "4689"]))
