import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd

numOfPages = 0

def getNumOfLinks():
    global numOfPages
    url = "files/message_1.html"
    page = open(url)
    soup = BeautifulSoup(page.read(), "html5lib")
    pages = []
    links = soup.find_all("a")

    pages = []
    for link in links:
        if re.search("^[0-9]*$", str(link.contents[0])):
            pages.append(str(link.contents[0]))

    pages = list(dict.fromkeys(pages))
    numOfPages = int(pages[len(pages)-1])

getNumOfLinks()

print(numOfPages)