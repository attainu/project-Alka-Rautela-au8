import requests

popular_coins = ['BTCZ20', 'ETHZ20', 'YFIUSDT', 'YFIIUSDT', 'LINKUSDT']
headers = {
    'Accept': 'application/json'
}


def getDetails(popular_coins, coin_name):
    all_coin_info = {}
    for i in popular_coins:
        if i != coin_name:
            r = requests.get('https://www.bitfex.com/api/v1/public/spot_price', params={
                'contract_symbol': i
            }, headers=headers)
            data = r.json()
            all_coin_info[i] = data
    return all_coin_info


def popularCryptoUpdate(currentCoin, key, applet_name):
    coin_dictionary = getDetails(popular_coins, currentCoin)
    dataToBePrinted = ''
    for i in coin_dictionary.keys():
        name = i
        price = f"${coin_dictionary[i]['spot_price']}"

        print(f'{name} --> {price}')

        dataToBePrinted += name + " --> " + price + '<br>'
    url = f'https://maker.ifttt.com/trigger/{applet_name}/with/key/{key}'
    data = {
        'value1': dataToBePrinted
    }
    r = requests.post(url=url, data=data)
