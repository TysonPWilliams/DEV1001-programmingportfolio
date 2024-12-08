from file_operations import load_financial_data
from financial_operations import *
from display_data import display_data

load_financial_data('financial_data.csv')

while True:
    print("Welcome to the Budget Manager!")
    print("------------------------------")
    print("1. Enter an income")
    print("2. Enter an expense")
    print("3. Display all income and expenses")
    print("4. Exit the application")

    choice = input("Please type in a number from the options above: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice =="3":
        display_data()
    elif choice == "4":
        quit()
    else:
        print("Your choice is invalid, try again!")