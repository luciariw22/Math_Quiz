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
            print("Please answer yes / no")


def instructions():
    print()
    print("**** Welcome to the Math Quiz ****")
    print()
    print("For each game you will be asked to...\n"
          "- Enter a 'low and 'high number. The computer will randomly\n"
          "generate a 'secret number between your two chosen numbers. It\n"
          "will use these numbers for all rounds in a given game.\n"
          "- The computer will calculate how many guesses you are allowed\n"
          "- enter the number or rounds you want to play"
          "- guess the secret number")
    print()
    print("Good Luck !")
    print()


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or am integer that is more than 0"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    elif low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check that integer is valid (ie: not too low / too high etc)
            if situation == "any integer":
                return response
            elif situation == "both":
                if low <= response <= high:
                    return response
            elif situation == "low only":
                if response >= low:
                    return response

            print(error)

        except ValueError:
            print(error)


show_instructions = yes_no("have you played the "
                           "game before? ")

if show_instructions == "no":
    instructions()
else:
    print("Program Continues")

# Main Routine

rounds_played = 0

rounds_lost = 0
rounds_drawn = 0

rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: " \
                  "Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of " \
                  "{}".format(rounds_played + 1, rounds)

    rounds = int_check("How many rounds", 1, exit_code="")

    print(heading)
