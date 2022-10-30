#%%
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# %%
url = 'https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina={}'

# %%
i = 1
resp = requests.get(url.format(i))
soup = bs(resp.text)
# %%
properties = soup.find_all('a',{'class': 'property-card__content-link js-card-title'})
prop_count = float(soup.find('strong',{'class': 'results-summary__count js-total-records'}).text.replace('.',''))
# %%
prop_count
# %%
df = pd.DataFrame(columns=['description','address','area','bedroom','bathroom','garage','price','maintenance_fee','prop_link'])
#%%
for prop in properties:
    try:
        description = prop.find('span',{'class': 'property-card__title'}).text.strip()
    except:
        description = None
    try:
        address = prop.find('span', {'class': 'property-card__address'}).text.strip()
    except:
        address = None
    try:
        area = prop.find('span', {'class': 'property-card__detail-area'}).text.strip()
    except:
        area = None
    try:
        bedroom = prop.find('li', {'class': 'property-card__detail-room'}).span.text.strip()
    except:
        bedroom = None
    try:
        bathroom = prop.find('li', {'class': 'property-card__detail-bathroom'}).span.text.strip()
    except:
        bathroom = None
    try:
        garage = prop.find('li', {'class': 'property-card__detail-garage'}).span.text.strip()
    except:
        garage = None
    try:
        price = prop.find('div', {'class': 'js-property-card-prices'}).p.text.strip()
    except:
        price = None
    try:
        maintenance_fee = prop.find('strong', {'class': 'js-condo-price'}).text.strip()
    except:
        maintenance_fee = None
    try:
        prop_link = 'https://www.vivareal.com.br' + prop['href']
    except:
        prop_link = None

    df.loc[df.shape[0]] = [description,address,area,bedroom,bathroom,garage,price,maintenance_fee,prop_link]
# %%
df.head()


# %%
#TUDO NUM LOOP SÓ:
url = 'https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina={}'
resp = requests.get(url.format(1))
soup = bs(resp.text)
prop_count = float(soup.find('strong',{'class': 'results-summary__count js-total-records'}).text.replace('.',''))
print(f'Total of properties:{prop_count}.\n')

i = 0
df = pd.DataFrame(columns=['description','address','area','bedroom','bathroom','garage','price','maintenance_fee','prop_link'])
while prop_count > df.shape[0]:
    i += 1
    print(f"i value: {i} \t\t Properties in DataFrame: {df.shape[0]}")
    resp = requests.get(url.format(i))
    soup = bs(resp.text, features='html.parser')
    properties = soup.find_all('a',{'class': 'property-card__content-link js-card-title'})
    for prop in properties:
        try:
            description = prop.find('span',{'class': 'property-card__title'}).text.strip()
        except:
            description = None
        try:
            address = prop.find('span', {'class': 'property-card__address'}).text.strip()
        except:
            address = None
        try:
            area = prop.find('span', {'class': 'property-card__detail-area'}).text.strip()
        except:
            area = None
        try:
            bedroom = prop.find('li', {'class': 'property-card__detail-room'}).span.text.strip()
        except:
            bedroom = None
        try:
            bathroom = prop.find('li', {'class': 'property-card__detail-bathroom'}).span.text.strip()
        except:
            bathroom = None
        try:
            garage = prop.find('li', {'class': 'property-card__detail-garage'}).span.text.strip()
        except:
            garage = None
        try:
            price = prop.find('div', {'class': 'js-property-card-prices'}).p.text.strip()
        except:
            price = None
        try:
            maintenance_fee = prop.find('strong', {'class': 'js-condo-price'}).text.strip()
        except:
            maintenance_fee = None
        try:
            prop_link = 'https://www.vivareal.com.br' + prop['href']
        except:
            prop_link = None
        df.loc[df.shape[0]] = [description,address,area,bedroom,bathroom,garage,price,maintenance_fee,prop_link]
    
# %%
df
# %%
df.to_csv('imoveis.csv',sep=';',index=False)
# %%
