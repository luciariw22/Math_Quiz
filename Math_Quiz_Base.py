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
    print("**** Welcome to the Math Quiz ****")
    print()
    print("For each game, you will be asked to enter a 'low' and 'high' number. The computer will randomly generate a 'secret number' between your chosen numbers. It will use these numbers for all rounds in a given game.")
    print("You need to guess the correct answer for each math equation.")
    print("Let's test your math skills!")
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
    print("Program continues.")

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

    rounds_played += 1

    # End game if the requested number of rounds has been played
    if rounds_played == rounds:
        end_game = "yes"

    # End game if the player wants to exit
    if input("Type 'xxx' to end the game, or press Enter to continue: ") == "xxx":
        end_game = "yes"

# Put end game content here
print("Thank you for playing.")

