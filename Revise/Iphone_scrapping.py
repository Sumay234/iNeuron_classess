import pandas as pd
import requests
from bs4 import BeautifulSoup

phone_name=[]
price=[]
review=[]
description=[]


url="https://www.flipkart.com/search?q=iphone+13&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_2_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_2_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=iphone+13%7CMobiles&requestId=3ef4f3f7-667a-467a-8e63-29a64e3ea399&as-backfill=on"
r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")
box=soup.find("div",class_="_1YokD2 _3Mn1Gg")

phonename=box.find_all("div",class_="_4rR01T")
for i in phonename:
    name=i.text
    phone_name.append(name)
print(phone_name)

prices=box.find_all("div",class_="_30jeq3 _1_WHN1")
for i in prices:
    name=i.text
    price.append(name)
print(price)

reviews=box.find_all("div",class_="_3LWZlK")
for i in reviews:
    name=i.text
    review.append(name)
print(review)

descriptions=box.find_all("ul",class_="_1xgFaf")
for i in descriptions:
    name=i.text
    description.append(name)
print(description)

dataset=pd.DataFrame({"Phone Name":phone_name,"Price of Phone":price,"Review":review,"Description":description})
dataset.to_csv("Iphone.csv")

