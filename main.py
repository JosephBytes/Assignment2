import data
from cashier import Cashier
from sandwich_maker import SandwichMaker

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    while True:
        choice = input("What would you like? (small / medium / large / off): ")
        if choice == "off":
            print("Turning off machine")
            break
        elif choice in recipes:
            ingredients = recipes[choice]["ingredients"]
            cost = recipes[choice]["cost"]
            if sandwich_maker_instance.check_resources(ingredients):  # check we have resources to make the sandwich
                print(f"The cost of a {choice} sandwich is ${cost}") # say how sandwich costs
                payment = cashier_instance.process_coins()  # call the process_coins method that stores the user's payment
                if cashier_instance.transaction_result(payment, cost):  # check if the user has enough money
                    sandwich_maker_instance.make_sandwich(choice, ingredients)  # if they do, we make the sandwich
            else:
                print(f"We don't have enough ingredients to make a {choice} sandwich")
        else:
            print("Please enter small / medium / large / off")
            main()


if __name__=="__main__":
    main()
