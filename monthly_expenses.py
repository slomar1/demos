# Simple monthly expense tracker.
# I know it has been over-done to hell, but I've never done one.
# "Here. We. Go" - Fabrizio Romano.


# Get a valid number from the user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number, not letters or symbols.")


# Main program
savings = get_number("How much do you have saved up? ")
savings_history = [savings]


# Ask for this month's income and expenses
while True:
    income = float(input("How much did you make this month?: "))

    rent = float(input("How much have you spent on housing (rent, utilities, etc.) this month?: "))
    food = float(input("How much have you spent on groceries this month?: "))
    gas = float(input("How much have you spent on transportation (gas, maintenece, public transportation, etc.) this month?: "))
    outside = float(input("How much have you spent on lesuire (restaurants, takeout, clothing, etc.) this month?: "))
    edu = float(input("How much have you spent on education (courses, books, etc.) this month?: "))
    other = float(input("How much money have you spent miscellaneously (gym, entertainment, grooming, etc.) this month?: "))

    
    # Calculate totals
    spent = rent + food + gas + outside + edu + other
    net = income - spent


    # Show this month's summary
    print(f"This month, you have spent a total of ${spent:.2f}. ")
    print(f"After income, your net balance is ${net:.2f} at the end of the month")


    # Update savings
    savings += net
    savings_history.append(savings)
    change = savings_history[-1] - savings_history[-2]
    print(f"You now have ${savings:.2f} in your savings (change of ${change:.2f} after this month). ")


    # Continue or exit
    next_month = input("Would you like to add another month? y/n: ").lower()
    if next_month == "y":
        pass
    elif next_month == "n":
        print("Okay. Here is a list of all your savings per month: ")
        print(savings_history)
        break
