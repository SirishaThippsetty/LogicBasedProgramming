'''
The e-commerce company Bookshelf wishes to analyse its monthly sales data
between minimum range 30 to max range 100.
The company has categorized these book sales into four groups depending on
the number of sales with the help of these groups the company will know
which stock they should increase or decrease in their inventory for the next
month.
the groups are as follows
30-50 ------------------> D
51-60 ------------------> C
61-80 ------------------> B
81-100 -----------------> A

'''
n = int(input())
if n>=30 and n<=100:
    if n>=30 and n<=50:
        print("Group D")
    elif n>=51 and n<=60:
        print("Group C")
    elif n>=61 and n<=80:
        print("Group B")
    elif n>=81 and n<=100:
        print("Group A")
else:
    print("Invalid")