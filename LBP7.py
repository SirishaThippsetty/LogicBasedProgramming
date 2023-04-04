'''
Extract Digits from the number
Implement a program to extract digits from the given number

'''

#### Normal Number #####
# number = input("Enter the number:")
# for each in number:
#     print(each,end = " ")

#### Reverse Number #####
# for i in input()[::-1]:
#      print(i,end=' ')

n=int(input())
while n!=0:
 print(n%10,end=' ')
 n = n//10