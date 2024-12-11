from cmc_api import CMC
import secret
import display_data
import csv

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
            pass
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

    with open(path, 'a') as file:
        fieldnames = ['BTC Added']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'BTC Added': f'{BTC_added}'})
        input("------Press Enter to Continue------")


    