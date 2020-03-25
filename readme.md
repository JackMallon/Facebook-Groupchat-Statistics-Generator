# Facebook Groupchat Statistics Generator

The three programs in this project scrape the chat data from downloaded facebook chat files, converts it to a csv and then performs analysis on the file. Markov.py generates a sentence by each individual in the chat based on all of the messages they have sent.     

## Getting Started

You must download your chat data in order to use these programs. You can download your data at the following address:

https://www.facebook.com/your_information/

Download in html format. It may take a few hours and it's faster if you just download the message data. 

Once you've downloaded the files open the folder of the chat you wish to analyse and locate the html files. They should be named in the following format.  

```
message_1.html
message_2.html
```

Run crawler.py before running either of the other two programs. This will generate a csv file containing the data from your chat.  

### Prerequisites

Must have python3 and pip installed and all of the dependencies

```
pip install requests bs4 csv re pandas collections matplotlib datetime random sys
```
