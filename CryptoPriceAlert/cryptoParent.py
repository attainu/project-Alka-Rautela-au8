import requests


class CryptoCurrency:
    def __init__(self):
        self.key = 'jGMUjkHpsNi6KkZfYVnqDhAx6H3suziJl8S0ihsiunt'
        self.applet1 = 'crypto_latest_price'
        self.applet2 = 'alert'
        self.applet3 = 'popularCrypto'
        self.alert_low_sent = False
        self.alert_high_sent = False

    # GET REQUEST
    def dailyTelegramNotification(self, info_arr, coin_name):
        # ifttt price alert, post request
        # print(info_arr)
        url = f'https://maker.ifttt.com/trigger/{self.applet1}/with/key/{self.key}'
        data = {
            'value1': f'{info_arr[0][1]} : <b>${info_arr[0][0]}</b> <br> {info_arr[1][1]} : <b>${info_arr[1][0]}</b>',
            'value2': f'{info_arr[2][1]} : <b>${info_arr[2][0]}</b> <br> {info_arr[3][1]} : <b>${info_arr[3][0]}</b> <br> {info_arr[4][1]} : <b>${info_arr[4][0]}</b>',
            'value3': f'{coin_name}'
        }

        r = requests.post(url=url, data=data)

    def priceAlert(self, coin_name, crypto_price, alert_message):
        url = f'https://maker.ifttt.com/trigger/{self.applet2}/with/key/{self.key}'
        data = {
            'value1': f'${crypto_price}',
            'value2': alert_message,
            'value3': coin_name,
        }
        r = requests.post(url=url, data=data)
        print('Alert Alert')

    def lowerBoundAlert(self, crypto_price, coin_name):
        # send ifttt post request (Time to buy)
        self.alert_low_sent = True
        m = f"below threshold price <br> it's time to <b>BUY<b> {coin_name}"
        self.priceAlert(coin_name, crypto_price, m)

    def upperBoundAlert(self, crypto_price, coin_name):
        # send ifttt post request (Time to sell)
        self.alert_high_sent = True
        m = f"above threshold price <br> it's time to <b>SELL<b> {coin_name}"
        self.priceAlert(coin_name, crypto_price, m)

    # checking for alert
    def checkPrice(self, price, coin_name):
        if self.lowerBoundPrice >= price and not self.alert_low_sent:
            self.lowerBoundAlert(price, coin_name)
        elif self.upperBoundPrice <= price and not self.alert_high_sent:
            self.upperBoundAlert(price, coin_name)
