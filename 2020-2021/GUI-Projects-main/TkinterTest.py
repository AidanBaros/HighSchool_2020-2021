from tkinter import *
import tkinter.font
import random
from B4TKfile import *

#top = Tk()
playlist = []
myRolls = []

width= top.winfo_screenwidth() 
height= top.winfo_screenheight()
top.geometry("%dx%d" % (width, height))
top.title("GUI CT PROJECT")

Desired_font = tkinter.font.Font( family = "Comic Sans MS", 
                                 size = 10, 
                                 weight = "bold")

def printList():
    print(playlist)

def exportPlaylist():
    with open("playlist.txt", "w") as f:
        for song in playlist:
            f.write("%s\n" % song)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI's", font=Desired_font)
    LMain.grid(column = 0, row = 1)

    B1Main = Button(text="Week 1", bg = "White", command = week1, font=Desired_font)
    B1Main.grid(column = 0, row = 2)

    B2Main = Button(text="Week 2", bg = "White", command = week2, font=Desired_font)
    B2Main.grid(column = 0, row = 3)

    B3Main = Button(text="Week 3", bg = "White", command = week3, font=Desired_font)
    B3Main.grid(column = 0, row = 4)

def week1():
    clearWindow()

    def addSong():
        playlist.append(E1.get())
        E1.delete(0, END)

    #This is a Label widget
    L1 = Label(top, text="Playlist Generator", font=Desired_font)
    L1.grid(column = 0, row = 1)

    #This is a Text Entry widget
    E1 = Entry(top, bd = 5, font=Desired_font)
    E1.grid(column = 0, row = 2)

    #this is a Button widget
    B1 = Button(text=" + ", bg = "Blue", command = addSong, font=Desired_font)
    B1.grid(column = 1, row = 2)

    B2 = Button(text="Print List", bg = "Orange", command = printList, font=Desired_font)
    B2.grid(column = 0, row = 3)

    B3 = Button(text="Export List", bg = "Orange", command = exportPlaylist, font=Desired_font)
    B3.grid(column = 1, row = 3)

    Bclear = Button(text="Main Menu", bg = "Light Blue", command = mainMenu, font=Desired_font)
    Bclear.grid(column = 1, row = 4)

def week2():
    def rollDice():
        #access the entry data
        rollTimes = E2W2.get()
        dieType = E1W2.get()

        #clear the window
        clearWindow()

        #perform the dice roll calculations
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        #display the result with two labels and a button that goes to main menu
        L1RD = Label(top, text="Here are your rolls!", font=Desired_font)
        L1RD.grid(column = 0, row = 0)

        L2RD = Label(top, text=f"{myRolls}", font=Desired_font)
        L2RD.grid(column = 0, row = 1)

        B1RD = Button(text="Main Menu", bg = "Light Blue", command = mainMenu, font=Desired_font)
        B1RD.grid(column = 0, row = 3)

    clearWindow()

    L1W2 = Label(top, text="Dice Roller App", font=Desired_font)
    L1W2.grid(column = 1, row = 0)

    L2W2 = Label(top, text="# of Rolls", font=Desired_font)
    L2W2.grid(column = 0, row = 2)

    L3W2 = Label(top, text="# of Sides", font=Desired_font)
    L3W2.grid(column = 2, row = 2)

    LS1 = Label(top, text="")
    LS1.grid(column = 0, row = 1)

    LS2 = Label(top, text="")
    LS2.grid(column = 0, row = 4)

    LS3 = Label(top, text="")
    LS3.grid(column = 2, row = 1)

    LS4 = Label(top, text="")
    LS4.grid(column = 2, row = 4)
    
    E1W2 = Entry(top, bd = 5, font=Desired_font)
    E1W2.grid(column = 0, row = 3)

    E2W2 = Entry(top, bd = 5, font=Desired_font)
    E2W2.grid(column = 2, row = 3)

    B1W2 = Button(text="     Roll 'em     ", bg = "Yellow", command = rollDice, font=Desired_font)
    B1W2.grid(column = 1, row = 5)

    B2W2 = Button(text="Main Menu", bg = "Light Blue", command = mainMenu, font=Desired_font)
    B2W2.grid(column = 2, row = 6)

def week3():
    clearWindow()
    mainProgram()

    B1RD = Button(text="Main Menu", bg = "Light Blue", command = mainMenu, font=Desired_font)
    B1RD.grid(column = 1, row = 16)



if __name__ == "__main__":
    mainMenu()
    top.mainloop()