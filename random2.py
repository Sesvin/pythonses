import random
num = random.randint(1, 10)
guess = int(input("guess the number between 1 to 10: "))
if guess == num:
    print("your guess is correct")
else:
    print(f"Wrong! The number was {num}")