try:
    n=int(input("enter a number"))
    n1=int(input("enter a number"))
    print(n/n1)
except Exception as err:
    print("wrong")
    print(err)
