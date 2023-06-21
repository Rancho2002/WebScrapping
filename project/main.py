from bs4 import BeautifulSoup
import pandas as pd 


with open("data/data.html","r") as f:
    html_doc=f.read()

soup=BeautifulSoup(html_doc,"html.parser")

title=soup.title.string
data={"Product":[],"Price":[],"Ratings":[],"No of Reviews":[]}

products=soup.select("div._4rR01T")
i=0
for product in products:
    products[i]=product.string
    data["Product"].append(products[i])
    i+=1
# print(products)

i=0
costs=soup.select("div._30jeq3._1_WHN1")
for cost in costs:
    costs[i]=cost.string
    data["Price"].append(costs[i])
    i+=1



results=soup.select("span._2_R_DZ span span")


for i in range(0,len(results),3):
    # print(results[i].string[:-9])
    data["Ratings"].append(results[i].string[:-9])

for i in range(2,len(results),3):
    # print(results[i].string[:-8])
    data["No of Reviews"].append(results[i].string[:-8])


dataframe=pd.DataFrame.from_dict(data)
dataframe.index=dataframe.index+1
dataframe.to_csv("SamsungUnder5k.csv")
