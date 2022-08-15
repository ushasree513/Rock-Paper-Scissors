import random
from tkinter import *
from PIL import ImageTk,Image

root= Tk()
root.geometry("800x500")
paper = ImageTk.PhotoImage(Image.open('paper.PNG'))
stone = ImageTk.PhotoImage(Image.open('stone.PNG'))
scissors = ImageTk.PhotoImage(Image.open('scissors.PNG'))
label1 = Label(root)

def logic():
    Output = random.randint(1,3)
    if(Output == 1):
        label1.config(image=paper)
        label1.pack()
    elif(Output == 2):
        label1.config(image=stone)
        label1.pack()
    else:
        label1.config(image=scissors)
        label1.pack()
b1 = Button(root,text="Lets Play Rock-Paper-Scissors", font=("Bold",30),bg="Light Blue",command=logic).pack()
root.mainloop()
