import requests
from bs4 import BeautifulSoup
import csv

'''
def download_img(link,i,page):
    #圖片下載 #放置路徑可能需修改
    download_path = './image{}/'.format(page)
    if not os.path.isdir(download_path):
        os.mkdir(download_path)
    img = requests.get(link)# url 轉為圖片
    with open(download_path+'shappee{}.jpg'.format(i),'wb') as f:
        f.write(img.content)#content 寫進 file.jpg 放入資料夾
'''
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
    pictures = soup.find_all("div",class_="_39-Tsj _1tDEiO")
    pictures_link = [i.find('img').get('src') for i in pictures]
    contents = soup.find_all("div", class_="_1NoI8_ _16BAGk")
    prices = soup.find_all("div", class_="_1w9jLI _37ge-4 _2ZYSiu")
    all_items = soup.find_all("div", class_="col-xs-2-4 shopee-search-item-result__item")
    links = [i.find('a').get('href') for i in all_items]
    '''因為有些是價格範圍，所以要特別取出來'''
    price1 = []
    price2 = []
    for i in range(len(prices)):
        a = []
        for item in prices[i]:
            a.extend(list(item))
        if len(a)>2:
            price1.append(a[1])
            price2.append(a[6])
        else:
            price1.append(a[1])
            price2.append(a[1])

    '''寫入csv檔案'''
    with open('output{}.csv'.format(page), 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['商品', '價格1', '價格2', '網址', '圖片']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(price1)):
            #download_img(picture_link[i]) #新增擺放圖片的資料夾
            writer.writerow({'商品': list(contents[i])[0], 
                             '價格1': price1[i], '價格2': price2[i], 
                             '網址': 'https://shopee.tw/'+links[i],
                             '圖片':pictures_link[i]})
    
for i in range(5):
    findShopee(i, '日檢', 'N2', '單字')
