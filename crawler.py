import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd

numOfPages = 0
url = "files/message_1.html"
page = open(url)
soup = BeautifulSoup(page.read(), "html5lib")
messages = []
names = []
dates = []

def getNumOfPages():
    global numOfPages,url,page,soup 
    pages = []
    links = soup.find_all("a")
    pages = []

    for link in links:
        if re.search("^[0-9]*$", str(link.contents[0])):
            pages.append(str(link.contents[0]))

    pages = list(dict.fromkeys(pages))

    if len(pages) == 0: 
        numOfPages = 1
    else: 
        numOfPages = int(pages[len(pages)-1])
    print(numOfPages)

def getMembers():
    global numOfPages,url,page,soup 
    memberDiv = soup.find("div", {"class": "_2lek"})
    memberString = memberDiv.contents[0]
    memberString = memberString[14:]
    memberString = memberString.replace(" and ", ", ")
    memberString = memberString.split(", ")
    print(memberString)

def getAllDataFromDivs(i):
    global messages,names,dates
    messageBoxes = soup.find_all("div", {"class": "_3-95"})
    messageBoxes = messageBoxes[2:]
    for box in reversed(messageBoxes):
        name = box.find("div", {"class": "_2pio"}).get_text()
        names.append(name)
        message = box.find("div", {"class": "_2let"}).get_text()
        messages.append(message)
        date = box.find("div", {"class": "_2lem"}).get_text()
        dates.append(date)

getNumOfPages()

for i in range(numOfPages, -1, -1):
    if i != 0:
        url = "files/message_" + str(i) + ".html"
        page = open(url)
        soup = BeautifulSoup(page.read(), "html5lib")
        getAllDataFromDivs(i)

with open('chat.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Message","Date"])
    for x in range(len(messages)):
        writer.writerow([names[x],messages[x],dates[x]])

#Convert the date column to date time data type
chat = pd.read_csv('chat.csv')
chat['Date'] = pd.to_datetime(chat.Date)

chat.to_csv(r'chat.csv', index = False)

