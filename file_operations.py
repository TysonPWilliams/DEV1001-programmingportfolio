import csv

path = "expense_data.csv"
def load_financial_data(path):
    """
    Loads existing data from CSV file

    paramaters:
        path: Path to the CSV file

    return:
        financial data consisting of income, expenses, category and date
    """
    try:
        with open(path) as file:
            financial_data = csv.reader(file)

        return financial_data 
    except Exception as e:
        print(f'An unexpected error occured: {e}')
    
def save_expense_to_file(expense, path):
    path = "expense_data.csv"
    print(f'Saving User Expense: {expense} to {path}')


    with open(path, 'a', newline='') as file:
        fieldnames = ['Name','Category','Amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'Name': f'{expense.name}','Category': f'{expense.category}', 'Amount': f'{expense.amount}'})



def save_income_to_file(income):
    path = "income_data.csv"
    print(f'Saving User Income: {income} to {path}')

    with open(path, 'a') as file:
        fieldnames = ['Name', 'Category', 'Amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'Name': f'{income.name}', 'Category': f'{income.category}', 'Amount': f'{income.amount}'})
