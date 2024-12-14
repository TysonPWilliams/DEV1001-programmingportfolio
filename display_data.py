from file_operations import *
from financial_operations import Expense, Income
import csv
import crypto_operations
from tabulate import tabulate

def main_menu():

    print("\nWelcome to the Budget Manager!")
    print("------------------------------")
    print("1. Enter an income")
    print("2. Enter an expense")
    print("3. Display all income and expenses")
    print("4. Access Crypto Menu")
    print("5. Exit the application")
    print("-------------------------------")

    choice = input("Please type in a number from the options above: ")

    if choice == "1":
        income = Income.add_income()
        save_income_to_file(income)
    elif choice == "2":
        expense = Expense.add_expense()
        save_expense_to_file(expense, path)
    elif choice =="3":
        display_data()
    elif choice == "4":
        crypto_operations.crypto_menu()
    elif choice == "5":
        quit()
    else:
        print("Your choice is invalid, try again!")

def display_csv_as_table(path):
    """
    Reads a CSV file and displays it's content as a table
    """
    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = [row for row in reader]
    
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def display_data():
    
    while True:

        print("\nWelcome to the Budget Summary Menu!")
        print("------------------------------")
        print("1. View all income")
        print("2. View all expenses")
        print("3. How am I doing for the month?")
        print("4. What category am I spending the most on?")
        print("5. Return to the main menu")
        print("-------------------------------")

        choice = input("Please type in a number from the options above: ")

        if choice == "1":
            display_csv_as_table('income_data.csv')
            summarise_totals('income_data.csv')
            input("------Please press Enter to continue----")
        elif choice == "2":
            display_csv_as_table('expense_data.csv')
            summarise_totals('expense_data.csv')
            input("------Please press Enter to continue----")
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            main_menu()
        else:
            print("Your choice is invalid, try again!")

        # with open('expense_data.csv', newline='') as file:
        #     reader = csv.DictReader(file)

        #     for row in reader:
        #         print(row['Name'],row['Category'],row['Amount'])

def summarise_totals(path):
    total = 0.0

    with open(path, newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            total += float(row['Amount'])
    
    print(f'The total amount is: ${total:.2f}!')
