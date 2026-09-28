phone=input("Enter a phone number: ")
a="*" * (len(phone) - 4) + phone[-4:]
print(a)