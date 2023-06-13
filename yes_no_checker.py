
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
    print("Select how many rounds you want to play and answer the algebra (addition) equations")
    print("The more equations you guess correctly, the more points you get")
    print()
    print("***** Good Luck! *****")
    print()


show_instructions = yes_no("Have you played the game before? ")

if show_instructions == "no":
    instructions()
else:
    print("Program continues")
