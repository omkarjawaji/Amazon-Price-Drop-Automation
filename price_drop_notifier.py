import requests
from bs4 import BeautifulSoup
import time
import json

dict = {}  # product name, current price , timestamp,

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

URL = 'https://www.amazon.in/Saregama-Carvaan-Bluetooth-Speaker-Porcelain/dp/B07F3YK7VW?pd_rd_w=d1dAh&pf_rd_p=3d2ae0df-d986-4d1d-8c95-aa25d2ade606&pf_rd_r=KPBZFCN6FR1ZMEA9R1P3&pd_rd_r=dfee7f9e-9301-43d7-91dc-bf21d09d1c71&pd_rd_wg=OABJJ'
page = requests.get(URL, headers=header)

soup = BeautifulSoup(page.content, 'html.parser')

seconds = time.time()
local_time = time.ctime(seconds)

dict["prod_name"] = soup.find(id='productTitle').get_text().strip()
desc_price = soup.find(id='priceblock_ourprice').get_text()

dot_index = desc_price.find(".")

current_price = int(desc_price[2:dot_index].replace(",", ""))
dict["current price"] = str(current_price) + "Rs only *wink wink*"

lowest_price_yet = 10000000

if(current_price < lowest_price_yet):
    lowest_price_yet = current_price
n = 0
while(n == 0):
    n = 1
    #URL = 'https://www.amazon.in/Saregama-Carvaan-Bluetooth-Speaker-Porcelain/dp/B07F3YK7VW?pd_rd_w=d1dAh&pf_rd_p=3d2ae0df-d986-4d1d-8c95-aa25d2ade606&pf_rd_r=KPBZFCN6FR1ZMEA9R1P3&pd_rd_r=dfee7f9e-9301-43d7-91dc-bf21d09d1c71&pd_rd_wg=OABJJ'
    URL = 'https://www.amazon.in/Pikkme-Redmi-9A-9i-Shockproof/dp/B08L16J3WD/ref=lp_21360365031_1_1?dchild=1'
    page = requests.get(URL, headers=header)

    soup = BeautifulSoup(page.content, 'html.parser')

    seconds = time.time()
    local_time = time.ctime(seconds)

    desc_price = soup.find(id = ('priceblock_dealprice' or 'priceblock_ourprice') ).get_text()
    print(desc_price)

    dot_index = desc_price.find(".")

    current_price = str(desc_price[1:dot_index].replace(",", ""))
    dict["previous price"] = dict["current price"]
    dict["current price"] = current_price + "Rs only *wink wink*"

    lowest_price_yet = current_price

    if(current_price == lowest_price_yet):
        lowest_price_yet = current_price


print(json.dumps(dict, sort_keys=False, indent=4))
