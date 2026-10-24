# Taco Palace Ordering System
# Uses lists, if-else, variables, functions, and loops.

# Menu items and their prices (lists that line up by position)
menu_items = ["Taco", "Burrito", "Nachos", "Soft Drink"]
menu_prices = [4.95, 8.25, 6.75, 2.50]


def print_menu():
    """Prints the Taco Palace menu."""
    print()
    print("Taco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")


def get_item_name(choice):
    """Returns the name of the food item for a menu choice (1-4)."""
    return menu_items[choice - 1]


def get_price(choice):
    """Returns the price of the food item for a menu choice (1-4)."""
    return menu_prices[choice - 1]


def format_order(order_list):
    """Turns the list of ordered items into a sentence like
    'a Taco, a Burrito, and Nachos'."""
    names = []
    for item in order_list:
        if item == "Nachos":
            names.append(item)
        else:
            names.append("a " + item)

    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return names[0] + " and " + names[1]
    else:
        return ", ".join(names[:-1]) + ", and " + names[-1]


def main():
    total = 0.0
    order = []

    print("Welcome to Taco Palace, please view the menu below and "
          "enter the number that represents your selection.")

    choice = 0
    while choice != 5:
        print_menu()

        try:
            choice = int(input("Enter your selection: "))
        except ValueError:
            print("Please enter a number from 1 to 5.")
            continue

        if choice >= 1 and choice <= 4:
            item = get_item_name(choice)
            price = get_price(choice)
            total = total + price
            order.append(item)
            print("You have selected " + format_order([item]) + ".")
        elif choice == 5:
            print()
            if len(order) == 0:
                print("You did not order anything. Thanks for visiting Taco Palace!")
            else:
                print("You ordered " + format_order(order) + ".")
                print(f"Your total is ${total:.2f}")
        else:
            print("Invalid selection. Please enter a number from 1 to 5.")


main()