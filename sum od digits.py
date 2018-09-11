n=int(input("enter a number: "))
s=0
while(n>0):
    a=n%10
    
    s+=a
    n=n//10
print("sum = ",s)
