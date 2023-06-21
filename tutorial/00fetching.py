'''
Step 1: pip install bs4 requests
Step 2: import requests and create fetchAndSave function
Step 3: there is limit of web scrapping on specific ip, so we use request with proxy 
Step 4: create separate sample.html
Step 5: now #! time for bs4
Step 6: create a soup i.e object of your html file in python
#! in case problem in fetching : search " simulate browser request python" in google
'''
import requests

# http_proxy  = "http://10.10.1.10:3128"
# https_proxy = "https://10.10.1.11:1080"
# ftp_proxy   = "ftp://10.10.1.10:3128"
# proxies = { 
#               "http"  : http_proxy, 
#               "https" : https_proxy, 
#               "ftp"   : ftp_proxy
#             }



def fetchAndSave(url,path):
    # r=requests.get(url, proxies=proxies) #!when need to do bulk scrapping
    r=requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)


url="https://groww.in/options/nifty"

fetchAndSave(url,"./data/index.html")