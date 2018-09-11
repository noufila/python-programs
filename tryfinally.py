def finallytest():
    try:
        n=int(input("enter a number"))
        n1=int(input("enter a number"))
        print(n/n1)
        return 1
    except (ZeroDivisionError,ValueError) as err:
        print("not valid")
        print(err)
        return 0
    finally:
        print("it is finally clause")
result=finallytest()
print(result)