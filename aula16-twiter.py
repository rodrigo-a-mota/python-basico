import oauth2
import json
import pprint
import urllib

consumer_key        = 'Z3k8WFxb2jsypIVGlrM5WFKS2'
consumer_secret     = 'tC3lviFlYMWYk9u6kRiatOWBQUN63KWqabMUwShiRORHwhGbCg'

token_key           = '1746922138743771136-v2ce5iTKFTGLS7O2o4diKNUa0LQ17n'
token_secret        = 'Q4S3JSW2IS5MTBdEwpCBUiWLTOtL44Zx853Sb0PJAV9gv'

consumer            = oauth2.Consumer(consumer_key, consumer_secret)
token               = oauth2.Token(token_key, token_secret)
client              = oauth2.Client(consumer, token)

request             = client.request('https://api.twitter.com/2/tweets/search/recent')
twitter_result      = json.loads(request[1].decode())

pprint.pprint(twitter_result)

# api não deixou eu fazer um projeto App para usa-lá

