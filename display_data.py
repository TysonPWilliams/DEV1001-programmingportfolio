from file_operations import load_financial_data, path
import csv

def display_data():
    
    with open('financial_data.csv', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row['Name'],row['Category'],row['Amount'])

