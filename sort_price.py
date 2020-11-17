import csv

# 將價格做排序
def sortPrice(page):
    '''開啟csv檔案，讀成list'''
    with open ('output{}.csv'.format(page), 'r', newline='', encoding='utf-8-sig') as csvFile:
        rows = csv.reader(csvFile)
        lists = []
        for row in rows:
            lists.append(row)
    
    '''按照價格做排序(由小到大)'''
    items = lists[1:]
    goods = {}
    for i in range(len(items)):
        url = items[i][3]
        name = url.split('-i')[0].split('https://shopee.tw//')[1]
        img = items[i][4]
        price1 = items[i][1]
        price2 = items[i][2]
        
        # 要對千元以上的數字進行處理 (網頁表示為'1,013')
        if ',' in price1:
            price = []
            price.append(price1.split(',')[0])
            price.append(price1.split(',')[1])
            price1 = int(''.join(price))
        else:
            price1 = int(price1)
        if ',' in price2:
            price = []
            price.append(price2.split(',')[0])
            price.append(price2.split(',')[1])
            price2 = int(''.join(price))
        else:
            price2 = int(price2)
        
        if name in goods:
            goods[name+' '] = [price1, price2, url, img]
        else:
            goods[name] = [price1, price2, url, img]
    sortGoods = sorted(goods.items(), key=lambda x:x[1][0])
    
    '''寫入csv檔案'''
    with open('sorted{}.csv'.format(page), 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['商品', '價格1', '價格2', '網址', '圖片']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(items)):
            writer.writerow({'商品': sortGoods[i][0], '價格1': sortGoods[i][1][0], '價格2': sortGoods[i][1][1], '網址': sortGoods[i][1][2], '圖片': sortGoods[i][1][3]})


for i in range(5):
    sortPrice(i)