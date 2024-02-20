import pandas

# Functions at the top

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
            response_integer = int(input(question))  # checks user input to make sure it is integer
            return response_integer

        except ValueError:  # catches value error that would be prompted incase if user inputs non-integer
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


# checks that the user has entered a valid response within a specific list.
# also checks user input according to num_letters
def string_checker(question, valid_list, num_letters):
    # error code
    error = f"Please choose either '{valid_list[0]}' or '{valid_list[1]}'."

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        for item in valid_list:
            if response == item[:num_letters] or response == item:
                return item

        # output error if item not in list, checks item if it is in valid_list, then continues to this.
        print(f"{error}\n")


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# Main Routine
# set maximum number of tickets below
MAX_TICKETS = 5  # constant so uppercase.

yes_no_list = ['yes', 'no']  # List of choices for yes/no questions
payment_list = ['cash', 'credit']  # list for preferred payment methods.

tickets_sold = 0

# dictionaries to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# dictionary used to create data frame: column name:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}


# Ask user if they want to see the instructions
see_instructions = string_checker("Do you want to read the instructions? ", yes_no_list, 1)

if see_instructions == 'yes':
    print("Instructions go here.")

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("\nPlease enter your name or 'xxx' to quit: ")  # checks input to make sure it is not blank

    if name == 'xxx':  # break if user inputs xxx
        break

    age = num_checker("\nWhat is your age? ")  # Checks to make sure users input is valid for age.

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

    # ask user for payment method
    payment_method = string_checker("Choose a payment method (cash / credit): ", payment_list, 2)

    if payment_method == "cash":
        surcharge = 0

    else:
        # calculate 5% surcharge if users are paying by credit
        surcharge = ticket_cost * 0.05

    tickets_sold += 1  # Increase amount of tickets sold

    # add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)


mini_movie_frame = pandas.DataFrame(mini_movie_dict)  # Data Frame (Pandas), frames the data sensibly
mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate total Profit
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency formatting (uses the currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:  # for each variable
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print("---- Ticket Data ----")
print()

# output table with ticket data
print(mini_movie_frame)

print()
# output total ticket sales and profit
print()
print(f"Total Ticket Sales: ${total:.2f}")
print(f"Total Profit: ${profit:.2f}")

remaining_tickets = MAX_TICKETS - tickets_sold

if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the available tickets.")
else:
    print(f"You have sold {tickets_sold} ticket{'s' if tickets_sold != 1 else ''}."
          f" There {'are' if remaining_tickets != 1 else 'is'} {remaining_tickets} remaining.")
