import pandas
import random
from datetime import date

# dictionaries to hold ticket details
all_names = ['a', 'b', 'c', 'd', 'e']
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)  # Data Frame (Pandas), frames the data sensibly

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate total Profit
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5


# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# choose a winner from our name list
winner_name = random.choice(all_names)

# get position of winner name in list
win_index = all_names.index(winner_name)

# look up total amount won (ie: ticket price + surcharge)
total_won = mini_movie_frame.at[win_index, 'Total']

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# *** Get current date for heading and filename ***
# Get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = f"The current date is {day}/{month}/{year}"
filename = f"MMF_{year}_{month}_{day}"

# Change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# create strings for printing...
ticket_cost_heading = "\n---- Ticket Cost / Profit ----"
total_ticket_sales = f"Total Ticket Sales ${total}"
total_profit = f"Total Profit: ${profit}"

sales_status = "\n*** All the tickets have been sold ***"

winner_heading = "\n---- Raffle Winner ----"
winner_text = f"The winner of the raffle is {winner_name}. " \
              f"They have won ${total_won}. ie: Their ticket is free!"

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