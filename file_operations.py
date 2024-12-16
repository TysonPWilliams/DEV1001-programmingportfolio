import csv




    
def save_expense_to_file(expense, path):
    print(f'Saving User Expense: {expense} to {path}')

    try:
        with open(path, 'a', newline='') as file:
            fieldnames = ['Name','Category','Amount', 'Date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'Name': f'{expense.name}','Category': f'{expense.category}', 'Amount': f'{expense.amount}', 'Date': f'{expense.date}'})
    except PermissionError:
        print(f"You don't have permission to access {path}")
    except Exception as e:
        print(f'An unexpected error occured: {e}')



def save_income_to_file(income, path):
    print(f'Saving User Income: {income} to {path}')
    
    try:
        with open(path, 'a') as file:
            fieldnames = ['Name', 'Category', 'Amount', 'Date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'Name': f'{income.name}', 'Category': f'{income.category}', 'Amount': f'{income.amount}', 'Date': f'{income.date}'})
    except PermissionError:
        print(f"You don't have permission to access {path}")
    except Exception as e:
        print(f'An unexpected error occured: {e}')

import csv

class FileOperations:
    """A class for saving data (expenses and incomes) to separate CSV files."""

    def __init__(self, expense_path="expense_data.csv", income_path="income_data.csv"):
        """
        Initialises the class with default paths for expense and income files.

        Args:
            expense_path (str, optional): The path to save expense data. Defaults to "expense_data.csv".
            income_path (str, optional): The path to save income data. Defaults to "income_data.csv".
        """

        self.expense_path = expense_path
        self.income_path = income_path

    def save_data(self, data, data_type, path):
        """
        Saves data (expense or income) to a specified CSV file.

        Args:
            data (object): The data object (expense or income) to be saved.
                Expected to have attributes 'name', 'category', 'amount', and 'date'.
            data_type (str): The type of data being saved ("expense" or "income").
            path (str): The path to the CSV file where data will be saved.
        """

        fieldnames = ['Name', 'Category', 'Amount', 'Date']

        try:
            with open(path, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow({
                    'Name': f'{data.name}',
                    'Category': f'{data.category}',
                    'Amount': f'{data.amount}',
                    'Date': f'{data.date}'
                })
            print(f'Successfully saved {data_type} data to {path}')
        except PermissionError:
            print(f"You don't have permission to access {path}")
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

    def save_expense(self, expense):
        """
        Saves expense data to the expense CSV file.

        Args:
            expense (object): The expense data object.
        """

        self.save_data(expense, "expense", self.expense_path)

    def save_income(self, income):
        """
        Saves income data to the income CSV file.

        Args:
            income (object): The income data object.
        """

        self.save_data(income, "income", self.income_path)