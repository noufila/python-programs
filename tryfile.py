try:
    f=open("ipsr.txt")
    for line in f:
        print(line,end='')
except IOError as err:
    print("file not open")
finally:
    f.close()
