n=int(input("enter a no: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n,end=" ")
    if(n!=i):
        print("+",end=" ")
    else:
        break
    
    
