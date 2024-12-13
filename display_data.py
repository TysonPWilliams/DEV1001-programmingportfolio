from file_operations import *
from financial_operations import Expense, Income
import csv
import crypto_operations
from tabulate import tabulate

def display_data():
    
    with open('expense_data.csv', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row['Name'],row['Category'],row['Amount'])

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


def summarise_expenses():
    print("Summarising user expenses!")

    
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        
        for line in reader:
            print(line)

def display_csv_as_table():
    """
    Reads a CSV file and displays it's content as a table
    """
    with open('crypto.csv', 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = [row for row in reader]
    
    print(tabulate(rows, headers=headers, tablefmt="grid"))