from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# Flag
is_on = True


while is_on:
	request = input(f"What would you like? ({menu.get_items()}): ")
	if request == "off":
		is_on = False
	elif request == "report":
		coffee_maker.report()
		money_machine.report()
	else:
		drink = menu.find_drink(request)
		if coffee_maker.is_resource_sufficient(drink):
			if money_machine.make_payment(drink.cost):
				coffee_maker.make_coffee(drink)
				
				
 				
			


		