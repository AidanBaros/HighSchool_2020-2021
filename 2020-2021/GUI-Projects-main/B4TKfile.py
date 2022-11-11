#----------
import random
from tkinter import *
import tkinter.font
top = Tk()
myList = []
unique_list =[]
Desired_font = tkinter.font.Font( family = "Comic Sans MS", 
                                 size = 10, 
                                 weight = "bold")

#----------
def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()
#----------
def mainProgram():
    clearWindow()
    try:
        L1W3 = Label(top, text="Hello, there! Let's work with lists!", font=Desired_font)
        L1W3.grid(column = 1, row = 0)

        L2W3 = Label(top, text="Choose from the following options.", font=Desired_font)
        L2W3.grid(column = 1, row = 1)

        LS1 = Label(top, text="")
        LS1.grid(column = 1, row = 2)

        B1W3 = Button(text="1.  Add to a list", bg = "Yellow", command = addToList, font=Desired_font)
        B1W3.grid(column = 1, row = 4)

        B2W3 = Button(text="2.  Add a bunch of numbers", bg = "Yellow",  command = addABunch, font=Desired_font)
        B2W3.grid(column = 1, row = 5)

        B3W3 = Button(text="3.  Add a few", bg = "Yellow",  command = addAFew, font=Desired_font)
        B3W3.grid(column = 1, row = 6)

        B4W3 = Button(text="4.  Return the value at an index position", bg = "Yellow",  command = indexValues, font=Desired_font)
        B4W3.grid(column = 1, row = 7)

        B5W3 = Button(text="5.  Sort list", bg = "Yellow",  command = sortList, font=Desired_font)
        B5W3.grid(column = 1, row = 8)

        B6W3 = Button(text="6.  Random Search", bg = "Yellow",  command = randomSearch, font=Desired_font)
        B6W3.grid(column = 1, row = 9)

        B7W3 = Button(text="7.  Linear Search", bg = "Yellow",  command = linearSearch, font=Desired_font)
        B7W3.grid(column = 1, row = 10)

        B8W3 = Button(text="8.  Recursive Binary Search", bg = "Yellow",  command = RBS, font=Desired_font)
        B8W3.grid(column = 1, row = 11)

        B9W3 = Button(text="9.  Iterative Binary Search", bg = "Yellow",  command = IBS, font=Desired_font)
        B9W3.grid(column = 1, row = 12)

        B10W3 = Button(text="10. Print lists", bg = "Yellow",  command = printLists, font=Desired_font)
        B10W3.grid(column = 1, row = 13)

        B11W3 = Button(text="11. Delete a number from a list", bg = "Yellow",  command = deleteListItem, font=Desired_font)
        B11W3.grid(column = 1, row = 14)

        B12W3 = Button(text="12. Clear List", bg = "Yellow",  command = clearList, font=Desired_font)
        B12W3.grid(column = 1, row = 15)

    except:
        print("You made a whoopsie!")        
#----------
def addToList():
    clearWindow()
    def ATL():
        myList.append(int(E1W3.get()))
        E1W3.delete(0, END)
        mainProgram()

    L1W3 = Label(top, text="Adding to a list! Great choice!", font=Desired_font)
    L1W3.grid(column = 1, row = 1)

    L1W3 = Label(top, text="Type an integer here!", font=Desired_font)
    L1W3.grid(column = 1, row = 2)

    E1W3 = Entry(top, bd = 5, font=Desired_font)
    E1W3.grid(column = 1, row = 3)

    B1W3 = Button(text="Add to a list", bg = "Yellow", command = ATL, font=Desired_font)
    B1W3.grid(column = 1, row = 4)
#----------
def addABunch():
    clearWindow()
    def AAB():
        for x in range(0, int(E1W3.get())):
            myList.append(random.randint(0, int(E2W3.get())))
        E1W3.delete(0, END)
        mainProgram()

    L1W3 = Label(top, text="We're gonna add a bunch of integers here!", font=Desired_font)
    L1W3.grid(column = 1, row = 0)

    L2W3 = Label(top, text="How many new integers would you like to add?", font=Desired_font)
    L2W3.grid(column = 0, row = 1)

    L3W3 = Label(top, text="And how high would you like these numbers to go?", font=Desired_font)
    L3W3.grid(column = 2, row = 1)

    E1W3 = Entry(top, bd = 5, font=Desired_font)
    E1W3.grid(column = 0, row = 2)

    E2W3 = Entry(top, bd = 5, font=Desired_font)
    E2W3.grid(column = 2, row = 2)

    B1W3 = Button(text="Add to myList.", bg = "Yellow", command = AAB, font=Desired_font)
    B1W3.grid(column = 1, row = 3)
