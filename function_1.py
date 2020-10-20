import requests
from bs4 import BeautifulSoup
import csv


# 爬取蝦皮網站
def findShopee(page, keyword1, keyword2, keyword3):
    '''設定網址'''
    if page==0:
        url = 'https://shopee.tw/search?keyword={}%20{}%20{}'.format(keyword1,keyword2,keyword3)
    else:
        url = 'https://shopee.tw/search?keyword={}%20{}%20{}&page={}'.format(keyword1,keyword2,keyword3,page)
    
    '''抓取網址內容'''
    headers = {'user-agent': 'Googlebot'}
    r = requests.get(url, headers=headers) 
    soup = BeautifulSoup(r.text, 'html.parser')
    
    '''設定抓取內容'''
    contents = soup.find_all("div", class_="_1NoI8_ _16BAGk")
    prices = soup.find_all("span", class_="_341bF0")
    all_items = soup.find_all("div", class_="col-xs-2-4 shopee-search-item-result__item")
    links = [i.find('a').get('href') for i in all_items]
    
    '''寫入csv檔案'''
    with open('output{}.csv'.format(page), 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['商品', '價格', '網址']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for c, p, l in zip(contents, prices, links):
          writer.writerow({'商品': c.contents[0], '價格': p.contents[0], '網址': 'https://shopee.tw/'+l})
        
for i in range(1):
    findShopee(i, '日檢', 'N2', '單字')