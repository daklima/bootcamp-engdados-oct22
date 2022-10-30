import pandas as pd
# import requests
import sys
import collections

# import urllib.request
import json

# url = 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbz8vTxNDRy9_Y2NQ13CDA0sTIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wBmoxN_FydLAGAgNTKEK8DkRrACPGwpyQyMMMj0VAcySpRM!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K85260Q5OIRSC42046/res/id=historicoHTML/c=cacheLevelPage/=/'
# url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofácil'
# url = sys.argv[1]
file = sys.argv[1] #'resultados.json'
# r = requests.get(url)

# r.text
# r.text = r.text

r = open(file, encoding="utf8")
data = json.load(r)
# data = json.load(urllib.request.urlopen(url))

r_text = data['html'].replace('\\r\\n', '')
r_text = r_text.replace('"\r\n}','')
r_text = r_text.replace('{\r\n  "html:','')
r_text

df = pd.read_html(r_text)
type(df)
type(df[0])
df1 = df
df = df[0].copy()

df = df[df['Bola1'] == df['Bola1']]

df.head()

nr_pop = list(range(1,26))
nr_par = []
nr_impar = []
nr_primo = []
for n in nr_pop:
    if n % 2 == 0:
        nr_par.append(n)
    elif n % 2 == 1:
        nr_impar.append(n)
    for i in range(2,n):
        if n % i == 0:
            break
        elif n not in nr_primo:
            nr_primo.append(n)

comb = []
v_cont = []
for n in nr_pop:
    v_cont.append([n, 0])
'''v01 = 0
v02 = 0
v03 = 0
v04 = 0
v05 = 0
v06 = 0
v07 = 0
v08 = 0
v09 = 0
v10 = 0
v11 = 0
v12 = 0
v13 = 0
v14 = 0
v15 = 0
v16 = 0
v17 = 0
v18 = 0
v19 = 0
v20 = 0
v21 = 0
v22 = 0
v23 = 0
v24 = 0
v25 = 0'''

cols = ['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15']

for idx, row in df.iterrows():
    v_par = 0
    v_impar = 0
    v_primo = 0
    for c in cols:
        if row[c] in nr_par:
            v_par += 1
        elif row[c] in nr_impar:
            v_impar += 1
        if row[c] in nr_primo:
            v_primo += 1
        for n in nr_pop:
            if row[c] == n:
                v_cont[n-1][1] += 1
        '''if row[c] == 1:
            v01 += 1
        elif row[c] == 2:
            v02 += 1
        elif row[c] == 3:
            v03 += 1
        elif row[c] == 4:
            v04 += 1
        elif row[c] == 5:
            v05 += 1
        elif row[c] == 6:
            v06 += 1
        elif row[c] == 7:
            v07 += 1
        elif row[c] == 8:
            v08 += 1
        elif row[c] == 9:
            v09 += 1
        elif row[c] == 10:
            v10 += 1
        elif row[c] == 11:
            v11 += 1
        elif row[c] == 12:
            v12 += 1
        elif row[c] == 13:
            v13 += 1
        elif row[c] == 14:
            v14 += 1
        elif row[c] == 15:
            v15 += 1
        elif row[c] == 16:
            v16 += 1
        elif row[c] == 17:
            v17 += 1
        elif row[c] == 18:
            v18 += 1
        elif row[c] == 19:
            v19 += 1
        elif row[c] == 20:
            v20 += 1
        elif row[c] == 21:
            v21 += 1
        elif row[c] == 22:
            v22 += 1
        elif row[c] == 23:
            v23 += 1
        elif row[c] == 24:
            v24 += 1
        elif row[c] == 25:
            v25 += 1'''
    comb.append(str(v_par) + 'p-' + str(v_impar) + 'i-' + str(v_primo) + 'np')

freq_nr = v_cont
freq_nr.sort(key=lambda tup: tup[1])

counter_comb = collections.Counter(comb)
resultado = pd.DataFrame(counter_comb.items(), columns=['combination','frequency'])
resultado['p_freq'] = resultado.frequency / resultado.frequency.sum()
resultado.sort_values('p_freq', inplace=True)

print('''
O número mais frequente é: {}
O número menos frequente é: {}
A combinação mais frequente é {}, com a frequência de {}%.
'''.format(freq_nr[-1][0], freq_nr[0][0], resultado['combination'].values[-1], int(resultado['p_freq'].values[-1]*100*100)/100)
)