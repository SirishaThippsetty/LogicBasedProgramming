'''
Implement the following function
int BlackJack(int n1,int n2);
the function accepts two +ve integers n1 and n2 as its arguments. 
Implement the function on given two vlaues to return an int value as follows
return whichever value is nearest to 21 without going over. Return if they go 
both go over.
input --------> two int values n1 and n2
constraint ---> no
output -------> 0 or n1 or n2

n1>21 and n2>21 ===> 0
n1>21 =============> n2
n2>21 =============> n1
n1<21 and n2<21 ===> n1 or n2 max

'''
def BlackJack(n1,n2):
    if n1 > 21 and n2 > 21:
        return 0
    elif n1 > 21:
        return n2
    elif n2 > 21:
        return n1
    elif n1 < 21 and n2 < 21:
        return max(n1,n2)

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print(BlackJack(n1,n2))

