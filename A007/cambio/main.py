import requests
import json
from datetime import date, datetime

def fx(value,currency_from,currency_to):
    url = f'https://economia.awesomeapi.com.br/json/last/{currency_from}-{currency_to}'
    resp = requests.get(url)    
    currency_data = json.loads(resp.text)[currency_from+currency_to]
    return(value * float(currency_data['bid']))

with open('cambio.csv','a') as f:
    f.write(f"{datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M')};{fx(1,'USD','BRL')}\n")