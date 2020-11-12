import requests
from timestampConverter import convertTime

# importing parent class
from cryptoParent import CryptoCurrency


class Bitcoin(CryptoCurrency):
    def __init__(self):
        super().__init__()
        self.currentPrice = None
        self.lowerBoundPrice = 10000
        self.upperBoundPrice = 15000

    def getBitcoinPrice(self):
        # get request for bitcoin rest API
        headers = {
            'Accept': 'application/json'
        }

        r = requests.get('https://www.bitfex.com/api/v1/public/spot_price', params={
            'contract_symbol': 'BTCZ20'
        }, headers=headers)

        data = r.json()

        # converting time into human readable format
        td = convertTime(str(data['timestamp']))

        # latest data
        print(td, float(data['spot_price']))

        # check for high and low for alert
        self.checkPrice(float(data['spot_price']), 'bitcoin')

        # now select necessary data and return
        filtered_data = [data['spot_price'], td]
        return filtered_data


def bitcoin():
    B = Bitcoin()
    priceAndTime = []
    count = 0
    while count < 5:
        data = B.getBitcoinPrice()
        priceAndTime.append(data)
        count += 1
    B.dailyTelegramNotification(priceAndTime, 'Bitcoin')


bitcoin()
