#%%
# imports
import requests
import json

#%%
currency_from = 'USD'
currency_to = 'BRL'
url = 'https://economia.awesomeapi.com.br/json/last/' + currency_from + '-' + currency_to
resp = requests.get(url)

#%%
if resp:
    print(resp.text)
else:
    print('Erro! Resposta: {}'.format(resp.text))

#%%
resp_json = json.loads(resp.text)

#%%
currency_data = resp_json[currency_from+currency_to]
print(f"A conversão do USD X para BRL é {currency_data['bid']}.")

#%%
# FAZENDO UMA FUNÇÃO PARA SIMPLIFICAR AS COISAS.
def cotacao(value,currency_from,currency_to):
    try:
        url = f'https://economia.awesomeapi.com.br/json/last/{currency_from}-{currency_to}'
        resp = requests.get(url)    
        currency_data = json.loads(resp.text)[currency_from+currency_to]
        print(f"{currency_from} {value:.2f} >> {currency_to} {value * float(currency_data['bid']):.2f}")
    except:
        print(f"Error: {currency_from} >> {currency_to}")
#%%
cotacao(20,'USD','BRL')

# %%
lst = ['USD','PEN','ARS','BATATA','MXN']
for c in lst:
    cotacao(20,c,'BRL')

# %%
def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} failed.")
    return inner_func

@error_check
def cotacao2(value,currency_from,currency_to):
    url = f'https://economia.awesomeapi.com.br/json/last/{currency_from}-{currency_to}'
    resp = requests.get(url)    
    currency_data = json.loads(resp.text)[currency_from+currency_to]
    print(f"{currency_from} {value:.2f} >> {currency_to} {value * float(currency_data['bid']):.2f}")

#%%
lst = ['USD','PEN','ARS','BATATA','MXN']
for c in lst:
    cotacao2(20,c,'BRL')

# %%
import backoff

# %%
@backoff.on_exception(backoff.expo, (KeyError), max_tries=2)
def cotacao3(value,currency_from,currency_to):
    url = f'https://economia.awesomeapi.com.br/json/last/{currency_from}-{currency_to}'
    resp = requests.get(url)    
    currency_data = json.loads(resp.text)[currency_from+currency_to]
    print(f"{currency_from} {value:.2f} >> {currency_to} {value * float(currency_data['bid']):.2f}")

# %%
lst = ['USD','PEN','ARS','BATATA','MXN']
for c in lst:
    cotacao3(20,c,'BRL')
# %%
# LOGS
import logging

# %%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# %%
@backoff.on_exception(backoff.expo, (KeyError), max_tries=2)
def cotacao_log(value,currency_from,currency_to):
    log.debug(f'Exchange Rate: {currency_from}-{currency_to}')
    log.info(f'Value: {value}')
    url = f'https://economia.awesomeapi.com.br/json/last/{currency_from}-{currency_to}'
    resp = requests.get(url)
    currency_data = json.loads(resp.text)[currency_from+currency_to]
    #log.error('Key Error.')
    print(f"{currency_from} {value:.2f} >> {currency_to} {value * float(currency_data['bid']):.2f}")

# %%
lst = ['USD','PEN','ARS','BATATA','MXN']
for c in lst:
    cotacao_log(20,c,'BRL')

# %%
