# Simple monthly expense tracker.
# I know it has been over-done to hell, but I've never done one.
# "Here. We. Go" - Fabrizio Romano.




savings = float(input("How munch do you have saved up?: "))

savings_per_month = []
savings_per_month.append(savings)

def add_savings(x):

    global savings_per_month
    global savings

    savings = savings + x
    
    savings_per_month.append(savings)
    print(f"You now have ${savings_per_month[-1]} in your savings, as opposed to {savings_per_month[-2]}")
    print(f"This is a difference of ${savings_per_month[-1] - savings_per_month[-2]} in your total savings. ")




while True:
    
    income = float(input("How much did you make this month?: "))

    rent = float(input("How much have you spent on housing (rent, utilities, etc.) this month?: "))
    food = float(input("How much have you spent on groceries this month?: "))
    gas = float(input("How much have you spent on transportation (gas, maintenece, public transportation, etc.) this month?: "))
    outside = float(input("How much have you spent on lesuire (restaurants, takeout, clothing, etc.) this month?: "))
    edu = float(input("How much have you spent on education (courses, books, etc.) this month?: "))
    other = float(input("How much money have you spent miscellaneously (gym, entertainment, grooming, etc.) this month?: "))

    spent = rent + food + gas + outside + edu + other
    total = income - spent
    print(f"This month, you have spent ${spent}. ")
    print(f"This has given you a balance of ${total} at the end of the month")

    add_savings(total)

    next_month = input("Would you like to add another month? y/n: ").lower()
    if next_month == "y":
        pass
    elif next_month == "n":
        print("Okay. Here is a list of all your savings per month: ")
        print(savings_per_month)
