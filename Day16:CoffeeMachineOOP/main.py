from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Day 16 I was given classes and had to read their documentation for the functionalities, and learned about OOP and how much it helps in reducing code
coffee_menu = Menu()
coffee_making = CoffeeMaker()
coffee_money = MoneyMachine()


is_on = True
while(is_on):
  choice = input(f"Choose 1: {coffee_menu.get_items()}off/report\n")
  if choice == 'off':
    is_on = False
  elif choice == 'report':
    coffee_making.report()
    coffee_money.report()
  else:
    if choice in coffee_menu.get_items():
      print(f"The cost of drink ${coffee_menu.find_drink(choice).cost}")
      ingredients = coffee_menu.find_drink(choice)
      print(ingredients.ingredients)
      enough_money = coffee_money.make_payment(coffee_menu.find_drink(choice).cost)
      can_make = coffee_making.is_resource_sufficient(ingredients)
      if can_make and enough_money:
        coffee_making.make_coffee(ingredients)
        print("\nCoffee Machine Report\n____________\n")
        coffee_making.report()
        print("\n")
  if is_on:
    again = input("anything else? 'y', 'n'\n")
    if again == 'n':
      is_on = False
