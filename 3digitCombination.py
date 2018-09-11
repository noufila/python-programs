a = []

n1 = int(input("enter first number : "))

n2 = int(input("enter second number : "))

n3 = int(input("enter third number : "))

#a.append(n1)
#a.append(n2)
#a.append(n3)
a=[n1,n2,n3]

for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            if(i != j and j != k and i != k):
                print(a[i], a[j], a[k])


