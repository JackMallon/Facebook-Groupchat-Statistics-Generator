import re, numpy as np, pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import datetime

#Import chat spreadsheet
chat = pd.read_csv('chat.csv')
#Convert date column to datetime format
chat['Date']= pd.to_datetime(chat['Date']) 
firstYearOfChat = chat.head(1).Date.dt.year

#Global variables
bigString = ""
names = chat.Name.unique()

#Total messages 
def totalMessages():
    global chat
    print("\n")
    print("Total number of messages:")
    print(len(chat.index))

#Get the number of messages per person 
def numberOfMessages():
    global chat
    print("\n")
    print("Total number of messages per individual:")
    print(chat.groupby('Name').size())

#Get the total number of words in the chat
def numberOfWords():
    global chat, bigString
    for index, row in chat.iterrows():
         bigString = bigString + " " + str(row['Message'])
    print("\n")
    print("Number of words:")
    print(str(len(bigString.split())))
    print("294,979")

#Get the most occuring words
def mostOccuringWords():
    global chat, bigString
    split_it = bigString.split() 
    numWords = len(split_it)
    Counter = Counter(split_it) 
    most_occur = Counter.most_common(20)
    print(most_occur) 

#Get largest message
def getBiggestMessage():
    global chat
    indexOfLargestMessage = 0
    largestMessage = ""
    for index, row in chat.iterrows():
         if len(str(row['Message'])) > len(largestMessage):
            largestMessage = row['Message']
            indexOfLargestMessage = index
    print("\n")
    print("Largest Message: " + str(largestMessage))
    print("Index: " + str(indexOfLargestMessage))
    print(str(len(str(largestMessage))))

#Overall group activity
def getGroupActivityPerYear():
    global names,firstYearOfChat
    now = datetime.datetime.now()
    year = int(firstYearOfChat) 
    currentYear = now.year
    numMessages = []
    years = []
    while year < currentYear:
        numMessages.append(len(chat[(chat['Date'].dt.year==year)]))
        years.append(year)
        year += 1
        plt.plot(years, numMessages)
    plt.xlabel('Years')
    plt.ylabel('Number of messages')
    plt.title('Chat activity per year')

    plt.show()

#Group activity per person
def getGroupActivityPerYearPerPerson():
    global names,firstYearOfChat
    now = datetime.datetime.now()
    year = int(firstYearOfChat) 
    currentYear = now.year
    
    for name in names:
        numMessages = []
        years = []
        while year < currentYear:
            numMessages.append(len(chat[(chat['Name']==name) & (chat['Date'].dt.year==year)]))
            years.append(year)
            year += 1
        if(name == 'Amy Larkin' or name == 'Megan Webb'):
            pass
        else:
            plt.plot(years, numMessages, label = name)
        year = int(firstYearOfChat)
    
    plt.xlabel('Years')
    plt.ylabel('Number of messages')
    plt.title('Involvment per person')

    plt.legend()
    plt.show()

#Total messages
totalMessages()

#Total number of words (print statements)
numberOfMessages()

#Total number of words
numberOfWords()

#Get biggest message
getBiggestMessage()

#Get overall group activty per year
getGroupActivityPerYear()

#Get group activity per person per year
getGroupActivityPerYearPerPerson()