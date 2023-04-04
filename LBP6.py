'''
For each of the 6 coffee cups I buy, I get a 7th cup free. In total, I get 7 cups.
Implement a program that takes n cups bought and print as an integer the
total number of cups I would get.

'''
count_cups = int(input("Enter the number of cups:"))

print("Total number of cups I would get:",count_cups + count_cups//6)