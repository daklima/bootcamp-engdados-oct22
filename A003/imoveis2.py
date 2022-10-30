#%%
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import json

# %%
def get_json(url,i,headersList,payload):
    resp = requests.get(url.format(0), data=payload, headers=headersList)
    soup = bs(resp.text, 'html.parser')
    json.loads(soup.text)

# %%
#TUDO NUM LOOP SÓ:
url = 'https://glue-api.vivareal.com/v2/listings?addressCity=Curitiba&addressLocationId=BR>Parana>NULL>Curitiba&addressNeighborhood=&addressState=Paraná&addressCountry=Brasil&addressStreet=&addressZone=&addressPointLat=-25.437238&addressPointLon=-49.269973&business=SALE&facets=amenities&unitTypes=APARTMENT&unitSubTypes=UnitSubType_NONE,DUPLEX,LOFT,STUDIO,TRIPLEX&unitTypesV3=APARTMENT&usageTypes=RESIDENTIAL&listingType=USED&parentId=null&categoryPage=RESULT&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount),page,seasonalCampaigns,fullUriFragments,nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,phones),developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount))&size=300&from={}&q=&developmentsSize=5&__vt=&levels=CITY,UNIT_TYPE&ref=&pointRadius=&isPOIQuery='
headersList = {
    "Accept": "*/*",
    "User/Agent": "Thunder Client (https://thunderclient.io)",
    "x-domain": "www.vivareal.com.br"
}
payload=""

first_prop = 0
json_data = get_json(url,first_prop,headersList,payload)

df = pd.DataFrame(columns=['description','address','area','bedroom','bathroom','garage','price','maintenance_fee','prop_link'])
while  len(json_data['search']['result']['listings'])> 0:
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
