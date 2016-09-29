#!/usr/bin/env python
# encoding=utf-8
import codecs
import requests
from bs4 import BeautifulSoup




def download_page(url):
    requests.encoding='utf-8'
    con = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    })
    
    #con.apparent_encoding
    return  con
    

def parse_html(html):
    soup = BeautifulSoup(html)
    
    
    return soup


def main():
    url = "http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=200,page=1,sortRule=-1,sortType=,startDate=2016-09-28,endDate=2016-09-28,gpfw=0,js=var%20data_tab_1.html?rt=24585598"
     
    html = download_page(url)
    print(html.apparent_encoding)
    #data = parse_html(html)
    


if __name__ == '__main__':
    main()




























