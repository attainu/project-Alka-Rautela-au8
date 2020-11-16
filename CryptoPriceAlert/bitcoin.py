import requests
from timestampConverter import convertTime

# for more info
from popularCryptoUpdates import popularCryptoUpdate

# importing parent class
from cryptoParent import CryptoCurrency


class Bitcoin(CryptoCurrency):
    def __init__(self, lowerBoundPrice=10000, upperBoundPrice=16000):
        super().__init__()
        # self.currentPrice = None
        self.lowerBoundPrice = lowerBoundPrice
        self.upperBoundPrice = upperBoundPrice

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
    x = input('Do you wanna set upper and lower limit? y/n: ').upper()
    if x == 'Y':
        lowerLimit = float(input('lower limit: '))
        upperLimit = float(input('upper limit: '))
        if lowerLimit >= upperLimit:
            print('invalid limits!')
            return bitcoin()
        else:
            B = Bitcoin(lowerLimit, upperLimit)
    elif x != 'N':
        print('invalid input')
        return bitcoin()

    priceAndTime = []
    count = 0
    while count < 5:
        data = B.getBitcoinPrice()
        priceAndTime.append(data)
        count += 1
    B.dailyTelegramNotification(priceAndTime, 'Bitcoin')

    y = input('Do you wanna know about other coins? y/n: ').upper()
    if y == 'Y':
        return popularCryptoUpdate('BTCZ20', B.key, B.applet3)
    return


try:
    bitcoin()
except ValueError:
    print('invalid inputs!')
