from tkinter import *
from tkinter.ttk import *
import csv
from urllib.request import urlopen
import time
import pandas as pd
root = Tk()
root.title("Shopee_Gui")
root.geometry("1200x780")

#entry = Entry(root,width = 100)
#entry.grid(row = 0,column = 0,padx = 5,pady =5)
'''
def readImage(url):
    img_bytes = urlopen(url).read()#讀取url
    data_stream = io.BytesIO(img_bytes)
    pil_image = Image.open(data_stream)
    return pil_image
'''
scrollbar = Scrollbar(root, orient="vertical") 
scrollbar.pack(side="right", fill="y") 
lb = Listbox(root,width = 400,height = 200,yscrollcommand=scrollbar.set)
lb2 = Listbox(root,width = 400,height = 200,yscrollcommand=scrollbar.set)
lb3 = Listbox(root,width = 40,height = 200,yscrollcommand=scrollbar.set)
lb4 = Listbox(root,width = 200,height = 200,yscrollcommand=scrollbar.set)
fn = 'output0.csv'
with open(fn,'r',encoding = 'utf-8-sig') as csvFile:
    csvDictReader = csv.DictReader(csvFile)
    for row in csvDictReader:
        print(row['商品'])
        lb.insert(END,row['商品'])
        lb2.insert(END,row['價格1'])
        lb3.insert(END,row['網址'])
        '''
        pil_image = readImage(row['圖片'])
        pil_image2 = pil_image.resize((186,186),Image.ANTIALIAS)
        imgobj = ImageTk.PhotoImage(pil_image2)
        putimage.append(imgobj) 
        lb4.insert(END,putimage[-1])
        '''
        lb4.insert(END,row['圖片'])
        time.sleep(0.2)
lb.pack(side = LEFT,padx = 5,pady = 5)
lb2.pack(pady = 5)
lb3.pack(pady = 5)
lb4.pack(side=RIGHT,padx = 5, pady = 5)
scrollbar.config(command=lb.yview) 
scrollbar.config(command=lb2.yview)
scrollbar.config(command=lb3.yview) 
scrollbar.config(command=lb4.yview)
root.mainloop()


