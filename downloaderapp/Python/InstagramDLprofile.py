from tkinter.font import BOLD
import instaloader
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("ProfileInstaDownloader")
def profileDL():
    try:
        ig = instaloader.Instaloader()
        profile = Entry.get(ent)
        ig.download_profile(profile,profile_pic_only=True)
        messagebox.showinfo("Status","Profile image downloaded successfully")
    except:
        messagebox.showinfo("Status","Failed, Please enter username correct")


title = Label(root,text="Instagram Profile Image Downloader",font=("Times",20,"bold"))
title.grid(row=0,column=0,padx=30,pady=10)
lbl = Label(root,text="Enter Username: ",font=("Ariel",15))
lbl.grid(row=3,column=0)
ent = Entry(root,width=50)
ent.grid(row=3,column=1,columnspan=3)
btn = Button(root,text="Download",width=30,command=profileDL)
btn.grid(row=4,column=0,columnspan=5,pady=10)
root.mainloop()
