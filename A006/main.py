#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time

#%%
# cep = '80420-130'
cep = sys.argv[1]

if cep:
    driver = webdriver.Chrome('src\chromedriver.exe')
    #driver.get('https://howedu.com.br')
    #driver.find_element(By.XPATH, '//*[@id="adopt-accept-all-button"]').click()

    # %%
    driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
    elem_cep = driver.find_element(By.NAME, 'endereco')

    # %%
    elem_cep.clear()
    elem_cep.send_keys(cep)

    # %%
    elem_cmb = driver.find_element(By.NAME, 'tipoCEP')

    # %%
    elem_cmb.send_keys('Todos')

    # %%
    elem_btn_buscar = driver.find_element(By.NAME, 'btn_pesquisar')
    elem_btn_buscar.click()
    time.sleep(3)
    # %%
    logradouro = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
    bairro = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
    localidade = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text 
    #cep_2 = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text 

    driver.close() 

    print(f'''
    Endereço:
    {logradouro}, {bairro}
    {localidade}
    {cep}
    ''')
    # %%
