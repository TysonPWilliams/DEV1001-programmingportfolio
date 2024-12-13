import requests
import csv
import secret

def get_btc_price():
    """
    Fetches the current BTC price from CoinMarketCap API.
    """

    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    parameters = {
        "symbol": "BTC",
        "convert": "AUD"
    }
    headers = {
        "X-CMC_PRO_API_KEY": secret.API_KEY # Replace with your CoinMarketCap API key
    }
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    btc_price = data['data']['BTC'][0]['quote']['AUD']['price']
    return btc_price

def read_csv_data(filename):
    """Reads the CSV file and extracts the user's BTC holdings."""
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            btc_holdings = float(row[0])
            return btc_holdings

def calculate_aud_value(btc_price, btc_holdings):
    """Calculates the total AUD value of the user's BTC holdings."""
    aud_value = btc_price * btc_holdings
    return aud_value

if __name__ == "__main__":
    btc_price = get_btc_price()
    btc_holdings = read_csv_data("user_data.csv")
    total_aud_value = calculate_aud_value(btc_price, btc_holdings)
    print(f"Your BTC holdings are worth approximately AUD {total_aud_value:.2f}")