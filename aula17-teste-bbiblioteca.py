from twitter import Twitter

consumer_key        = ''
consumer_secret     = ''

token_key           = ''
token_secret        = ''

twitter             = Twitter(consumer_key, consumer_secret, token_key, token_secret)
response            = twitter.tweet('vamos testar a lib')

print(response)
