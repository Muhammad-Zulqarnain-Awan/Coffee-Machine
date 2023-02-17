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

end = True

while end:
    user_want = input("What do you want to order? (espresso, latte, cappuccino) ")
    if user_want == "off":
        end = False
    elif user_want == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Total Earning: ${earning}")
    else:
        coffee = MENU[user_want]
        for item in coffee['ingredients']:
            if resources[item] <= coffee['ingredients'][item]:
                print(f"Sorry there is not enough {item}.")
        else:
            print("Please insert the coins!")
            quarters = int(input("Insert the quarters: "))
            dimes = int(input("Insert the dimes: "))
            nickles = int(input("Insert the nickles: "))
            pennies = int(input("Insert the pennies: "))

            total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)

            if total < coffee['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round((total - coffee['cost']),2)
                earning += round((total-change), 2)
                for resource in coffee['ingredients']:
                    resources[resource] -= coffee['ingredients'][resource]

            print(f"Here is ${change} dollars in change.")
            print(f"Here is your {user_want}. Enjoy!")






              
