from datetime import datetime
import tweepy
import requests
import json

now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M")

#CoinGecko API
btc_request = requests.get("#CoinGeckoAPI", headers = {'accept': 'application/json'})
btc_price = str(btc_request.json()['bitcoin']['eur'])
btc_24_round = round(btc_request.json()['bitcoin']['eur_24h_change'],2)
btc_24_change = str(btc_24_round)


eth_request = requests.get("#CoinGeckoAPI", headers = {'accept': 'application/json'})
eth_price = str(eth_request.json()['ethereum']['eur'])
eth_24_round = round(eth_request.json()['ethereum']['eur_24h_change'],2)
eth_24_change = str(eth_24_round)


ltc_request = requests.get("#CoinGeckoAPI", headers = {'accept': 'application/json'})
ltc_price = str(ltc_request.json()['litecoin']['eur'])
ltc_24_round = round(ltc_request.json()['litecoin']['eur_24h_change'],2)
ltc_24_change = str(ltc_24_round)

if btc_24_round > 0 :
    btc_emoji = "🟢"
else:
    btc_emoji = "🔴"

if eth_24_round > 0 :
    eth_emoji = "🟢"
else:
    eth_emoji = "🔴"

if ltc_24_round > 0 :
    ltc_emoji = "🟢"
else:
    ltc_emoji = "🔴"


#Twitter API
consumer_key = 'Twitter consumer_key'
consumer_secret = 'Twitter consumer_secret'
access_token = 'Twitter access_token'
access_token_secret = 'Twitter access_token_secret'


def AuthHandler():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        return auth
    except Exception as e:
        return None

oauth = AuthHandler()
api = tweepy.API(oauth)
api.update_status('Crypto Price For Today ' + current_time + ' : '
'\n#BTC: '+ btc_price + ' € , ('+ btc_24_change + ' %)' + btc_emoji + '💰'
'\n#ETH : '+ eth_price + ' € , ('+ eth_24_change + ' %)' + eth_emoji + '💰'
'\n#LTC : '+ ltc_price + ' € , ('+ ltc_24_change + ' %)' + ltc_emoji + '💰'
'\nCrypto #ToTheMoon 🚀')

print("Twitter post has been posted, Time:",current_time)
