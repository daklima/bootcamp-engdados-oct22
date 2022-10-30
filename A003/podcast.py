#%%
import requests
from bs4 import BeautifulSoup as bs
import logging
import pandas as pd
# %%
url = 'https://portalcafebrasil.com.br/todos/podcasts/'
#%%
resp = requests.get(url)
# %%
resp.text
# %%
soup = bs(resp.text)
# %%
soup
# %%
soup.find('h5')
# %%
soup.find('h5').text
#%%
soup.find('h5').a['href']
# %%
podcasts = soup.find_all('h5')
for p in podcasts:
    print(f"EP: {p.text} - Link: {p.a['href']}")
# %%
url = 'https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true'
#%%
def get_podcast(url):
    resp = requests.get(url)
    soup = bs(resp.text)
    return soup.find_all('h5')
# %%
get_podcast(url.format(1))
#%%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# %%
i = 1
lst_podcast = []
lst_get = get_podcast(url.format(i))
log.debug(f"{len(lst_get)} EPs coletados do link: {url.format(i)}")
while len(lst_get) > 0:
    lst_podcast += lst_get
    i += 1
    lst_get = get_podcast(url.format(i))
    log.debug(f"{len(lst_get)} EPs coletados do link: {url.format(i)}")

# %%
len(lst_podcast)

# %%
df = pd.DataFrame(columns = ['name','link'])
for i in lst_podcast:
    df.loc[df.shape[0]] = [i.text, i.a['href']]
# %%
df.head()

# %%
df.to_csv('cafe_brasil_ep_list.csv',sep=';',index=False)