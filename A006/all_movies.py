#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

#%%
def has_item(xpath, driver):
    try: 
        driver.find_element(By.XPATH, xpath)
        return True
    except:
        return False

#%%
driver = webdriver.Chrome('src\chromedriver.exe')
#   time.sleep(3)
driver.implicitly_wait(10)
driver.get('https://en.wikipedia.org/wiki/Nicolas_Cage_filmography')
xpath_table = '/html/body/div[3]/div[3]/div[5]/div[1]/table[1]'
#%%

tries = 0

while not has_item(xpath_table, driver):
    tries+=1
    if tries > 50:
        break
    pass

#%%
table = driver.find_element(By.XPATH, xpath_table)

# %%
df = pd.read_html('<table>'+table.get_attribute('innerHTML')+'</table>')[0]

with open('print.png','wb') as f:
    f.write(driver.find_element(By.XPATH, '/html/body/div').screenshot_as_png)

driver.close()

# %%
#df[df['Year']=='1984']
# %%
df.to_csv('nic_cage_filmography.csv', sep=';', index=False)
# %%
