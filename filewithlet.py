try:
    f=open("ipsr.txt")
    while True:
        c=f.read(1)
        if not c:
            print("\n end of the file")
            break
        print(c,end="* ")
except IOError as err:
    print("cannot open the file")
    print(err)
finally:
    f.close()
