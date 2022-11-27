import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  secret_key: ${{ secrets.SuperSecret }},
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  for i in data['data']:
    print("id "+str(i['id'])+"\n")
    print("quote"+ str(i['quote'])+"\n")
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
