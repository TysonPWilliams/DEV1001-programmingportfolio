from file_operations import *
import financial_operations as fin_ops
import csv
import crypto_operations
from tabulate import tabulate
from color50 import rgb, constants
from colors import *

def main_menu():
    color_print("\nWelcome to the Budget Manager!", color=heading)
    color_print("------------------------------", color=heading)
    color_print("1. Enter an income")
    color_print("2. Enter an expense")
    color_print("3. Display all income and expenses")
    color_print("4. Access Crypto Menu")
    color_print("5. Exit the application")
    color_print(f"-------------------------------")

    choice = input(heading + f"Please type in a number from the options above: {constants.RESET}")

    if choice == "1":
        fin_ops.Income.add_income()
    elif choice == "2":
        fin_ops.Expense.add_expense()
    elif choice =="3":
        display_data()
    elif choice == "4":
        crypto_operations.crypto_menu()
    elif choice == "5":
        quit()
    else:
        print(f"{error_text}\nYour choice is invalid, try again!{constants.RESET}\n")
        input(f"{primary_text}----Press Enter to Continue----")

def display_csv_as_table(path):
    """
    Reads a CSV file and displays it's content as a table
    """
    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = [row for row in reader]
    
    color_print(tabulate(rows, headers=headers, tablefmt="grid"))

def display_data():
    
    while True:

        color_print("\nWelcome to the Budget Summary Menu!", heading)
        color_print("------------------------------", heading)
        color_print("1. View all income")
        color_print("2. View all expenses")
        color_print("3. How am I doing for the month?")
        color_print("4. What category am I spending the most on?")
        color_print("5. Return to the main menu")
        color_print("-------------------------------", heading)

        choice = input(f"{primary_text}Please type in a number from the options above: ")

        if choice == "1":
            display_csv_as_table('income_data.csv')
            total = summarise_totals('income_data.csv')
            color_print(f'The total amount is: ${total:.2f}!')
            input("------Please press Enter to continue----")
        elif choice == "2":
            display_csv_as_table('expense_data.csv')
            total = summarise_totals('expense_data.csv')
            color_print(f'The total amount is: ${total:.2f}!')
            input("------Please press Enter to continue----")
        elif choice == "3":
            income_summary = summarise_totals('income_data.csv')
            fin_ops.income_expense_calc()
        elif choice == "4":
            max_category = max_category_spending()
            color_print(f'\nYour max category is {max_category[0]} with an amount of ${max_category[1]:.2f}!\n')
            input("--------Press Enter to continue-------")
        elif choice == "5":
            main_menu()
        else:
            print(f"{error_text}Your choice is invalid, try again!")
            input(f'{primary_text}----Press Enter to Continue----')


def summarise_totals(path):
    total = 0.0

    with open(path, newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            total += float(row['Amount'])
    
    return total

def max_category_spending():

    category_totals = {}
    with open('expense_data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['Category']
            amount = float(row['Amount'])
            category_totals[category] = category_totals.get(category, 0) + amount

    max_category = None
    max_amount = 0
    for category, amount in category_totals.items():
        if amount > max_amount:
            max_category = category
            max_amount = amount
    
    return max_category, max_amount