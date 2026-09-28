a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
x= input("Enter operator (+, -, *, /): ")
if x=='+':
    print(a + b)
elif x=='-':
    print(a - b)
elif x=='*':
    print(a * b)
elif x=='/':
    print(a / b)
else:
    print("Invalid operator")