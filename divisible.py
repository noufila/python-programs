n=int(input("enter  1 limit:"))
n1=int(input("enter 2 limit: "))
a=int(input("enter the divisible no: "))
for i in range(n,n1+1):
    if(i%a==0):
        print(i)
