'''
Valid Palindrome
Given a string, 
determine if it is a Palindrome string or not. 
A String is Palindrome if it is equal to reverse of the original string

'''
string = input("Enter the input string:")
a = string.lower()
print("Palindrome String" if a == a[::-1] else "Not Palindrome String")