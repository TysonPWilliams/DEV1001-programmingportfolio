from file_operations import load_financial_data, path, save_expense_to_file
from financial_operations import add_income, add_expense
import csv

def display_data():
    
    with open('financial_data.csv', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row['Name'],row['Category'],row['Amount'])

def main_menu():

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
        summarise_expenses()
    elif choice == "4":
        quit()
    else:
        print("Your choice is invalid, try again!")


def summarise_expenses():
    print("Summarising user expenses!")

    
    with open(path, 'r') as file:
        reader = csv.reader(file)
        
        for line in reader:
            print(line)