"""#find the number is postive even , neagitve even and  postive odd neagitve odd.
num=int(input("enter the number:"))
if num>=0 and num%2==0:
    print("postive even")
elif num<0 and num%2==o:
        print("negative even")
elif num>=0 and num%2!=0:
        print("postive odd")
else:
       print("negative odd")"""
"""#find the greatest of three number
a,b,c=map(int,input().split())
if a>b and a>c:
     print("a is greater")
elif  b>c:
    print("b is greater")
else:
    print("c is greater")"""
#nested if
num=int(input("enter the number:"))
if num>0:
    if num%2==0:
        print("+ve even")
    else:
          print("+ve odd")
else:
    if num%2==0:
        if num<0:
          print("-ve even")
    else:
          print("-ve odd")
#
"""a,b,c=map(int,input().split())
if a>=b:
    if a>=c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>=c:
        print("b is greater")
    else:
        print("c ic greatest")"""

        





