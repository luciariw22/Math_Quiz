import random

low_number = 1
high_number = 20

answer = low_number, high_number
x = low_number, high_number


secret = random.randint(low_number, high_number)

# Start Round
while True:
    print(low_number/high_number, "+", "x")

    guess = int(input("Guess a number: "))

    if guess == secret:
        print("Congratulations! You guessed the secret number.")
        break
    elif guess < secret:
        print("Too low! Try again.")
        low_number = guess + 1
    else:
        print("Too high! Try again.")
        high_number = guess - 1