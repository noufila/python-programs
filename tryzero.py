try:
    n=int(input("enter a number"))
    n1=int(input("enter a number"))
    print(n/n1)
except ZeroDivisionError as err:
    print("second number cannot be zero")
    print(err)