import re, numpy as np, pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import datetime
import random
import sys

names = ['Jack Mallon','Ryan Brennan','Cianan Collins']

#Import chat spreadsheet
chat = pd.read_csv('chat.csv')
bigString = ""

#Create one big string of all of the messages from one individual
def createBigString(name):
    global chat, bigString
    for index, row in chat.iterrows():
        if row['Name']==name:
            if str(row['Message']) == "nan":
                pass
            else:
                bigString = bigString + ". " + str(row['Message'])

#Builds the markov chain
def build_chain(text, chain = {}):
    words = text.split(' ')
    index = 1
    for word in words[index:]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    
    return chain

#Generate the message
def generate_message(chain, count = 50):
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    
    return message

#Read file
def read_file(filename):
    with open(filename, "r") as file:
        contents = file.read().replace('\n\n',' ')
    return contents

#Write the file
def write_file(filename, message):
    with open(filename, "w") as file:
        file.write(message)


for name in names:
    bigString = ""
    createBigString(name)
    chain = build_chain(bigString)
    message = generate_message(chain)
    write_file(name + ".txt", message)
