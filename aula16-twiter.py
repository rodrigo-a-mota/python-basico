import oauth2
import json
import pprint
import urllib

consumer_key        = ''
consumer_secret     = ''

token_key           = ''
token_secret        = ''

consumer            = oauth2.Consumer(consumer_key, consumer_secret)
token               = oauth2.Token(token_key, token_secret)
client              = oauth2.Client(consumer, token)

request             = client.request('https://api.twitter.com/2/tweets/search/recent')
twitter_result      = json.loads(request[1].decode())

pprint.pprint(twitter_result)

# api não deixou eu fazer um projeto App para usa-lá

