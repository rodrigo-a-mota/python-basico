import requests
import json

city = input('Escreva sua cidade:')

request = (requests.get('https://pro.openweathermap.org/data/2.5/forecast/climate?q='+city+'&appid=8cc0dba93e3cf352babfb5b24e332658'))
data    = json.loads(request.text)

print('Condição do tempo: ', data)

# API não responde corretamente

