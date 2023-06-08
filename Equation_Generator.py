import random

low_number = 1
high_number = 20

number = random.randint(low_number, high_number)
# gives x's value high/low number
x = random.choice(['low', 'high'])

if x == 'low':
    x_value = low_number
else:
    x_value = high_number

print(f"x = {x_value}")
print(f"{number} + x =")

user_input = input("Answer: ")

# Convert the user input to an integer
user_result = int(user_input)

# Get the correct answer
correct_answer = number + x_value

# Compare the user's input with the correct answer
if user_result == correct_answer:
    print("Correct!")
else:
    print(f"Incorrect. The answer is {correct_answer}")

