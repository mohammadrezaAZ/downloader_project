# Start
import random as rn
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
# Functions
def gen():
	lst1.delete(0,END)
	lst2.delete(0,END)
	team_a = rn.sample(players,10)
	team_b = rn.sample(team_a,5)
	for x in team_b:
		if x in team_a:
			team_a.remove(x)
	for x in team_a:
		lst1.insert(0, x)
	for x in team_b:
		lst2.insert(0, x)
def add_player():
	global counter 
	if len(Entry.get(ent)) == 0:
		messagebox.showwarning('اخطار','لطفا نام را وارد کنید')
	players.append(Entry.get(ent))
	ent.delete(0, 'end')
	counter -= 1
	lblcounter.config(text=f'{counter} نفر مانده')
	if len(players) == 10:
		f1.pack_forget()
		f2.pack()
def help():
	messagebox.showinfo("آموزش","اسم ده تا بازیکن رو وارد کن بعد خودکار میره صفحه تیم کشی")
# User_Interface
root = Tk()
f1 = Frame(root)
f2 = Frame(root)
root.title('Team Generator')
root.geometry('400x200')
# Frame 1
counter = 10 
players = []
f1.pack()
ent = Entry(f1,width=50)
btnp = Button(f1,text='اضافه کن',command=add_player,width=10)
btnh = Button(f1,text='آموزش',command=help,width=10)
lblcounter = Label(f1,text=f'{counter} نفر مانده')
ent.grid(row=0,column=0)
btnp.grid(row=1,column=0)
btnh.grid(row=2,column=0)
lblcounter.grid(row=3,column=0)
# Frame 2
lst1 = Listbox(f2)
lbl = Label(f2,text='VS',font=("Times",20,"bold"))
lst2 = Listbox(f2)
btngen = Button(f2,text='Generate',command=gen)
lst1.grid(row=0,column=0)
lbl.grid(row=0,column=1)
btngen.grid(row=1,column=1)
lst2.grid(row=0,column=2)
root.mainloop()
# End
