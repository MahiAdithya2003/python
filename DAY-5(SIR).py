"""n1,n2,n3=map(int,input().split())
if n1%2==0:
    print("n1 is even")
else:
    print("n1 is odd")
if n2%2==0:
    print("n2 is even")
else:
    print("n2 is odd")
if n3%2==0:
    print("n3 is even")
else:
    print("n3 is odd")"""


"""#find which one is even or odd from the list number.

lst=[11,12,13,14,15]
for ind in range(0,5,1):
    if lst[ind]%2==0:
        print(lst[ind], "is even")
    else:
        print(lst[ind],"is odd")"""

"""#print the even numbers between 20 to 40.
for num in range(20,41):
    if num%2==0:
        print(num)"""
"""#approach-2
for num in range(20,41,2):
     print(num)"""
"""#print 1-100 numbers.
for num in range(1,101,1):
    print(num, end=" ")"""

#sum of n natural number

n = int(input())
total = 0
for i in range(1,n+1):
    total = total + i
print(total)