#----------
def addAFew():
    clearWindow()
    def AAF():
        myList.append(int(E1W3.get()))
        E1W3.delete(0, END)

    L1W3 = Label(top, text="It seem that you want to add a few numbers!", font=Desired_font)
    L1W3.grid(column = 1, row = 0)

    L2W3 = Label(top, text="What numbers would you like to add.", font=Desired_font)
    L2W3.grid(column = 1, row = 1)

    E1W3 = Entry(top, bd = 5, font=Desired_font)
    E1W3.grid(column = 1, row = 2)

    B1W3 = Button(text="Add to myList", bg = "Yellow", command = AAF, font=Desired_font)
    B1W3.grid(column = 1, row = 3)

    B2W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font=Desired_font)
    B2W3.grid(column = 1, row = 4)
#----------
def indexValues():
    clearWindow()
    def IV():
        iv = (myList[int(E1W3.get())])
        e1w3 = E1W3.get()
        clearWindow()

        L3W3 = Label(top, text=f"The number at index position {e1w3} is:", font= Desired_font)
        L3W3.grid(column = 1, row = 0)

        L4W3 = Label(top, text=f"{iv}", font= Desired_font)
        L4W3.grid(column = 1, row = 1)
        
        B2W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
        B2W3.grid(column = 1, row = 2)

    L1W3 = Label(top, text="Ohhh! I heard you need a particular piece of data!", font=Desired_font)
    L1W3.grid(column = 1, row = 0)

    L2W3 = Label(top, text="What index position are you curious about?", font=Desired_font)
    L2W3.grid(column = 1, row = 1)

    E1W3 = Entry(top, bd = 5, font=Desired_font)
    E1W3.grid(column = 1, row = 2)

    B1W3 = Button(text="Find a list item.", bg = "Yellow", command = IV, font=Desired_font)
    B1W3.grid(column = 1, row = 3)
#----------
def sortList():
    clearWindow()
    def SLY():
        clearWindow()
        for x in myList:
            if x not in unique_list:
                unique_list.append(x)
        unique_list.sort()
        L3W3 = Label(top, text=f"{unique_list}", font=Desired_font)
        L3W3.grid(column = 1, row = 0)

        B3W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
        B3W3.grid(column = 1, row = 2)

    def SLN():
        clearWindow()
        for x in myList:
            if x not in unique_list:
                unique_list.append(x)
        unique_list.sort()
        mainProgram()

    L1W3 = Label(top, text="A litte birdie told me you needed some sorted data!", font=Desired_font)
    L1W3.grid(column = 1, row = 0)

    L2W3 = Label(top, text="Wanna see your new list?", font=Desired_font)
    L2W3.grid(column = 1, row = 1)

    B1W3 = Button(text="Yes", bg = "Yellow", command = SLY, font=Desired_font)
    B1W3.grid(column = 0, row = 4)

    B2W3 = Button(text="No", bg = "Yellow", command = SLN, font=Desired_font)
    B2W3.grid(column = 2, row = 4)
