# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:06:23 2020

@author: user
"""

import csv


for page in range(1):   
    with open('output{}.csv'.format(page), 'r', newline='', encoding='utf-8-sig') as csvfile:
        filereader = csv.reader(csvfile)
        
        mydict={}
        for row in filereader:
            key = row[0]
            mydict[key]=row[1:]
        
        for key in mydict:
            print('Key in mydict='+str(key))
        for key in mydict.keys():
            print('Key in d.keys='+str(key))   #.keys()可以列出字典所有的鍵
        for value in mydict.values():
            print('Key in d.values='+str(value))
        for k,v in mydict.items():
            print(k,v)
        
        #拿掉價格的欄位
        dictlst1 = mydict.pop('商品')
        
        #把價格變成int
        for key in mydict:
            for value in key[0]:
                mydict[key][0] = int(mydict[key][0])
                print(mydict)
         
        #價格排序
        dictlst = sorted(mydict.items(),key = lambda x: (x[1][0]),reverse=False)
        print(dictlst)
        
        #寫入新的csv檔
        for page1 in range(1):    
            with open('output1{}.csv'.format(page1),'a+',newline='',encoding='utf-8-sig') as csvfile_1:
                writer  = csv.writer(csvfile_1)
                for row2 in dictlst:
                    writer.writerow(row2)
            
    
