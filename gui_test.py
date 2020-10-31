from tkinter import *
from tkinter.ttk import *
import csv
root = Tk()
root.title("Shopee_Gui")
root.geometry("680x160")

#entry = Entry(root,width = 100)
#entry.grid(row = 0,column = 0,padx = 5,pady =5)


scrollbar = Scrollbar(root, orient="vertical") 
scrollbar.pack(side="right", fill="y") 
lb = Listbox(root,width = 160,height = 80,yscrollcommand=scrollbar.set)
lb2 = Listbox(root,width = 160,height = 80,yscrollcommand=scrollbar.set)
lb3 = Listbox(root,width = 160,height = 80,yscrollcommand=scrollbar.set)
fn = 'output0.csv'
with open(fn,'r',encoding = 'utf-8-sig') as csvFile:
    csvDictReader = csv.DictReader(csvFile)
    for row in csvDictReader:
        print(row['商品'])
        lb.insert(END,row['商品'])
        lb2.insert(END,row['價格'])
        lb3.insert(END,row['網址'])
lb.pack(side = LEFT,padx = 5,pady = 5)
lb2.pack(pady = 5)
lb3.pack(side=RIGHT,padx = 5, pady = 5)
scrollbar.config(command=lb.yview) 
scrollbar.config(command=lb2.yview)
scrollbar.config(command=lb3.yview) 
root.mainloop()


