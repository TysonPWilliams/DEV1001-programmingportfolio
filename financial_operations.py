class BudgetManager():
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date
    
    def add_income(self, amount, category, date):
        pass

    def add_expense(self, amount, category, date):
        pass

class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount
    
    def __str__(self):
        return f"Expense: {self.name}, {self.category}, ${self.amount:.2f}"

class Transactions(BudgetManager):
    def __init__():
        pass

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
