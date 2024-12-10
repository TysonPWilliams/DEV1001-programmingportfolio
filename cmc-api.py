from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import secret
from pprint import pprint as pp
# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
# parameters = {
#   'start':'1',
#   'limit':'5000',
#   'convert':'USD'
# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': secret.API_KEY,
# }

# session = Session()
# session.headers.update(headers)

# try:
#   response = session.get(url, params=parameters)
#   data = json.loads(response.text)
#   print("Data successfully loaded")
# #   print(data)
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(f'An unexpected error occured: {e}')


class CMC:
    # https://coinmarketcap.com/api/documentation/v1/
    
    def __init__(self, token):
        self.apiurl = "https://pro-api.coinmarketcap.com"
        self.headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': token}
        self.session = Session()
        self.session.headers.update(self.headers)

    def get_all_coins(self):
       url = self.apiurl + "/v1/cryptocurrency/map"
       r = self.session.get(url)
       data = r.json()['data']
       return data
    
    def get_price(self, symbol):
       url = self.apiurl + "/v2/cryptocurrency/quotes/latest"
       parameters = {'symbol': symbol}
       r = self.session.get(url, params=parameters)
       data = r.json()['data']
       return data
    

cmc = CMC(secret.API_KEY)

pp(cmc.get_price('BTC'))
