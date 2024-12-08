class BudgetManager():
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date
    
    def add_income(self, amount, category, date):
        pass

    def add_expense(self, amount, category, date):
        pass


class Transactions(BudgetManager):
    def __init__():
        pass

def add_expense():
    print("\nGetting User Expense")
    print("--------------------")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter the expense amount: $"))
    expense_category = [
        "🍔 Food",
        "🏠 Home",
        "🚗 Fuel",
        "🎸 Entertainment",
        "🌟 Misc"
    ]

    counter = 1
    for category in expense_category:
        print(f'{counter}. {category}')
        counter += 1
    
    choice_expense_category = int(input("Please choose a category from the list above: "))
    print(f'You have entered: {expense_name}, ${expense_amount}, {expense_category[choice_expense_category - 1]}')

def add_income():
    print("\nAdding some income! 💵")

def summarise_expenses():
    print("Summarising user expenses!")