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
        self.hintButton = Button(self.master, text='Hint', width=5, height=1, font=('Arial', 10, 'bold'), relief=RAISED, bg='#445b8e', fg='white', command=self.displayHint)
        self.passButton = Button(self.master, text='Pass', width=10, height=1, font=('Arial', 10, 'bold'), relief=RAISED, bg='#b1d300', fg='black', command=self.passImage)
        self.exitButton = Button(self.master, text='Exit', width=10, height=1, font=('Arial', 10, 'bold'), relief=RAISED, bg='#c0292a', fg='white', command=self.exitProg)

        self.keyboardFrame = Frame(self.master)

        #ANSWER ENTRY
        self.var = StringVar()
        self.var.trace('w', self.checkAnswer) 
        self.entry = Entry(root, textvariable=self.var, width=27, justify=CENTER, font=('Gill Sans MT', 13, 'bold'), state='readonly', readonlybackground='#151922')
        self.entry.bind('<Button-1>', lambda e: self.displayKeyboard())

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
        
        self.displayFirstImage()
    
    #FUNCTIONS
    def displayFirstImage(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

        try:
            f = open(os.path.join(__location__, 'picList.txt'), 'r')
            x = f.readlines()

            self.picfiles = list()
            for p in x:
                fn = p.strip().split(';')
                self.picfiles.append(fn[1])

            if os.path.isfile('4PicsSaveFile.txt'):
                try: 
                    with open('4PicsSaveFile.txt', 'r') as f:
                        data = f.read()
                        f.close()
                    data = data.split(',')
                    self.level = int(data[0])
                    self.levelText.config(text=self.level)
                    self.coinAmount = int(data[1])
                    self.coinAmountTxt.config(text=str(self.coinAmount))
                    self.picNum = self.picfiles.index(data[2])
                except:
                    print('Opening 4PicsSaveFile file error.')

            self.pics = PhotoImage(file=os.path.join(__location__+'\\MP2_Pictures\\', self.picfiles[self.picNum]) + '.png')
            lblpic = Label(self.master, image=self.pics)
            lblpic.place(x=72, y=50)

            self.displayKeyboard()
        except:
            print('File not found.')

    def changeImage(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

        if self.level == 50:
            if mb.showinfo('Congratulations!', 'You finished the game!'):
                self.master.destroy()

        self.picNum += 1
        if self.picNum == 50:
            self.picNum = 0

        while self.picfiles[self.picNum] in self.answeredPics:
            self.picNum += 1

        self.pics.config(file=os.path.join(__location__+'\\MP2_Pictures\\', self.picfiles[self.picNum]) + '.png')

        self.entry.configure(state='normal', justify=CENTER, font=('Gill Sans MT', 13, 'bold'), bg='#151922', fg='white')
        self.entry.delete(0, END)
        self.entry.configure(state='readonly', justify=CENTER, font=('Gill Sans MT', 13, 'bold'), readonlybackground='#151922', fg='white')

        self.displayKeyboard()

    def displayKeyboard(self):
        buttons = list(string.ascii_uppercase)
        buttons.append('⟳')

        row = 2
        column = 0

        for button in buttons:
            if button == '⟳':
                Button(self.keyboardFrame, text=button, width=4, bg='#9b9b9b', fg='black', activebackground='lightgrey', 
                   activeforeground='black', font=('Arial', 8), relief='raised', padx=1, pady=1, bd=1, command=lambda x=button: self.selectChar(x)).grid(row=row, column=column)
            else:
                Button(self.keyboardFrame, text=button, width=4, bg='white', fg='black', activebackground='lightgrey', 
                   activeforeground='black', font=('Arial', 8), relief='raised', padx=1, pady=1, bd=1, command=lambda x=button: self.selectChar(x)).grid(row=row, column=column)

            column += 1

            if column > 8 and row == 2:
                column = 0
                row += 1
            if column > 8 and row == 3:
                column = 0
                row += 1
            if column > 8 and row == 4:
                column = 0
                row += 1

    def selectChar(self, value):
        self.entry.configure(state='normal', justify=CENTER, font=('Gill Sans MT', 13, 'bold'), bg='#151922', fg='white')

        if value == '⟳':
            self.entry.delete(0, END)
        else:
            self.entry.insert(END, value)
        
        self.entry.configure(state='readonly', justify=CENTER, font=('Gill Sans MT', 13, 'bold'), readonlybackground='#151922', fg='white')

    def displayHint(self):
        try:
            if self.coinAmount >= 2:
                self.coinAmount -= 2
                self.coinAmountTxt.config(text=str(self.coinAmount))

                word = list(self.picfiles[self.picNum])
                current_word = list(self.entry.get())

                self.entry.configure(state='normal', justify=CENTER, font=('Gill Sans MT', 13, 'bold'), bg='#151922', fg='white')

                if len(current_word) == 0:
                    self.entry.insert(INSERT, word[0].upper())
                elif len(current_word) > 0 and len(current_word) < len(word):
                    self.entry.insert(INSERT, word[len(current_word)].upper())
                
                self.entry.configure(state='readonly', justify=CENTER, font=('Gill Sans MT', 13, 'bold'), readonlybackground='#151922', fg='white')
            else:
                mb.showinfo('No more hints!', 'You do not have enough coins.')
        except:
            mb.showerror('Error!')

    def checkAnswer(self, *args):
        s = self.var.get()
        answer = self.picfiles[self.picNum]

        if len(s) > len(answer):
            mb.showwarning('Oops!', 'Wrong answer. Try again.')
            self.entry.delete(0, END)
        elif s == answer.upper():
            self.entry.configure(state='normal', justify=CENTER, font=('Gill Sans MT', 13, 'bold'), bg='#151922', fg='white')

            mb.showinfo('Great Work!', 'Amazing! You got the correct answer!')
            self.answeredPics.append(self.picfiles[self.picNum])

            self.coinAmount += 10
            self.coinAmountTxt.config(text=self.coinAmount)

            self.levelUp()
            self.changeImage()

    def levelUp(self):
        self.level += 1
        self.levelText.config(text=self.level)

    def passImage(self):
        if self.coinAmount >= 10:
            self.coinAmount -= 10
            self.coinAmountTxt.config(text=str(self.coinAmount))
            self.changeImage()
        else:
            mb.showinfo('Cannot pass anymore!', 'You do not have enough coins.')

    def exitProg(self):
        with open('4PicsSaveFile.txt', 'w') as f:
            data = str(self.level) + ',' + str(self.coinAmount) + ',' + str(self.picfiles[self.picNum]) 
            f.write(data)
            f.close()
            
        if mb.askokcancel('Quit', 'Do you want to exit? Your progress will be saved.'):
            self.master.destroy()

# -----------------------------------------------------------------------

def disable_exit_event():
   mb.showwarning('Quit', 'Please use the exit button in the program.')

def randomize_pictures():
    words = ['yellow', 'addition', 'accounts', 'accident', 'tree', 'wig', 'attach', 'van', 'unit', 'werewolf', 
             'wet', 'yak', 'withdraw', 'zen', 'caress', 'trip', 'zeppelin', 'write', 'wreck', 'wellness', 'airplane', 
             'achiever', 'wizard', 'turn', 'wrench', 'war', 'zombie', 'tune', 'alliance', 'athens', 'snap', 'tuna', 'twig', 
             'tube', 'wok', 'zip', 'wax', 'activity', 'yacht', 'woolly', 'wrong', 'wisdom', 'writer', 'workshop', 'way', 'type', 
             'achieve', 'zebra', 'young', 'bikini']
    shuffled_words = random.sample(words, len(words))
    for x in range(1, len(shuffled_words)+1):
        shuffled_words[x-1] = str(x) + ';' + shuffled_words[x-1]
    text = '\n'.join(shuffled_words)

    with open('picList.txt', 'w') as f:
        f.write(text)
        f.close()

def main():
    #randomize_pictures()

    global root
    root = Tk()
    root.geometry('450x550')
    root.resizable(False, False)
    root.protocol('WM_DELETE_WINDOW', disable_exit_event)
    app = Window(root)
    root.mainloop()

main()