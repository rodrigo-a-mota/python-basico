# Beautiful Soup 4 BS4 pip installs4

import requests

cabecalho = {
    'User-agent': 'Windows 12',
    'Referer': 'https://google.com'
}

meus_cookies = {
    'Ultima-visita': '10-10-2022'
}

dados = {
    'username': 'rodigo',
    'password': 'lsls2023'
}

try:
    request_get = requests.post(
        'https://putsreq.com/aYZDqBNQ7UUlTdCsAgwm',
        headers=cabecalho,
        cookies=meus_cookies,
        data=dados
    )

    print(request_get.text)

except Exception as error:
    print("Requisição deu erro: ", error)
