from datetime import date

import pandas
import random


# Functions at the top

# shows instructions
def show_instructions():
    print('''\n
***** Instructions *****

For each ticket, enter ....
- The person's name (can't be blank)
- Age (between 12 and 120_
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit.

The program will then display the ticket details including
 the cost of each ticket, the total cost and the total profit.

 This information will also be automatically written to a text 
 file. 

 Enjoy!
 **********************''')


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
        for i in valid_list:
            if response == i[:num_letters] or response == i:
                return i

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
    show_instructions()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("\nPlease enter your name or 'xxx' to quit: ")  # checks input to make sure it is not blank

    if name == 'xxx' and len(all_names) > 0:  # break if user inputs xxx
        break
    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

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

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate total Profit
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# choose a winner from our name list
winner_name = random.choice(all_names)

# get position of winner name in list
win_index = all_names.index(winner_name)

# look up total amount won (ie: ticket price + surcharge)
total_won = mini_movie_frame.at[win_index, 'Total']

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency formatting (uses the currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:  # for each item in the dictionary, add currency
    # matches dictionary item to item from movie_frame and adds appropriate currency.
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# get position of winner name in list
win_index = all_names.index(winner_name)

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# *** Get current date for heading and filename ***
# Get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = f"\n--- Mini Movie Fundraiser Ticket Data ({day}/{month}/{year}) ----\n"
filename = f"MMF_{year}_{month}_{day}"

# Change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# create strings for printing...
ticket_cost_heading = "\n---- Ticket Cost / Profit ----"
total_ticket_sales = f"Total Ticket Sales ${total:.2f}"
total_profit = f"Total Profit: ${profit:.2f}"

sales_status = f"{MAX_TICKETS - tickets_sold} ticket{'s' if tickets_sold > 1 else ''} remaining"
print(f"\nYou have sold {tickets_sold} ticket{'s' if tickets_sold > 1 else ''}."
      f" There {'are' if MAX_TICKETS - tickets_sold > 1 else 'is'} {MAX_TICKETS - tickets_sold} remaining.")

winner_heading = "\n---- Raffle Winner ----"
winner_text = f"The winner of the raffle is {winner_name}. " \
              f"They have won ${total_won:.2f}. ie: Their ticket is free!"

# list holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading, total_ticket_sales,
            total_profit, sales_status, winner_heading, winner_text]

# print output
for item in to_write:
    print(item)

# write output to file
# create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
