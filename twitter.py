import json
import oauth2
import oauth2
import urllib

class Twitter:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.conexao(consumer_key, consumer_secret, token_key, token_secret)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):

        self.consumer   = oauth2.Consumer(consumer_key, consumer_secret)
        self.token      = oauth2.Token(token_key, token_secret)
        self.cliente    = oauth2.Client(self.consumer, self.token)

        return self.cliente

    def tweet(self, novo_tweet):

        query_codificada    = urllib.parse.quote(novo_tweet, safe='')
        requisicao          = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status='+query_codificada, method='POST')
        decodificar         = requisicao[1].decode()
        objeto              = json.loads(decodificar)
