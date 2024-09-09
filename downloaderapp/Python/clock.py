from time import strftime
from tkinter import *

root = Tk()
root.title('Clock')

def time():
    str = strftime('%H : %M : %S')
    lbl.config(text=str)
    lbl.after(1000,time)
lbl = Label(root,font=('ds-digital',150),background='black',foreground='green')
lbl.pack(anchor='center')
time()

root.mainloop()
