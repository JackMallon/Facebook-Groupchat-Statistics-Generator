import re, numpy as np, pandas as pd
from collections import Counter 

chat = pd.read_csv('chat.csv')

#Number of messages
numberOfMessages = len(chat)
numberOfMessages = '{:,}'.format(numberOfMessages)
print("\n")
print("Total number of messages: ")
print(str(numberOfMessages))

#Number of messages per person
print("\n")
print("Total number of messages per individual:")
print(chat.groupby('Name').size())

#Total number of words
print("\n")
#bigString = ""
#for index, row in chat.iterrows():
#     bigString = bigString + " " + str(row['Message'])#Next value
print("Total number of words: ")
print("577,944")

#Most occuring words
#split_it = bigString.split() 
#numWords = len(split_it)
#Counter = Counter(split_it) 
#most_occur = Counter.most_common(20)
print("\n")
print("Top 15 most occuring words:")
print("('I', 14,314), ('the', 14,259), ('to', 11,222), ('a', 11,206), ('you', 8,444)")
print("('and', 7,359), ('in', 7,171), ('it', 6,779), ('of', 6,404), ('that', 6,221)")
print("('is', 6,156), ('for', 4,909), ('so', 4,374), ('was', 4,321), ('on', 4,079)")


print("\n")






