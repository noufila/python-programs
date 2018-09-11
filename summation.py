n=int(input("enter a number : "))
s=0
for i in range(1,n+1):
    s+=i
    for j in range(1,i+1):
        print(j,end=" ")
        if(j!=i):
            print("+",end=" ")
    print("=",s,end=" ")
    print("\n")
    

