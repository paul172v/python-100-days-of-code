coins = [0.01, 0.05, 0.10, 0.25]

resources = {"water": 300, "milk": 200, "coffee": 100}

recipes = {
    "Espresso": {"water": 50, "milk": 0, "coffee": 18, "price": 1.50},
    "Latte": {"water": 200, "milk": 150, "coffee": 24, "price": 2.50},
    "Cappuccino": {"water": 250, "milk": 100, "coffee": 24, "price": 3.00},
}


def process_coins(drink):
    print("Please insert coins...")
    one_cents_amount = int(input("How many 1 cent coins are you using?"))
    five_cents_amount = int(input("How many 5 cent coins are you using?"))
    ten_cents_amount = int(input("How many 10 cent coins are you using?"))
    twenty_five_cents_amount = int(input("How many 25 cent coins are you using?"))

    one_cents_tally = 0.1 * one_cents_amount
    five_cents_tally = 0.5 * five_cents_amount
    ten_cents_tally = 0.10 * ten_cents_amount
    twenty_five_cents_tally = 0.25 * twenty_five_cents_amount

    total_tally = (
        one_cents_tally + five_cents_tally + ten_cents_tally + twenty_five_cents_tally
    )

    price = recipes[drink]["price"]

    change = 0

    if total_tally < price:
        print("Sorry, this is not enough! Your money has been refunded!")
    else:
        resources["water"] -= recipes[drink]["water"]
        resources["milk"] -= recipes[drink]["milk"]
        resources["coffee"] -= recipes[drink]["coffee"]

        change = total_tally - price
        print(f"Here is your {drink} with ${change} in change.")
        print(
            f"The following resources are available...\nwater: {resources['water']}\nmilk {resources['milk']}\ncoffee {resources['coffee']}"
        )


def enough_ingredients(drink):
    if (
        resources["water"] >= recipes[drink]["water"]
        and resources["milk"] >= recipes[drink]["milk"]
        and resources["coffee"] >= recipes[drink]["coffee"]
    ):
        process_coins(drink)
    else:
        print(
            "Sorry but the machine does not have enough ingredients to make this item!"
        )


print("---172v Coffee Machine---")
print("-------------------------")
task = input(
    "What task would you like to perform? (Number only please)\n1. Print report\n2. Order an espresso\n3. Order a latte\n4. Order a cappuccino\n"
)

if task == "1":
    print("Current resources")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
elif task == "2":
    enough_ingredients("Espresso")
elif task == "3":
    enough_ingredients("Latte")
elif task == "4":
    enough_ingredients("Cappuccino")
