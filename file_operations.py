import csv

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
    