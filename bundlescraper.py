#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

URL = 'https://www.humblebundle.com/books/open-source-bookshelf?hmb_source=navbar&hmb_medium=product_tile&hmb_campaign=tile_index_6'
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')

#datastructure
tier_dict = {}

tiers= soup.find_all("div", class_ ="main-content-row dd-game-row js-nav-row")

for tier in tiers:
    #only for the headline
    if tier.select(".dd-header-headline"):
        #grab the tier name
        tiername = tier.select(".dd-header-headline")[0].text.strip()
        #grab tier product names
        product_names = tier.select(".front-page-art-image-text")
        product_names = [prodname.text.strip() for prodname in product_names]
        tier_dict[tiername] = {"products":product_names}


for tiername, tierinfo in tier_dict.items():
    print(tiername)
    print("Products: ")
    print(" , ".join(tierinfo['products']))
    print("\n\n")


#Bundle Tiers
# tier_headlines = soup.find_all("h2", class_ = "dd-header-headline")
# stripped_headlines= [tier.text.strip() for tier in tier_headlines]
# print(stripped_headlines)
#Product names
# product_name = soup.find_all('span', class_ ="front-page-art-image-text")
# stripped_prduct_name= [tier.text.strip() for tier in product_name ]

#Price for each tiers
# price_names = [name.split[1] for name in stripped_headlines if name.startswith("Pay")]
# print(price_names)

#tier 1 name and price
#    -product
#    -product
#tier 2 name and price
#    -product
#    -product
##this is the data structure we'll use to store bundle info
# tiers = {
#     "tier 1":{
#                 "price": 500,
#                 "product":[
#                             'name 1',
#                             'name 2'
#                           ]
#              },
#     'tier 2':{
#                 'price': 250,
#                 'product':[
#                             'name 1',
#                             'name 2'
#                           ]
#              }
# }
