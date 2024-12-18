from datetime import datetime
from display_data import summarise_totals
import file_operations
from color50 import constants
from colors import *

class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date
    
    def add_expense():
        color_print(f"\nGetting User Expense", color=heading)
        color_print(f"--------------------", heading)
    
        expense_name = input(f"{secondary_text}Enter expense name: {constants.RESET}")
        try:
            expense_amount = float(input(f"{secondary_text}Enter the expense amount: ${constants.RESET}"))
        except ValueError:
            print("Error: Please enter a dollar amount ie: 4.95")
            Expense.add_expense()
        except Exception as e:
            print(f'An unexpected error occured: {e}')
            Expense.add_expense()

        expense_category = [
            "🍔 Food",
            "🏠 Home",
            "🚗 Fuel",
            "🎸 Entertainment",
            "🌟 Misc"
        ]

        counter = 1

        while True:
    
            for category in expense_category:
                color_print(f'{counter}. {category}', heading)
                counter += 1
    
            value_range = f'(1 - {len(expense_category)})'
            try:
                choice_expense_category = int(input(f"Please enter a category number {value_range}: ")) - 1
            except ValueError:
                print(f'Error: Please enter an integer ie: {value_range}')
                input("----Press Enter to Continue----")
                Expense.add_expense()
            except Exception as e:
                print(f"An unexpected error has occured: {e}")
                input("----Press Enter to Continue----")
                Expense.add_expense()

            if choice_expense_category in range(len(expense_category)):
                new_expense = Expense(
                    name=expense_name, 
                    category=expense_category[choice_expense_category], 
                    amount=expense_amount,
                    date = datetime.now().strftime('%Y-%m-%d')
                )
                new_expense_data = file_operations.FileOperations()
                new_expense_data.save_expense(new_expense)
                return
            else:
                print("You have entered an invalid option. Try again!")
            

class Income:
    def __init__(self, name, amount, category, date):
        self.amount = amount
        self.category = category
        self.name = name
        self.date = date

    def add_income():
        color_print("\nGetting User Income", heading)
        color_print("----------------------", heading)

        income_name = input(f"{secondary_text}Enter the income name: {constants.RESET}")
        
        try:
            income_amount = float(input(f"{secondary_text}Enter the income amount: ${constants.RESET}"))
        except ValueError:
            print("Please enter a dollar value, ie: 2.55")
            Income.add_income()
        except Exception as e:
            print(f'An unexpected error occured: {e}')
            input("----Press Enter to Continue----")
            Income.add_income()

        income_category = [
            "💼 Salary",
            "🎁 Gift",
            "🤑 Investment Income",
            "🌟 Other Income"
        ]

        for i, category in enumerate(income_category):
            color_print(f'{i + 1}. {category}', color=heading)

        value_range = f'(1 - {len(income_category)})'
        try:
            choice_of_category = int(input(f'{secondary_text}Please enter a category number {value_range}: {constants.RESET}')) - 1
        except ValueError:
            print(f"Please enter a whole number: {value_range}")
            print("----Press Enter to Continue----")
            Income.add_income()
        except Exception as e:
            print(f'An unexpected error occured: {e}')
            print("----Press Enter to Continue----")
            Income.add_income()

        if choice_of_category in range(len(income_category)):
            new_income = Income(
                name=income_name, 
                category=income_category[choice_of_category], 
                amount=income_amount,
                date = datetime.now().strftime('%Y-%m-%d')
            )
            new_income_data = file_operations.FileOperations()
            new_income_data.save_income(new_income)
            return
        else:
            print("You have entered an invalid option. Try again!")
            Income.add_income()



def income_expense_calc():

    income_summary = summarise_totals('income_data.csv')
    expense_summary = summarise_totals('expense_data.csv')
    financial_position = float(income_summary) - float(expense_summary)
    color_print('---------------------------------------------------------', heading)
    color_print(f'\nYou have earned ${income_summary:.2f} and spent ${expense_summary:.2f} on expenses.\n')
    if financial_position > 0.0:
        color_print(f'You have ${financial_position:.2f} remaining after your expenses.')
    elif financial_position == 0.0:
        color_print("You have no money left after your expenses")
    else:
        color_print(f'You have spent ${financial_position:.2f} more than what you have earned.')
    
    input(f"{primary_text}------Press Enter to Continue-----{constants.RESET}")
    