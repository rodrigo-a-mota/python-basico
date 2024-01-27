import requests
import json


def request(titulo):
    try:

        return json.loads(requests.get('https://www.omdbapi.com/?apikey=a024e553&t=' + titulo + '&type=movie').text)

    except Exception as error:

        print('Erro na conexão: ', error)
        return None


def details(data):

    if data['Response'] == 'False':

        print('Filme não encontrado')

    else:

        print('\nTitulo:', data['Title'])
        print('Ano:', data['Year'])
        print('Diretor:', data['Director'])
        print('Atores:', data['Actors'])
        print('Nota', data['imdbRating'])
        print('Prêmios', data['Awards'])
        print('Poster', data['Poster'] + '\n')


close = False

while not close:

    option = input('Escreva o nome de um filme ou SAIR para fechar: ')

    if option == 'SAIR':
        close = True
        print('Saindo...')
    else:
        details(request(option))
