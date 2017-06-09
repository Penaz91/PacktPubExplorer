#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

useragent = "Mozilla/5.0 (X11; U; Linux i686; en-gb) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) epiphany-webkit"
url = "https://www.packtpub.com/packt/offers/free-learning"

response = requests.get(url, headers={"user-agent": useragent})

soup = BeautifulSoup(response.content, "lxml")

rawtitle = soup.findAll("div", class_="dotd-title")

title = rawtitle[0].text.strip()

title = title.replace("#", "\#")

with open("/home/penaz/.packt", "w") as p:
    p.write(title)
