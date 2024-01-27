import requests
import json

city = input('Escreva sua cidade:')

request = (requests.get('https://pro.openweathermap.org/data/2.5/forecast/climate?q='+city+'&appid='))
data    = json.loads(request.text)

print('Condição do tempo: ', data)

# API não responde corretamente

