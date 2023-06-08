import random

# Functions go here


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes/no")


def instructions():
    print()
    print("**** Welcome to the Math Quiz ****")
    print()
    print("Select how many rounds you want to play and answer the alegbra equations")
    print("The more equations you guess correct, "
          "the more points you get")
    print()
    print("***** Good Luck! *****")
    print()


def check_rounds():
    while True:
        response = input("How many rounds would you like to play?: ")

        round_error = "Please enter a whole number greater than 0, or leave it blank for continuous mode."

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here...

show_instructions = yes_no("Have you played the game before? ")

if show_instructions == "no":
    instructions()
else:
    print("Program continues")

rounds_played = 0

# Ask the user for the number of rounds, leave it blank for continuous mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)

    # Generate two random numbers for the math equation
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
        question_result = "correct"
    else:
        print(f"Incorrect. The answer is {correct_answer}")
        question_result = "incorrect"

    rounds_played += 1

    # End game if rounds end or user enters 'xxx'
    if rounds_played == rounds:
        end_game = "yes"

    if input("Type 'xxx' to end the game, or press Enter to continue: ") == "xxx":
        end_game = "yes"

# Calculate Game Statistics
game_summary = []
rounds_won = sum(question["Result"] == "correct" for question in game_summary)
rounds_lost = rounds_played - rounds_won

# Display Game Statistics
percent_win = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100

print("\n***** Game Statistics *****")
print(f"Total Rounds Played: {rounds_played}")
print(f"Total Rounds Won: {rounds_won}")
print(f"Total Rounds Lost: {rounds_lost}")
print()
print("Thank you for playing!")

