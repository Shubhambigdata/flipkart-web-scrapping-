import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name=[]
Price=[]
Desc=[]
Reviews= []

url = "https://www.flipkart.com/search?q=mobiles+under+15000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+15000%7CMobiles&requestId=103d4252-c13d-4911-83bd-d84e097159ec&as-searchtext=mobiles+under&page="+ str(1)
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")

box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

names= box.find_all("div", class_="_4rR01T")
for i in names:
    name = i.text
    Product_name.append(name)
#print(Product_name)

price = box.find_all("div", class_="_30jeq3 _1_WHN1")
for i in price:
    name = i.text
    Price.append(name)
#print(Price)

desc = box.find_all("ul", class_="_1xgFaf")
for i in desc:
    name = i.text
    Desc.append(name)
#print(Desc)

reviews = box.find_all("div", class_="_3LWZlK")
for i in reviews:
    name = i.text
    Reviews.append(name)
#print(Reviews)



df = pd.DataFrame({"Product_name":Product_name,"Price":Price,"Desc":Desc,"Reviews":Reviews})

df.to_csv("C:/Users/HP/OneDrive/Desktop/shubham/python/flipkart/flipkart_mobiles_firstpage.csv")

#this select Olny single page data checck it for multiple pages using for loop
