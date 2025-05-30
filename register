# Small little register project.
# I know it doesn't have all the features of an actual register, but it's something.

inventory = {
    "mandarins": 3.09,
    "lemons":     4.29,
    "avocado":    1.09,
    "pineapple":  2.29,
    "oranges":    4.95,
    "tomatoes":   2.19,
    "onions":     2.55
}

total = 0.0
receipt = []

print("Welcome! Scan items or type 'x' to finish.\n")

while True:

    choice = input("Please select an item form our inventory to add to order. " \
    "Once you finish scanning, please press 'x' to finish. ").strip().lower()

    if choice == "x":
        print(f"Thank yuu for shopping wiht us. Your total is ${total}.")
        print(f"This is your receipt: ")
        print(receipt)
        break

    elif choice not in inventory:
        print(f"Sorry, {choice} is not in inventory. Please try again. ")

    elif choice in inventory:
        receipt.append(choice)
        total += inventory[choice]
        print(f"{choice.title()} added. Your running total is currently ${total}.")
