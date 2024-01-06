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


# instructions function
def instructions():
    print("*** How to use Mini Movie Fundraiser ***\n")

    # Brief description of game
    print("Your objective is to answer graph-related questions by providing the equation of the presented graph. \nYou "
          "have up to three attempts to guess the correct equation. Choose your preferred difficulty level (easy,\n "
          "medium, or hard) and graph mode (linear, parabola, or mixed) to customize your quiz experience. The game\n "
          "will keep track of your progress, including the number of questions attempted, correct answers,\n "
          "wrong answers, and your average number of guesses. Have fun and enjoy the challenge!\n")
    # Sections with numbers
    print("1. Objective")
    print("2. How to Answer")
    print("3. Difficulty Levels")
    print("4. Using the Graph display")
    print("5. Exiting the game\n")

    # Ask the user to select a section
    selected_section = '0'
    while selected_section != "":
        selected_section = input("If you would like to learn more enter the number of your desired section,"
                                 " otherwise press <enter>: ")

        # If user presses enter, program continues
        if selected_section == "":
            break

        # Display the selected section
        elif selected_section == "1":
            # Game Objective
            print("\nObjective:")
            print("Answer graph-related questions by providing the equation of the presented graph.\n")

        elif selected_section == "2":
            # How to Answer
            print("\nHow to Answer:")
            print("- You will be shown a graph, and you need to determine its equation.")
            print("- You have a maximum of three attempts per question.")
            print("- Enter your answer using a valid equation format.")
            print("- For linear equations please use the format 'mx + c'")
            print("- For quadratic equations please use either 'k * (x-a)^2 + b' or 'k * (x-a)*(x-b)'.")

            print('\033[1m!! You have a maximum of three attempts to guess the correct equation for each '
                  'graph !!\033[0m')  # Bold text

        elif selected_section == "3":
            # Difficulty Levels
            print("\nDifficulty Levels:")
            print("- Easy: Graphs with simple features and integer coordinates.")
            print("- Medium: Graphs with more complex features and decimal coordinates.")
            print("- Hard: Challenging graphs with a wide range of features and fractional coordinates.\n")

        elif selected_section == '4':
            # ways to use the graph
            print("\nHow to use the graph:")
            print("- You can move the graph around by pressing the arrow cross button in the bottom left corner of the "
                  "graph display.")
            print("- You can zoom into the graph by pressing the magnifying glass at the bottom of the graph display."
                  "When you press it you can draw a square using your left mouse button to zoom in to the area you have"
                  "drawn.")
            print("- Pressing the house button will reset the graph to its original display. By pressing the two arrows"
                  "you can also undo or redo changes you have done to the graph display. \n")

        elif selected_section == "5":
            # Exiting the Game
            print("\nExiting the Game:")
            print("If you wish to quit the game at any time, enter 'xxx' as your answer to any question.")
            print("Make sure to close the graph before entering the exit code. \n")

        else:
            # Invalid input
            print("Invalid input. Please select a valid section number.")

    print("Enjoy the game and have fun! 📈💡\n")


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
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx':
        break

    tickets_sold += 1

remaining_tickets = MAX_TICKETS - tickets_sold
if tickets_sold == 3:
    print("Congratulations, you have sold all the available tickets.")
else:
    print(f"You have sold {tickets_sold} ticket{'s' if tickets_sold != 1 else ''}."
          f" There {'are' if remaining_tickets != 1 else 'is'} {remaining_tickets} remaining.")
