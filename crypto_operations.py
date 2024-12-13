from cmc_api import CMC
import display_data
import csv
import btc_calculations
from datetime import datetime

path = 'crypto.csv'

def crypto_menu():

    while True:

        print("\n\n------Cryptocurrency Main Menu--------")
        print("1. Add BTC to your portfolio")
        print("2. Display the value of your BTC portfolio")
        print("3. Remove BTC from your portfolio")
        print("4. Quit to the main menu")
        print("---------------------------------------")
        choice = int(input("Please enter a number from the above menu: "))

        if choice == 1:
            add_crypto()
        elif choice == 2:
            print("------------------------------------")
            print("Calculating the value of you BTC holdings\n")
            btc_price = btc_calculations.get_btc_price()
            btc_holdings = btc_calculations.read_csv_data('crypto.csv')
            total_aud_value = btc_calculations.calculate_aud_value(btc_price, btc_holdings)
            print(f"Your BTC holdings are worth approximately AUD ${total_aud_value:.2f}")
            input("------Press Enter to Continue-------")
        elif choice == 3:
            pass
        elif choice == 4:
            display_data.main_menu()
        else:
            print("\n\nYou have entered an invalid option, try again!")

def add_crypto():

    print("-------------------------------")
    print("Adding BTC to your portfolio!")
    BTC_added = float(input("How much BTC are you adding: "))
    print("-------------------------------")
    print(f'Adding {BTC_added} BTC to your portfolio!')

    with open(path, 'a', newline='') as file:
        fieldnames = ['BTC Added', 'Date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        current_date = datetime.now().strftime('%Y-%m-%d')
        writer.writerow({'BTC Added': BTC_added, 'Date': current_date})
        input("------Press Enter to Continue------")


    