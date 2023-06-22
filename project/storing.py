import requests,bs4
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r= requests.get("https://www.techncyber.com/2022/04/best-indian-youtube-channels-for-c.html",headers=headers)

with open("data/data2.html", "w") as f:
    f.write(r.text)