#-----------
def sortListNoDis(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
#----------
def randomSearch():
    clearWindow()
    rs = (myList[random.randint(0, len(myList)-1)])
    def cw():
        clearWindow()

        L2W3 = Label(top, text=f"{rs}", font=Desired_font)
        L2W3.grid(column = 1, row = 0)

        B2W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
        B2W3.grid(column = 1, row = 2)

    L1W3 = Label(top, text="RaNdOm SeArCh?!?", font=Desired_font)
    L1W3.grid(column = 1, row = 0)

    B1W3 = Button(text="Press to randomly search our list.", bg = "Yellow", command = cw, font=Desired_font)
    B1W3.grid(column = 1, row = 4)
#----------
def linearSearch():
    clearWindow()
    def ls():
        lsg = E1W3.get()
        clearWindow()
        for x in range (len(myList)):
            if myList[x] == int(lsg):
                L2W3 = Label(top, text=f"Your item is at index position {x}", font=Desired_font)
                L2W3.grid(column = 1, row = 1)

            else:
                L3W3 = Label(top, text="Your item could not be found.", font=Desired_font)
                L3W3.grid(column = 1, row = 1)

        B2W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
        B2W3.grid(column = 1, row = 2)

    L1W3 = Label(top, text="We're gonna check out each ietm ona at a time in your list! This sucks.", font=Desired_font)
    L1W3.grid(column = 1, row = 0)

    L2W3 = Label(top, text="What you lookin for, pardner?", font=Desired_font)
    L2W3.grid(column = 1, row = 1)

    E1W3 = Entry(top, bd = 5, font=Desired_font)
    E1W3.grid(column = 1, row = 2)

    B1W3 = Button(text="Search", bg = "Yellow", command = ls, font=Desired_font)
    B1W3.grid(column = 1, row = 4)
#----------
def RBS():
    clearWindow()
    def rbs():
        rbsg = E1W3.get()
        clearWindow()
        sortListNoDis(myList)
        recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(rbsg))

    L1W3 = Label(top, text="What number are you looking for?", font=Desired_font)
    L1W3.grid(column = 1, row = 0)

    E1W3 = Entry(top, bd = 5, font=Desired_font)
    E1W3.grid(column = 1, row = 2)

    B1W3 = Button(text="Search", bg = "Yellow", command = rbs, font=Desired_font)
    B1W3.grid(column = 1, row = 3)
#----------
def recursiveBinarySearch(unique_list, low, high, x):
    clearWindow()
    if high >= low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            L1W3 = Label(top, text=f"Your number is at index position {mid}", font=Desired_font)
            L1W3.grid(column = 1, row = 0)

            B2W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
            B2W3.grid(column = 1, row = 2)
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        L2W3 = Label(top, text="Your number isn't here! Have you sorted your list?", font=Desired_font)
        L2W3.grid(column = 1, row = 0)

        B3W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
        B3W3.grid(column = 1, row = 2)
#----------
def IBS():
    clearWindow()
    def ibs():
        ibsg = E1W3.get()
        clearWindow()
        sortListNoDis(myList)
        result = iterativeBinarySearch(unique_list, int(ibsg))
        if result != -1:
            L2W3 = Label(top, text=f"Your number is at index position {result}", font=Desired_font)
            L2W3.grid(column = 1, row = 0)

            B1W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
            B1W3.grid(column = 1, row = 2)
        else:
            L2W3 = Label(top, text="Your number is not found in that list, bud! Have you sorted your list?", font=Desired_font)
            L2W3.grid(column = 1, row = 0)

            B2W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
            B2W3.grid(column = 1, row = 2)

    L1W3 = Label(top, text="What number are you looking for?", font=Desired_font)
    L1W3.grid(column = 1, row = 0)

    E1W3 = Entry(top, bd = 5, font=Desired_font)
    E1W3.grid(column = 1, row = 2)

    B1W3 = Button(text="Search", bg = "Yellow", command = ibs, font=Desired_font)
    B1W3.grid(column = 1, row = 4)
#----------
def iterativeBinarySearch(unique_list, x):
    clearWindow()
    low = 0
    high = len(unique_list)-1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
#----------
def printLists():
    clearWindow()
    if len(unique_list) == 0:
        L1W3 = Label(top, text=f"{myList}", font=Desired_font)
        L1W3.grid(column = 1, row = 0)
    else:
        L2W3 = Label(top, text="Which list? Sorted or unsrted?", font=Desired_font)
        L2W3.grid(column = 1, row = 0)

        E1W3 = Entry(top, bd = 5, font=Desired_font)
        E1W3.grid(column = 1, row = 3)

        e1w3 = E1W3.get()
        if e1w3.lower() == "sorted":
            L2W3 = Label(top, text=f"{e1w3}", font=Desired_font)
            L2W3.grid(column = 1, row = 0)
        else:
            L3W3 = Label(top, text=f"{myList}", font=Desired_font)
            L3W3.grid(column = 1, row = 0)

    B2W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
    B2W3.grid(column = 1, row = 2)
