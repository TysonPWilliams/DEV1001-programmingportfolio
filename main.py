from file_operations import *
from financial_operations import *
from display_data import display_data, main_menu

load_financial_data('financial_data.csv')

while True:
    
    main_menu()