from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money = MoneyMachine()

end = True
while end:
    drink = menu.get_items()
    user_want = input(f"What do you want to order? ({drink}) ")
    
    if user_want == "off":
        end = False
    
    elif user_want == "report":
        resources_report = coffeemaker.report()
        money_report = money.report()
    
    else:
        drink = menu.find_drink(user_want)
        if coffeemaker.is_resource_sufficient(drink):
            order = money.make_payment(drink.cost)
            coffee = coffeemaker.make_coffee(drink)
