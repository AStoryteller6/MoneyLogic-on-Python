# Initial amount of money the user has
money = 7

# Infinite loop to simulate the vending machine interaction
while True:
    # Display the vending machine menu
    print("Welcome to the vending machine")
    print("Water(1)/Soda(3)/Candy(2)/Snack(6)/Chips(7)")
    print("You have $", money)

    have_item = False
    
    # Get user input for the item they want to buy
    x = input(">> ")

    # Function to handle purchasing an item
    def buy(money, price):
        # Check if the user has enough money to buy the item
        if int(money) >= int(price):
            # Deduct the price from the user's money
            return money - price
        else:
            # Inform the user they don't have enough money
            return "You don't have enough money"

    # Function to handle selling an item (adding money back)
    def sell(price):
        # Add the price of the sold item back to the user's money
        return money + price

    # Check which item the user wants to buy and process the transaction
    if x == "Water":
        print(money)
        money = buy(money, 1)
        have_item == True

    elif x == "Soda":
        print(money)
        money = buy(money, 3)
        have_item = True

    elif x == "Candy":
        print(money)
        money = buy(money, 2)
        have_item = True

    elif x == "Snack":
        print(money)
        money = buy(money, 6)
        have_item = True

    elif x == "Chips":
        print(money)
        money = buy(money, 7)
        have_item = True
    else:
        print("Invalid input")
        break

    # Ask the user if they want to sell anything
    print("Do you want to sell anything")
    a = input("Y/N: ")

    # If the user wants to sell an item
    if a == "Y":
        # Display the menu of items they can sell
        print("What do you want to sell")
        print("Water(1)/Soda(3)/Candy(2)/Snack(6)/Chips(7)")
        
        # Get user input for the item they want to sell
        b = input(">> ")
        
        # Check which item the user wants to sell and process the transaction
        if b == "Water":
            if have_item == True:
                money = sell(1)
                print("You sold water for $1")

                # If the user does not have any water to sell, inform them
            else:
                print("You don't have any water to sell")
                break
        elif b == "Soda":
            if have_item == True:
                money = sell(3)
                print("You sold soda for $3")

                # If the user does not have any soda to sell, inform them
            else:
                print("You don't have any soda to sell")
                break
        elif b == "Candy":

            if have_item == True:
                money = sell(2)
                print("You sold candy for $2")

            # If the user does not have any candy to sell, inform them
            else:
                print("You don't have any candy to sell")
                break
        elif b == "Snack":
            
            if have_item == True:
                money = sell(6)
                print("You sold snack for $6")

            # If the user does not have any snack to sell, inform them
            else:
                print("You don't have any snack to sell")
                break
        elif b == "Chips":
            
            if have_item == True:
                money = sell(7)
                print("You sold chips for $7")

            # If the user does not have any chips to sell, inform them
            else:
                print("You don't have any chips to sell")
                break
        else:
            # If the user inputs an invalid item, inform them
            print("Invalid item")

    # If the user does not want to sell anything, break the loop and end the program
    elif a == "N":
        break

    if x == "Quit":
        break
