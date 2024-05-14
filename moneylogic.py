# Initial amount of money the user has
money = 7

# Infinite loop to simulate the vending machine interaction
while True:
    # Display the vending machine menu
    print("Welcome to the vending machine")
    print("Water(1)/Soda(3)/Candy(2)/Snack(6)/Chips(7)")
    print("You have $", money)

    
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
    def sell(price, money):
        # Add the price of the sold item back to the user's money
        return price + money

    def have_item(item):
        return item
    # Check which item the user wants to buy and process the transaction
    if x == "Water":
        money = buy(money, 1)
        Water = True
        have_item(Water)
        print(money)

    elif x == "Soda":
        money = buy(money, 3)
        Soda = True
        print(money)
        have_item(Soda)

    elif x == "Candy":
        money = buy(money, 2)
        Candy = True
        print(money)
        have_item(Candy)

    elif x == "Snack":
        money = buy(money, 6)
        Snack = True
        print(money)
        have_item(Snack)
    
    elif x == "Chips":
        money = buy(money, 7)
        Chips = True
        print(money)
        have_item(Chips)
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
            money = sell(1, money)
            have_item(Water)
            print("You have sold water for $1")
            if Water == False:
                print("You don't have any water")

        elif b == "Soda":
            money = sell(3, money)
            have_item(Soda)
            print("You have sold soda for $3")
            if Soda == False:
                print("You don't have any soda")

        elif b == "Candy":
            money = sell(2, money)
            have_item(Candy)
            print("You have sold candy for $2")
            if Candy == False:
                print("You don't have any candy")

        elif b == "Snack":
            money = sell(6, money)
            have_item(Snack)
            print("You have sold snack for $6")
            if Snack == False:
                print("You don't have any snack")
            
        elif b == "Chips":
            money = sell(7, money)
            have_item(Chips)
            print("You have sold chips for $7")
            if Chips == False:
                print("You don't have any chips")
        else:
            print("Invalid input")
    
    print("Do you want to buy anything else?")
    z = input("Y/N: ")
    if z == "N":
        break
