import requests
import json
import time
import datetime

while True:

    req         = requests.get('https://economia.awesomeapi.com.br/json/last/USD')
    dictionary  = json.loads(req.text)

    print('Cotação de ', datetime.datetime.now())
    print('Dólar: ', dictionary['USDBRL']['high'])

    time.sleep(2)
