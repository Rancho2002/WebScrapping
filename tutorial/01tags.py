import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    html_doc= f.read()

soup=BeautifulSoup(html_doc,"html.parser") #from the documentation https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.find_all("div")[0])


# for links in soup.find_all("a"):
#     # print(dir(links))
#     print(links)
#     print(links.get("href"))
#     print(links.get_text())

# print(soup.select("div.head")) # ! use of css selector as well 
# print(soup.select("span#head")) 
# print(soup.div.get("class")) #first div class

# print(soup.find_all(class_="head")) # find gives only the first one

# for child in soup.find(class_="container").children:
#     print(child)


for parent in soup.find(class_="head").parent:
    print(parent)
