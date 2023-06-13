
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


rounds = check_rounds()