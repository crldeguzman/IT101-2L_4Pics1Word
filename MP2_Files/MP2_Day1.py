import os
import random
import string
from tkinter import *
from tkinter import messagebox as mb


class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title('4 Pics, 1 Word')
        
        topFrame = Frame(self.master, width=450, height=32, bg='#151922')
        lblLevel = Label(topFrame, text='Level: ', fg='white', bg='#151922', font='Arial 14 bold')
        lblCoin = Label(topFrame, text='Coins: ', fg='white', bg='#151922', font='Arial 14 bold')
        
        self.level = 1
        self.levelText = Label(topFrame, text=self.level, fg='#add100', bg='#151922', font='Arial 14 bold')

        self.coinAmount = 100
        self.coinAmountTxt = Label(topFrame, text=str(self.coinAmount), fg='#f5e34d', bg='#151922', font='Arial 14 bold')

        self.picNum = 0
        self.answeredPics = []

        #BUTTONS
        self.hintButton = Button(self.master, text='Hint', width=5, height=1, font=('Arial', 10, 'bold'), relief=RAISED, bg='#445b8e', fg='white')
        self.passButton = Button(self.master, text='Pass', width=10, height=1, font=('Arial', 10, 'bold'), relief=RAISED, bg='#b1d300', fg='black')
        self.exitButton = Button(self.master, text='Exit', width=10, height=1, font=('Arial', 10, 'bold'), relief=RAISED, bg='#c0292a', fg='white')

        self.keyboardFrame = Frame(self.master)

        #ANSWER ENTRY
        self.var = StringVar()
        self.entry = Entry(root, textvariable=self.var, width=27, justify=CENTER, font=('Gill Sans MT', 13, 'bold'), state='readonly', readonlybackground='#151922')
        self.entry.bind('<Button-1>')

        #PLACE WIDGETS
        topFrame.place(x=0, y=0)
        lblCoin.place(x=320, y=2)
        lblLevel.place(x=20, y=2)
        self.levelText.place(x=80, y=2)
        self.coinAmountTxt.place(x=385, y=2)

        self.entry.place(x=74, y=355)
        self.hintButton.place(x=324, y=355)
        self.keyboardFrame.place(x=78, y=400)

        self.passButton.place(x=283, y=482)
        self.exitButton.place(x=73, y=482)

        self.place()
        

def main():
    #randomize_pictures()

    global root
    root = Tk()
    root.geometry('450x550')
    root.resizable(False, False)
    app = Window(root)
    root.mainloop()

main()