from datetime import datetime

class BudgetManager():
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

class Expense(BudgetManager):
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return f"Expense: {self.name}, {self.category}, ${self.amount:.2f}"
    
    def add_expense():
        print("\nGetting User Expense")
        print("--------------------")
    
        expense_name = input("Enter expense name: ")
        try:
            expense_amount = float(input("Enter the expense amount: $"))
        except ValueError:
            print("Error: Please enter a dollar amount ie: 4.95")
            add_expense()
        except Exception as e:
            print(f'An unexpected error occured: {e}')
            add_expense()

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
                print(f'{counter}. {category}')
                counter += 1
    
            value_range = f'(1 - {len(expense_category)})'
            try:
                choice_expense_category = int(input(f"Please enter a category number {value_range}: ")) - 1
            except ValueError:
                print(f'Error: Please enter an integer ie: {value_range}')
                add_expense()
            except Exception as e:
                print(f"An unexpected error has occured: {e}")
                add_expense()

            if choice_expense_category in range(len(expense_category)):
                new_expense = Expense(
                    name=expense_name, 
                    category=expense_category[choice_expense_category], 
                    amount=expense_amount,
                    date = datetime.now().strftime('%Y-%m-%d')
                )
                return new_expense
            else:
                print("You have entered an invalid option. Try again!")
            

class Income(BudgetManager):
    def __init__(self, name, amount, category, date):
        self.amount = amount
        self.category = category
        self.name = name
        self.date = date

    def add_income():
        print("\nGetting User Income")
        print("----------------------")

        income_name = input("Enter the income name: ")
        income_amount = float(input("Enter the income amount: $"))

        income_category = [
            "💼 Salary",
            "🎁 Gift",
            "🤑 Investment Income",
            "🌟 Other Income"
        ]

        for i, category in enumerate(income_category):
            print(f'{i + 1}. {category}')

        value_range = f'(1 - {len(income_category)})'
        choice_of_category = int(input(f'Please enter a category number {value_range}: ')) - 1

        if choice_of_category in range(len(income_category)):
            new_income = Income(
                name=income_name, 
                category=income_category[choice_of_category], 
                amount=income_amount,
                date = datetime.now().strftime('%Y-%m-%d')
            )
            return new_income
        else:
            print("You have entered an invalid option. Try again!")

def add_expense():
    print("\nGetting User Expense")
    print("--------------------")
    
    expense_name = input("Enter expense name: ")
    try:
        expense_amount = float(input("Enter the expense amount: $"))
    except ValueError:
        print("Error: Please enter a dollar amount ie: 4.95")
        add_expense()
    except Exception as e:
        print(f'An unexpected error occured: {e}')
        add_expense()

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
            print(f'{counter}. {category}')
            counter += 1
    
        value_range = f'(1 - {len(expense_category)})'
        try:
            choice_expense_category = int(input(f"Please enter a category number {value_range}: ")) - 1
        except ValueError:
            print(f'Error: Please enter an integer ie: {value_range}')
            add_expense()
        except Exception as e:
            print(f"An unexpected error has occured: {e}")
            add_expense()

        if choice_expense_category in range(len(expense_category)):
            new_expense = Expense(
                name=expense_name, 
                category=expense_category[choice_expense_category], 
                amount=expense_amount
            )
            return new_expense
        else:
            print("You have entered an invalid option. Try again!")
            

def add_income():
    print("\nGetting User Income")
    print("----------------------")

    income_name = input("Enter the income name: ")
    income_amount = float(input("Enter the income amount: $"))

    income_category = [
        "💼 Salary",
        "🎁 Gift",
        "🤑 Investment Income",
        "🌟 Other Income"
    ]

    for i, category in enumerate(income_category):
        print(f'{i}. {category}')

    value_range = f'(1 - {len(income_category)})'
    choice_of_category = int(input(f'Please enter a category number {value_range}: ')) - 1

    if choice_of_category in range(len(income_category)):
        new_income = Income(
            name=income_name, 
            category=income_category[choice_of_category], 
            amount=income_amount
        )
        return new_income
    else:
        print("You have entered an invalid option. Try again!")
