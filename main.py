#!/usr/bin/env python3
import re
import requests
import argparse
from datetime import date
from datetime import timedelta
from subprocess import Popen
import json
from pathlib import Path
from os.path import join as pathjoin

USERAGENT = "Mozilla/5.0 (X11; U; Linux i686; en-gb) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) epiphany-webkit"
REGEX = re.compile(r"""<h3 class="product-info__title">(?P<content>.*)</h3>""")


def api_based():
    """
    Uses the legacy API-based approach to get the ebook title
    """
    today = date.today().strftime("%Y-%m-%d") + "T00:00:00.000Z"
    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d") + "T00:00:00.000Z"
    firsturl = "https://services.packtpub.com/free-learning-v1/offers?dateFrom={}&dateTo={}".format(today, tomorrow)

    response = requests.get(firsturl, headers={"user-agent": USERAGENT})
    resp1 = json.loads(response.content)
    bookid = resp1["data"][0]["productId"]

    finalurl = "https://static.packt-cdn.com/products/{}/summary".format(bookid)
    response = requests.get(finalurl, headers={"user-agent": USERAGENT})
    resp1 = json.loads(response.content)
    rawtitle = resp1["title"]

    title = rawtitle.strip()

    if title == "":
        title = "No title found - Check Packt's Free Learning Page"

    return title


def scraper():
    """
    Uses a regex-based web scraper to get the ebook title
    """
    url = "https://www.packtpub.com/free-learning"
    response = requests.get(url, headers={"user-agent": USERAGENT})

    content = response.text

    title = REGEX.search(content).groupdict().get(
        "content", "Could not scrape title, check the PacktPub Website"
    )

    return title


def write_file(title):
    """
    Writes a file in home to be used with Conky
    """
    with open(pathjoin(Path.home(), ".packt"), "w") as p:
        p.write(title)


def notify(title):
    """
    Sends the title as a notification with Notify-Send
    """
    Popen(["notify-send", "Today @ Packt", title])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--api", help="Use api-based approach (legacy)", action="store_true"
    )
    parser.add_argument(
        "--notify", help="Use notify-send instead of .packt file",
        action="store_true"
    )
    parser.add_argument(
        "--conky", help="Escape characters to avoid issues with Conky",
        action="store_true"
    )
    args = parser.parse_args()
    if args.api:
        title = api_based()
    else:
        title = scraper()
    if args.conky:
        title = title.replace("#", "\#")
    if args.notify:
        notify(title)
    else:
        write_file(title)
