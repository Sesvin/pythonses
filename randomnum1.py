import random
a=random.randint(1,100)
count=0
while True:
    b=int(input("Enter a number between 1 to 100: "))
    count+=1
    if b>=1 and b<=100:
        if b==a:
            print("Your guess is correct")
            print(f"You guessed it in {count} attempts")
            break
        elif b>a:
            print("Your guess is low")
        elif b<a:
            print("Your guess is high")
        else:
            print("Your guess is equal value")