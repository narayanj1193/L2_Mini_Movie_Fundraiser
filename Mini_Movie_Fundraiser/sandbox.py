import pandas
import math


# asks user if they have used the quiz before, if not displays instructions
def instructions():
    played_before = yes_no("Have you used this program before? ")
    if played_before == 'no':
        print("Displays instructions")

    return


# checks validity of user's number input according to
# set num_type in main routine. Takes in custom error message
def num_check(question, error, num_type):
    while True:

        try:
            # uses num_type and checks if user input is valid according
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# checks that user has entered either yes or no
def yes_no(question):
    yes_no_list = ['yes', 'no']

    # error code
    error = f"Please choose either '{yes_no_list[0]}' or '{yes_no_list[1]}'."

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        for item in yes_no_list:
            if response == item[:1] or response == item:
                return item

        # output error if item not in list, checks item if it is in yes_no_list, then continues to this.
        print(f"{error}\n")


# function checks that the users input is not blank
def not_blank(question, error):
    while True:
        response = input(question).strip()

        # if the response is blank, outputs error
        if response == "":
            print(f"\n {error}. Please try again.\n")
        else:
            return response


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# gets expenses, returns list which has
# the data frame and subtotal
def get_expenses(var_fixed):
    # setup dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name , quantity and item
        item_name = not_blank("Item name: ", "The item name cannot be blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity: ", "The amount must be a whole number more than zero.", int)

        else:
            quantity = 1

        price = num_check("How much for a single item? $", "The price must be a number (more than 0)", float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # calculate Cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # find subtotal
    sub_total = expense_frame['Cost'].sum()

    # currency formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# prints final outputs regarding users expenses.
def expense_print(heading, frame, subtotal):
    print()
    print(f"**** {heading} Costs ****")
    print(frame)
    print()
    print(f"{heading} Costs: ${subtotal:.2f}")
    return


# Work out profit goal and total sales required.
def profit_goal(total_costs):
    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    while True:

        # ask for profit goal...
        response = input("What is your profit goal (eg $500 or %)? ")

        # checks if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # check if last character is %...
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no(f"Do you mean ${amount:.2f}. ie {amount:.2f} dollars?, (y / n): ")

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"

            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no(f"Do you mean {amount}%, (y / n)? ")
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# rounding function - rounds to nearest 'round_to' value.
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# *** main routine starts here ***

print("Fundraising Calculator")

instructions()
print()

fixed_frame = ''

# get product name
product_name = not_blank("Product Name: ", "The product name cannot be blank")

how_many = num_check("How many items will you be producing? ", "The number of items must be"
                                                               "a whole number more than zero", int)
print()
print("Please enter your variable costs below... ")

# get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y / n)? ")

# get fixed costs
if have_fixed == "yes":
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

else:
    fixed_sub = 0

# work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# calculate total sales needed to reach goal
sales_needed = all_costs + profit_target

# ask user for rounding
round_to = num_check("Round to nearest...? $", "Can't be 0", int)

# Calculate recommended price
selling_price = sales_needed / how_many

recommended_price = round_up(selling_price, round_to)

# *** Printing Area ***

product_name = f"Fund Raising - {product_name}"
variable_heading = "Variable Costs"
fixed_cost_heading = "Fixed Costs"

# change frames to strings
variable_txt = pandas.DataFrame.to_string(variable_frame)
fixed_txt = pandas.DataFrame.to_string(fixed_frame)

to_write = [product_name, variable_heading, variable_txt, f"Subtotal: ${variable_sub:.2f}", fixed_cost_heading, fixed_txt,
            f"Subtotal: ${fixed_sub:.2f}", f"*** Profit Target: ${profit_target:.2f} ***",
            f"Sales Needed: ${sales_needed:.2f}", f"Recommended Price: ${recommended_price:.2f}"]

# create file to hold data (add .txt extension)
file_name = f"{product_name}.txt"
text_file = open(file_name, "w+")

# heading
for item in to_write:
    item = f"{item}"
    text_file.write(item)
    text_file.write("\n\n")

text_file.close()

print()
for item in to_write:
    print(item)
    print()
