import csv

path = "financial_data.csv"
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
            financial_data = csv.DictReader(file)

        return financial_data 
    except Exception as e:
        print(f'An unexpected error occured: {e}')
    
def save_expense_to_file(expense, path):
    print(f'Saving User Expense: {expense} to {path}')

    with open(path, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['Name','Category', 'Amount'])
        for row in expense:
            writer.writerow(expense.to_dict())


    # for row in csv.writer(open(path)):
    #     expense.name = row[0]
    #     expense.category = row[1]
    #     expense.amount = row[2]
