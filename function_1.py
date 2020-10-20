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
    
    headers = {'user-agent': 'Googlebot'}
    r = requests.get(url, headers=headers) 
    soup = BeautifulSoup(r.text, 'html.parser')
    
    '''設定抓取內容'''
    contents = soup.find_all("div", class_="_1NoI8_ _16BAGk")
    prices = soup.find_all("div", class_="_1w9jLI _37ge-4 _2ZYSiu")
    all_items = soup.find_all("div", class_="col-xs-2-4 shopee-search-item-result__item")
    links = [i.find('a').get('href') for i in all_items]
    
    '''因為有些是價格範圍，所以要特別取出來'''
    price = []
    for i in range(len(prices)):
        a = []
        for item in prices[i]:
            a.extend(list(item))
        if len(a)>2:
            price.append('{}{} ~ {}{}'.format(a[0],a[1],a[5],a[6]))
        else:
            price.append('{}{}'.format(a[0],a[1]))
            
    
    '''寫入csv檔案'''
    with open('output{}.csv'.format(page), 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['商品', '價格', '網址']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(price)):
          writer.writerow({'商品': list(contents[i])[0], '價格': price[i], '網址': 'https://shopee.tw/'+links[i]})

        
for i in range(5):
    findShopee(i, '日檢', 'N2', '單字')