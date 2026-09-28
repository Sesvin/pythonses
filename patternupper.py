n=5
for i in range(n):
    upper=True
    for j in range(i,n):
        if upper:
            print(chr(65+j),end="")
        else:
            print(chr(97+j),end=" ")
        upper=not upper
    print()