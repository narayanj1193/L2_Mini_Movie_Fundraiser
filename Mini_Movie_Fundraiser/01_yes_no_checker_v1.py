# Functions go here...
def yes_no_checker(question):
    while True:

        # Variables
        yes_variables = ["yes", "y", "yer", "yeah"]
        no_variables = ["no", "n", "nay", "nope"]
        # Ask the user if they have played before

        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response.lower() in yes_variables:
            response = "yes"
            return response

        elif response.lower() in no_variables:
            response = "no"
            return response

        else:
            print("Please type either yes or no \n")


def instructions():
    print("Displays Instructions.")

    return


# Main routine
while True:
    played_before = yes_no_checker("Would you like to see the instructions? ")

    if played_before == "no":
        instructions()
    else:
        print("Program Continues")

    print()
