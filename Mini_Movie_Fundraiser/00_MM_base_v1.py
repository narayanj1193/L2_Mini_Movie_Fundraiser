# Functions at the top

# checks user choice is valid according to a list given in main routine
def user_choice(question, valid_list):
    # error code
    error = "Please choose a valid input."

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list, checks item if it is in valid_list, then continues to this.
        print(f"{error}\n")


# function checks that the users input is not blank
def not_blank(question):

    while True:
        response = input(question).strip()

        # if the response is blank, outputs error
        if response == "":
            print("Sorry, this can't be blank or contain only spaces. Please try again")
        else:
            return response


# Main Routine

# set maximum number of tickets below
MAX_TICKETS = 3  # constant so uppercase.
yes_no_list = ['yes', 'no']  # List of choices for yes/no questions
tickets_sold = 0

# Ask user if they want to see the instructions
see_instructions = user_choice("Do you want to read the instructions? ", yes_no_list)

if see_instructions == 'yes':
    print("Instructions go here")

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or 'xxx' to quit: ")
    print(name)

    if name == 'xxx':
        break

    tickets_sold += 1

remaining_tickets = MAX_TICKETS - tickets_sold

if tickets_sold == 3:
    print("Congratulations, you have sold all the available tickets.")
else:
    print(f"You have sold {tickets_sold} ticket{'s' if tickets_sold != 1 else ''}."
          f" There {'are' if remaining_tickets != 1 else 'is'} {remaining_tickets} remaining.")
