#!/usr/bin/env python3
import requests
from datetime import date
from datetime import timedelta
import json

useragent = "Mozilla/5.0 (X11; U; Linux i686; en-gb) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) epiphany-webkit"
today = date.today().strftime("%Y-%m-%d") + "T00:00:00.000Z"
tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d") + "T00:00:00.000Z"
firsturl = "https://services.packtpub.com/free-learning-v1/offers?dateFrom={}&dateTo={}".format(today, tomorrow)

response = requests.get(firsturl, headers={"user-agent": useragent})
resp1 = json.loads(response.content)
bookid = resp1["data"][0]["productId"]

finalurl = "https://static.packt-cdn.com/products/{}/summary".format(bookid)
response = requests.get(finalurl, headers={"user-agent": useragent})
resp1 = json.loads(response.content)
rawtitle = resp1["title"]

title = rawtitle.strip()

title = title.replace("#", "\#")

if title == "":
    title = "No title found - Check Packt's Free Learning Page"

with open("/home/penaz/.packt", "w") as p:
    p.write(title)
