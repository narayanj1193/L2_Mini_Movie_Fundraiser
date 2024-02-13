# Functions at the top

# checks user choice is valid according to a list given in main routine
def user_choice(question, valid_list):
    # error code
    error = f"Please choose a valid input from this list, {valid_list}."

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list, checks item if it is in valid_list, then continues to this.
        print(f"{error}")


# function checks that the users input is not blank
def not_blank(question):
    while True:
        response = input(question).strip()

        # if the response is blank, outputs error
        if response == "":
            print("Sorry, this can't be blank or contain only spaces. Please try again.")
        else:
            return response


# Simple number checker to check for integers.
def num_checker(question):
    while True:

        try:
            response_integer = int(input(question))
            return response_integer

        except ValueError:
            print("Please respond with a sensible integer. Please try again.")
            continue


# Calculate ticket prices according to age
def calc_ticket_price(var_age):

    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# Main Routine
# set maximum number of tickets below
MAX_TICKETS = 3  # constant so uppercase.
yes_no_list = ['yes', 'no']  # List of choices for yes/no questions
tickets_sold = 0

ticket_holders_names = []
ticket_holders_ages = []

# Ask user if they want to see the instructions
see_instructions = user_choice("Do you want to read the instructions? ", yes_no_list)

if see_instructions == 'yes':
    print("Instructions go here")

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or 'xxx' to quit: ")  # checks input to make sure it is not blank

    if name == 'xxx':  # break if user inputs xxx
        break

    age = num_checker("What is your age? ")  # Checks to make sure users input is valid for age.

    if 12 <= age <= 120:  # If user is between 12 and 120 program continues
        pass
    elif age < 12:  # if user is less than 12 they are deemed too young.
        print("Sorry you are too young for this movie")
        continue
    else:  # if it is not either of the above two then they must be too old.
        print("This looks like it may be a typo, please try again.")
        continue

    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print("\033[1m" f"\nName: {name}. Age: {age}. Ticket Price: ${ticket_cost:.2f}\b\n" "\033[0m")
    tickets_sold += 1  # Increase amount of tickets sold

remaining_tickets = MAX_TICKETS - tickets_sold

if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the available tickets.")
else:
    print(f"You have sold {tickets_sold} ticket{'s' if tickets_sold != 1 else ''}."
          f" There {'are' if remaining_tickets != 1 else 'is'} {remaining_tickets} remaining.")
