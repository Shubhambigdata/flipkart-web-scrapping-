import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name =[]
Prices =[]
Desc =[]
Reviews =[]
#for i in range(2):
url= "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page="+str(1)
r= requests.get(url)
soup = BeautifulSoup(r.text,"lxml")

box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
names= box.find_all("div", class_="_4rR01T")
for i in names:
    name=i.text
    Product_name.append(name)
#print(len(Product_name))


prices= box.find_all("div", class_="_30jeq3 _1_WHN1")
for i in prices:
    price=i.text
    Prices.append(price)
#print(len(Prices))

desc= box.find_all("ul", class_="_1xgFaf")
for i in desc:
    des=i.text
    Desc.append(des)
#print(len(Desc))

reviews= box.find_all("div", class_="_3LWZlK")
for i in reviews:
    review=i.text
    Reviews.append(review)
#print(len(Reviews))


df= pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Description":Desc,"Reviews":Reviews})
print(df)

df.to_csv("flipkart_mobile_under_50000.csv")
#write the file in same folder