#----------
def delFromMyList(myList):
    clearWindow()
    def dfml():
        dfmlg = E1W3.get()
        clearWindow()
        for x in range(0, len(myList)-1):
            if myList[x] == int(dfmlg):
                myList.pop(x)
        L1W3 = Label(top, text=f"{dfmlg} has been deleted from myList", font=Desired_font)
        L1W3.grid(column = 1, row = 0)

        B2W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
        B2W3.grid(column = 1, row = 2)

    L1W3 = Label(top, text="What number do you want to delete?", font=Desired_font)
    L1W3.grid(column = 1, row = 0)

    E1W3 = Entry(top, bd = 5, font=Desired_font)
    E1W3.grid(column = 1, row = 3)

    B1W3 = Button(text="Delete item", bg = "Yellow", command = dfml, font=Desired_font)
    B1W3.grid(column = 1, row = 4)
#----------
def deleteListItem():
    clearWindow()
    def dli(unique_list):
        clearList()
        def dlig():
            dlig1 = E1W3.get()
            clearList()
            for x in range(len(unique_list)):
                if unique_list[x] == int(dlig1):
                    unique_list.pop(x)
            L4W3 = Label(top, text=f"{dlig1} has been deleted from unique_list.", font=Desired_font)
            L4W3.grid(column = 1, row = 0)

            B2W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
            B2W3.grid(column = 1, row = 2)

        L3W3 = Label(top, text="What number do you want to delete?", font=Desired_font)
        L3W3.grid(column = 1, row = 0)

        E1W3 = Entry(top, bd = 5, font=Desired_font)
        E1W3.grid(column = 1, row = 3)

        B1W3 = Button(text="Delete", bg = "Yellow", command = dlig, font=Desired_font)
        B1W3.grid(column = 1, row = 4)

    if len(unique_list) == 0:
        delFromMyList(myList)
    else:
        L1W3 = Label(top, text="I hear you want to delete an item from a list aye.", font=Desired_font)
        L1W3.grid(column = 1, row = 0)

        L2W3 = Label(top, text="Which list would you like to delete a number from?", font=Desired_font)
        L2W3.grid(column = 1, row = 1)

        B1W3 = Button(text="myList", bg = "Yellow", command = delFromMyList, font=Desired_font)
        B1W3.grid(column = 1, row = 4)

        B2W3 = Button(text="unique_list", bg = "Yellow", command = dli, font=Desired_font)
        B2W3.grid(column = 1, row = 5)
#----------
def clearList():
    clearWindow()
    def cw():
        clearWindow()
        list.clear(myList)
        L1W3 = Label(top, text="myList has been cleared.", font=Desired_font)
        L1W3.grid(column = 1, row = 0)

        B2W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
        B2W3.grid(column = 1, row = 2)

    def cwu():
        clearWindow()
        def cwu1():
            clearWindow()
            list.clear(unique_list)
            L1W3 = Label(top, text="unique_list has been cleared.", font=Desired_font)
            L1W3.grid(column = 1, row = 0)

            B2W3 = Button(text="Main Menu", bg = "Light Blue", command = mainProgram, font= Desired_font)
            B2W3.grid(column = 1, row = 1)

        L1W3 = Label(top, text="Are you sure you want to clear myList?", font=Desired_font)
        L1W3.grid(column = 1, row = 0)

        B1W3 = Button(text="Yes", bg = "Yellow", command = cwu1, font=Desired_font)
        B1W3.grid(column = 2, row = 1)

        B2W3 = Button(text="No", bg = "Yellow", command = mainProgram, font=Desired_font)
        B2W3.grid(column = 0, row = 1)

    def cwynml():
        L1W3 = Label(top, text="It seems that you want to clear myList.", font=Desired_font)
        L1W3.grid(column = 1, row = 0)

        L1W3 = Label(top, text="Are you sure you want to clear myList?", font=Desired_font)
        L1W3.grid(column = 1, row = 1)

        B1W3 = Button(text="No", bg = "Yellow", command = mainProgram, font=Desired_font)
        B1W3.grid(column = 2, row = 2)

        B1W3 = Button(text="Yes", bg = "Yellow", command = cw, font=Desired_font)
        B1W3.grid(column = 0, row = 2)
    if len(unique_list) == 0:
        cwynml()

    else:
        L1W3 = Label(top, text="It seems that you wnt to clear a list.", font=Desired_font)
        L1W3.grid(column = 1, row = 0)

        B1W3 = Button(text="myList", bg = "Yellow", command = cwynml, font=Desired_font)
        B1W3.grid(column = 0, row = 1)

        B1W3 = Button(text="unique_list", bg = "Yellow", command = cwu, font=Desired_font)
        B1W3.grid(column = 2, row = 1)
#----------
