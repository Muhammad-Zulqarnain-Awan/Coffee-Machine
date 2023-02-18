MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18
        },
        "cost":1.5
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24
        },
        "cost":3.0
    }
}

resources = {
    "water":300,
    "milk":200,
    "coffee":100
}

earning = 0

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Earning: ${earning}")

def is_resources_sufficient(drink):
    for item in drink:
        if drink[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
        

def process_coins():
        
    print("Please insert the coins!")
    quarters = int(input("Insert the quarters: "))
    dimes = int(input("Insert the dimes: "))
    nickles = int(input("Insert the nickles: "))
    pennies = int(input("Insert the pennies: "))

    total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    return total

def make_payment(cost, drink):
    global earning
    change = 0
    if cost < drink['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = cost - drink['cost']
        earning += cost - change
    
        print(f"Here is ${change} dollars in change.")
        return True

def make_coffee(user_want, drink):
    for item in drink:
        resources[item] -= drink[item]
    print(f"Here is your {user_want}. Enjoy!")

end = True

while end:
    user_want = input("What do you want to order? (espresso, latte, cappuccino) ")
    if user_want == 'off':
        end = False
    elif user_want == 'report':
        report()
    else:
        drink = MENU[user_want]
        if is_resources_sufficient(drink['ingredients']):
            cost = process_coins()
            if make_payment(cost, drink):
                make_coffee(user_want, drink['ingredients'])

