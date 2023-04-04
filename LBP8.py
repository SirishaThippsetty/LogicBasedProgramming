'''
Sum of Digits
Implement a program to calculate sum of digits present in the given number


'''

# n = int(input("Enter the number:"))
# total = 0
# for each in str(n):
#     a = int(each)
#     total += a
# print("Sum of digits:",total)

print(sum([int(i) for i in list(input())]))