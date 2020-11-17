import io
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from urllib.request import urlopen
import time
import os
import pandas as pd
# 參考網址 https://stackoverrun.com/cn/q/12976424

root = Tk()
root.title("Shopee_Gui")
root.geometry("1260x780")
Style().configure("Treeview",rowheight = 200)

def readImage(url):
    img_bytes = urlopen(url).read()#讀取url
    data_stream = io.BytesIO(img_bytes)
    pil_image = Image.open(data_stream)
    return pil_image
#建立捲動條
scrollbar = Scrollbar(root, orient="vertical") 
scrollbar.pack(side="right", fill="y") 
#建立treeview(此height 代表顯示欄位數量 非欄位寬(rowheight))
tree = Treeview(root,height = 3,columns = ("商品","價格","網址"),
                yscrollcommand=scrollbar.set)
#建立欄位開頭
tree.heading("#0", text = "圖片")
tree.heading("#1", text = "商品")
tree.heading("#2", text = "價格")
tree.heading("#3", text = "網址")
#設定欄位寬度與顯示位置
tree.column("#0",anchor = W,width = 250)
tree.column("#1",anchor = W,width = 450)
tree.column("#2",anchor = CENTER,width = 110)
tree.column("#3",anchor = W,width = 450)

putimage= []
data = pd.read_csv('./sorted0.csv')#pandas 開啟 csv檔案
for i in range(0,data.shape[0]):
     pil_image = readImage(data.iloc[i][4])#跳去副函式 iloc[i][0]為圖片網址
     pil_image2 = pil_image.resize((186,186),Image.ANTIALIAS)#resize 修改大小
     imgobj = ImageTk.PhotoImage(pil_image2) #photoImage轉換
     putimage.append(imgobj) #放進list
     
     if data.iloc[i][1]!=data.iloc[i][2]:
         price = '{}~{}'.format(data.iloc[i][1],data.iloc[i][2])
     else:
         price = data.iloc[i][1]
     tree.insert("",'end',image = putimage[-1],values=(data.iloc[i][0],
                                        price,data.iloc[i][3]))
     #insert treeview
     #注意 如果執行發現error:img???(???為任意數字) does not exist 
     #請重新刪除 image = putimage[-1] 執行一次，並關閉程式後再補回執行
     #每次圖片抓取[-1] : 因image是每次讀取一整個list, 
     #每次list元素會增加，因此固定抓最後一個被放進的圖片
tree.pack(side=TOP,fill=BOTH)
scrollbar.config(command=tree.yview)  
root.mainloop()