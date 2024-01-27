from twitter import Twitter

consumer_key        = 'Z3k8WFxb2jsypIVGlrM5WFKS2'
consumer_secret     = 'tC3lviFlYMWYk9u6kRiatOWBQUN63KWqabMUwShiRORHwhGbCg'

token_key           = '1746922138743771136-v2ce5iTKFTGLS7O2o4diKNUa0LQ17n'
token_secret        = 'Q4S3JSW2IS5MTBdEwpCBUiWLTOtL44Zx853Sb0PJAV9gv'

twitter             = Twitter(consumer_key, consumer_secret, token_key, token_secret)
response            = twitter.tweet('vamos testar a lib')

print(response)
