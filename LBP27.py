'''
Find The Sequence Sum
Given three integers i,j&k, a sequence sum to be the value of 
i+(i+1)+(i+2)..+j+(j-1)+(j-2)+..+k
(increment from i until it equals to j, 
then decrement from j until equals k). 
Given values i,j,k. 
caluclate the sequence sum as described.
5,9,6
5+6+7+8+9+8+7+6=56
'''

i = int(input("Enter the value i:"))
j = int(input("Enter the value j:"))
k = int(input("Enter the value k:"))

count1 = 0

for a in range(i,j):
    count1 += a

while j != k:
    count1 += j
    j -= 1

 
print("Sequence sum:",count1)