import random
from tkinter import *
from unittest import result
from PIL import ImageTk,Image

root= Tk()
root.geometry("800x500")
paper = ImageTk.PhotoImage(Image.open('paper.PNG'))
stone = ImageTk.PhotoImage(Image.open('stone.PNG'))
scissors = ImageTk.PhotoImage(Image.open('scissors.PNG'))
label1 = Label(root)
Result = Button(root,font=("Bold",30))




def logic():
    Output = random.randint(1,3)
    sum1 = 0
    if(Output == 1):
        label1.config(image=paper)
        label1.place(x=0,y=150)
        sum1 = sum1 + 1
    elif(Output == 2):
        label1.config(image=stone)
        label1.place(x=0,y=150)
        sum1 = sum1 + 2
    else:
        label1.config(image=scissors)
        label1.place(x=0,y=150)
        sum1 + sum1 + 3
    Result.config(text=sum1)
    Result.place(x=500,y=0)
        
def logic2():
    Output = random.randint(1,3)
    sum2 = 0
    
    if(Output == 1):
        label1.config(image=paper)
        label1.place(x=500,y=150)
        sum2 = sum2 + 1
    elif(Output == 2):
        label1.config(image=stone)
        label1.place(x=500,y=150)
        sum2 = sum2 + 2
    else:
        label1.config(image=scissors)
        label1.place(x=500,y=150)
        sum2 = sum2 + 3
    Result.config(text=sum2)
    Result.place(x=0,y=0)

def logic3():
    Output = random.randint(1,3)
    sum3 = 0
    if(Output == 1):
        label1.config(image=paper)
        label1.place(x=1000,y=150)
        sum3 = sum3 + 1
    elif(Output == 2):
        label1.config(image=stone)
        label1.place(x=1000,y=150)
        sum3 = sum3 + 2
    else:
        label1.config(image=scissors)
        label1.place(x=1000,y=150)
        sum3 = sum3 + 3
    Result.config(text=sum3)
    Result.place(x=0,y=0)
label2 = Button(root,text="Lets Play Rock-Paper-Scissors", font=("Bold",30),bg="Light Blue")
label2.place(height=50)
label2.pack(fill=X)
Player1 = Button(root,text="Player 1",font=("Normal",20),command=logic).place(x=0,y=80)
Player2 = Button(root,text="Player 2",font=("Normal",20),command=logic2).place(x=500,y=80)
player3 = Button(root,text="Player 3",font=("Normal",20),command=logic3).place(x=1000,y=80)
root.mainloop()
