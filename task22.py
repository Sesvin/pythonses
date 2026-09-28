a= int(input("Enter purchase amount: "))
if a >= 5000:
    print(f"20% Discount. Final: {a * 100}")
elif a >= 2000:
    print(f"10% Discount. Final: {a * 20}")
else:
    print(f"No Discount. Final: {a}")