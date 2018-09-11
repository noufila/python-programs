while True:
    try:
        n=int(input("enter a number"))
        n1=int(input("enter a number"))
        print(n/n1)

    except ValueError as err:
        print("must be a number")
    except ZeroDivisionError as err:
        print("cannot be zero")
    else:
        break