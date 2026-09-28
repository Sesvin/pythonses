n=5
for i in range(n):
    for j in range(n):
        if i==n //2 :
            print("*",end=" ")
        elif j==0 or j==n-1:
            print("*",end=" ")
        elif i==j or i+j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()