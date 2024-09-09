import random as rn
from tkinter import *

root = Tk()
root.title('Dice Generator')
root.geometry('600x600')

def Generator():
    canvas.create_image(250,250,image=photo)

canvas = Canvas(root, width=600, height=500)
canvas.pack(side='top')
btn = Button(text="Generate",command=Generator,height=100,width=600,bg='green',fg='white')
btn.pack(side='bottom')
dice = rn.randint(1,6)
for i in range(1,7):
    if dice == i:
        photo = PhotoImage(file=f'dice/{i}.png')
root.mainloop()
