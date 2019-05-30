import csv # to do operations on CSV
import pandas as pd  # file operations
from bs4 import BeautifulSoup as soup  #Scrapping tool
from urllib.request import urlopen as ureq # For requesting data from link
import numpy as np
import re
def scrap(x):
    global soup
    x = chr(x)#to change integer into character
    url = "http://howstat.com/cricket/Statistics/Players/PlayerList.asp?Group={}".format(x)
    pagehtml = ureq(url)
    soup = soup(pagehtml,"html.parser") #parse the html
    table = soup.find("table", { "class" : "TableLined" })
    with open('AZ.csv', 'a',newline='') as csvfile:
        f = csv.writer(csvfile)
        for x in table:
                rows = table.find_all('tr') #find all tr tag(rows)
                for tr in rows:
                    data=[]
                    cols = tr.find_all('td') #find all td tags(columns)
                    for td in cols:
                        data.append(td.text.strip()) 
                    f.writerow(data)
                    print (data[2])
#Handling the Missing Values using Pandas
    df = pd.read_csv("AZ.csv",header = 1)#so that unnecessary row is removed
    print (df['ODIs'])
    print (df['ODIs'].isnull())
    df['ODIs'].fillna(0, inplace=True)
    df['Tests'].fillna(0, inplace=True)
    df['T20s'].fillna(0, inplace=True)
    print (df)
    df.to_csv('AZ2.csv', index=False)

scrap(90)
