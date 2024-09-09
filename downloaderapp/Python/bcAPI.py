from tkinter import *
from tkinter.font import BOLD, Font
import requests as req
res = req.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
price = res.json()['data']['amount']
root = Tk()
root.geometry('235x200')
root.title('Bitcoin price')
lbl = Label(root,text=f'BitCoin Price is: {price}',font=("Times",14,"bold"))
lbl.pack(side=LEFT)
root.mainloop()
 
 