#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import requests
import json
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#windows cmd命令行正确输出中文###########################
class UnicodeStreamFilter:  
    def __init__(self, target):  
        self.target = target  
        self.encoding = 'utf-8'  
        self.errors = 'replace'  
        self.encode_to = self.target.encoding  
    def write(self, s):  
        if type(s) == str:  
            s = s.decode("utf-8")  
        s = s.encode(self.encode_to, self.errors).decode(self.encode_to)  
        self.target.write(s)  
          
if sys.stdout.encoding == 'cp936':  
    sys.stdout = UnicodeStreamFilter(sys.stdout)  
#################################################   


    
def download_page(url):
    #requests.encoding='utf-8'
    con = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    })
    con.encoding = 'GB2312'
    #con.apparent_encoding
    return  con.text
    
##分析网页获取上榜公司链接#######################################
def parse_html(html):
    soup = BeautifulSoup(html);
    
    print(soup.prettify())
    
    for sss in soup.find_all('span', attrs={'class': 'wname'}):
        print(sss)
    
    
    #return soup
    
#################################################################

def main():

    start_date = "2016-09-30"
    end_date   = "2016-09-30"

    url = "http://data.eastmoney.com/DataCenter_V3/stock2016/TradeDetail/pagesize=200,page=1,sortRule=-1,sortType=,startDate=2016-09-30,endDate=2016-09-30,gpfw=0,js=var%20data_tab_1.html?rt=24585598"
     
    data = download_page(url)
    start_pos = data.index('=')
    json_data = data[start_pos + 1:]
    dict = json.loads(json_data)
    
    list_data = dict['data']
    #html =  html.encode('utf-8')
    #print (list_data)
    for item in list_data:
        print(item['SName'])
    


if __name__ == '__main__':
    main()




























