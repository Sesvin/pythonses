a=int(input("Enter Physics mark: "))
b=int(input("Enter Chemistry mark: "))
c=int(input("Enter Math mark: "))
total= a + b + c
if a >= 50 and b >= 40 and c >= 60 and total >= 200:
    print("Eligible for Admission")
else:
    print("Not Eligible")