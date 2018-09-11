try:
    n=int(input("enter a number"))
    n1=int(input("enter number"))
    d=n/n1
    print(d)
except ValueError as err:
    print("input a number")
    print(err)

