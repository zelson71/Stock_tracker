# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 04:06:54 2020

@author: zelso
"""
import bs4
import requests
import json
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime
import re

def parsePrice(stock):
        url = 'https://finance.yahoo.com/quote/'
        full = url + stock
        
        r=requests.get(full)
        
        soup = bs(r.text,"lxml")
        price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        return price


# while True:
#         print('The current price for Facebook is '+ str(parsePrice('FB')))
#         print('The current price for Kodak is '+ str(parsePrice('KODK')))
#         print('The current price for Tesla is '+ str(parsePrice('TSLA')))
#         print('The current price for Palantir is '+ str(parsePrice('PLTR')))

def ticker():
        company_name = []
        company_ticker = []

        # remove = re.compile('Fw\(b\)').text
         
        
        # print(remove)
        url = 'https://finance.yahoo.com/trending-tickers'
        r=requests.get(url)

        soup = bs(r.text,'lxml')
        ticks = soup.find_all('Fw(b)')
        outfile = open ('tickers/tickers.txt', 'w')
        for row in ticks:
                outfile.write(row.text + '\n\n')
        
        return ticks

     

print (ticker())