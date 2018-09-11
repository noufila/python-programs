n=int(input("enter a number: "))
s=0
for i in range(1,n+1):
    
    print(i,end=" ")
    s+=i
    if(n!=i):
        print("+",end=" ")
    
print("=",s)
