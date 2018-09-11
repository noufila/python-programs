n=int(input("enter a number: "))
a=n
rem=0
r=0
while(n>0):
    rem=n%10
    r=r*10+rem
    n=n//10
if(a==r):
    print("pallindrome")

else:
    print("not pallindrome")
