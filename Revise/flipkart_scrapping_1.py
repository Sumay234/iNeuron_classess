import pandas as pd
import requests
from bs4 import BeautifulSoup

product_name=[]
prices=[]
description=[]
review=[]

for i in range(2,10):
    url="https://www.flipkart.com/search?q=mobile%20under%2070000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"+str(i)
    r=requests.get(url)

    soup=BeautifulSoup(r.text,"lxml")

    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
    names=box.find_all("div",class_="_4rR01T")
    for i in names:
        name=i.text
        product_name.append(name)

    #print(product_name)

    price=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in price:
        name=i.text
        prices.append(name)
    #print(prices)

    descriptions=box.find_all("div",class_="fMghEO")
    for i in descriptions:
        name=i.text
        description.append(name)
    #print(description)

    reviews=box.find_all("div",class_="_3LWZlK")

    for i in reviews:
        name=i.text
        review.append(name)
    #print(review)
    #print(len(review))

df=pd.DataFrame({"Product Name":product_name,"Prices":prices,"Description":description,"Review":review})

df.to_csv("Flipkart_mobile_2.csv")




    #np=soup.find("a",class_="_1LKTO3").get("href")
    #cmp="https://www.flipkart.com"+np
    #print(cmp)

    #url=cmp
    #r=requests.get(url)
#soup=BeautifulSoup(r.text,"lxml")