"""We will take 1 element at a time from list B and then compare it with all the elements from list A and we will maintain a list c to check which elements are matching so that if list c is empty then print -1
"""
n, m = map(int, input().split())
a = []
b = []
c = []
z = 1
for i in range(n):
    a.append(input())             #append is to add an element in sa list
for j in range(m):
    b.append(input())
for k in b:
    for l in a:
        if(k == l):
            c.append(z)
            z = z+1
        else:
            z = z+1
    if len(c) == 0:
        c.append(-1)  
    z = 1
    for o in c:
       print(o, end=" ")
    print()
    c.clear()
