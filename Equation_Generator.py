import random

low_number = 1
high_number = 20

num1 = random.randint(low_number, high_number)
num2 = random.randint(low_number, high_number)

print(num1, "+", num2, "=")

user_input = input("Answer: ")

# Convert the user input to an integer
user_result = int(user_input)

# Compare the user's input with the correct answer
if user_result == num1 + num2:
    print("Correct!")
else:
    print("Incorrect. The answer is", num1 + num2)