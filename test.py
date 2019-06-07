import urllib.request, urllib.error

# from urllib.request import urlopen

from bs4 import BeautifulSoup

url = "http://www.nikkei.com/markets/kabu/"

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

span = soup.find_all("span")

nikkei_average = ""

for tag in span:
    try:
        string_ = tag.get("class").pop(0)

        if string_ in "mkc-stock_prices":
            nikkei_average = tag.string
            break


    except:
        pass

print(nikkei_average)
