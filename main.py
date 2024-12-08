from file_operations import *
from financial_operations import *
from display_data import display_data

load_financial_data('financial_data.csv')

while True:
    print("\nWelcome to the Budget Manager!")
    print("------------------------------")
    print("1. Enter an income")
    print("2. Enter an expense")
    print("3. Display all income and expenses")
    print("4. Exit the application")

    choice = input("Please type in a number from the options above: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        expense = add_expense()
        save_expense_to_file(expense, path)
    elif choice =="3":
        display_data()
    elif choice == "4":
        quit()
    else:
        print("Your choice is invalid, try again!")