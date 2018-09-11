m1=int(input("marks of  sub 1 :  "))
m2=int(input("marks of  sub 2 :  "))
m3=int(input("marks of  sub 3 :  "))
m4=int(input("marks of  sub 4 :  "))
m5=int(input("marks of  sub 5 :  "))
mark=[m1,m2,m3,m4,m5]
s=sum(mark)
print("total mark: ",s)
if(s>=450):
    print("grade is A")
elif(s>=400):
    print("grade is B")
elif(s>=350):
    print("grade is c")
elif(s>=200):
    print("grade is D")
else:
    print("fail")

    
