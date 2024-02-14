import json


with open('menu.json') as resource:
    coffee_resource = json.load(resource)


menu = coffee_resource["menu"]
resources = coffee_resource["resources"]
profit = 0


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transactional_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost ,2)
        print(f"Here is the ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕") 


is_on = True

while is_on:
    order = input("What would you like? (espresso/latte/cappuccino)")
    if order == 'off':
        is_on= False
    elif order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
         drink = menu[order]
         if is_resource_sufficient(drink["ingredients"]):
             payment = process_coins()
             if is_transactional_successful(payment,drink["cost"]) == True:
                 make_coffee(order,drink["ingredients"])



