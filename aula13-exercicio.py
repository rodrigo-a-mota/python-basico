import requests
import json


def request(titulo):
    try:

        pages = int(json.loads(
            requests.get('https://www.omdbapi.com/?apikey=a024e553&s=' + titulo + '&type=movie').text
        )['totalResults']) / 10

        request_for_page(pages, titulo)

    except Exception as error:

        print('Erro na conexão: ', error)


def request_for_page(pages, titulo):
    i = 0
    while i <= pages:
        print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        if (i + 1) <= 9\
                :
            print('|||||||||||||||||||||||||      ', i + 1, '      ||||||||||||||||||||||||||||||||')
        else:
            print('|||||||||||||||||||||||||      ', i + 1, '      |||||||||||||||||||||||||||||||')
        print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        print(json.loads(
            requests.get('https://www.omdbapi.com/?apikey=a024e553&s=' + titulo + '&type=movie&page=' + str(i + 1)).text))

        i += 1


request(input('Escreva o nome de um filme: '))
