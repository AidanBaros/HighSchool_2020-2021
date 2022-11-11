'''
Program Goals:
    1. Get input from the user (at multiple points)
    2. We need to convert some of this input to INTs from STRs
    3. We need to provide choices to the user 
        a. Add more values to a list
        b. Return a value at a specific index
'''
#----------
import random
myList = []
unique_list =[]
#----------
def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""    1.  Add to a list
    2.  Add a bunch of numbers
    3.  Add a few
    4.  Return the value at an index position
    5.  Sort list
    6.  Random Search 
    7.  Linear Search
    8.  Recursive Binary Search
    9.  Iterative Binary Search
    10. Print lists
    11. Delete a number from a list
    12. Clear List
    13. Quit
     -- """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                addAFew()
            elif choice == "4":
                indexValues()
            elif choice == "5":
                sortList(myList)
            elif choice == "6":
                randomSearch()
            elif choice == "7":
                linearSearch()
            elif choice == "8":
                binSearch = input("What number are you looking for?" + "\n -- ")
                sortListNoDis(myList)
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "9":
                binSearch = input("What number are you looking for?" + "\n -- ")
                sortListNoDis(myList)
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print(f"Your number is at index position {result}")
                else:
                    print("Your number is not found in that list, bud! Have you sorted your list?")
            elif choice == "10":
                printLists()
            elif choice == "11":
                deleteListItem(myList, unique_list, delFromMyList)
            elif choice == "12":
                clearList(myList, unique_list)
            else:
                break
        except:
            print("You made a whoopsie!")
#----------
    '''
    addToList() Here we give an input and then take that input and make it an integer and add it to myList.
    '''
def addToList():
    print ("Adding to a list! Great choice!")
    newItem = input ("Type an integer here!" + "\n -- ")
    myList.append(int(newItem))
#----------
    '''
    addABunch()
    '''
def addABunch():
    print ("We're gonna add a bunch of integers here!")
    numToAdd = input("How many new integers would you like to add?" + "\n -- ")
    numRange = input("And how high would you like these numbers to go?" + "\n -- ")
    for numToAdd in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is a new complete.")
#----------
    '''

    '''
def addAFew():
    print("It seem that you want to add a few numbers!")
    while True:
        whatNum = input("What numbers would you like to add if you are done type stop." + "\n -- ")
        myList.append(int(whatNum))
        if whatNum == ("stop"):
            return
#----------
    '''

    '''
def indexValues():
    print ("Ohhh! I eard you need a particular piece of data")
    indexPos = input("What index position are you curious about?" + "\n -- ")
    print(myList[int(indexPos)])
#----------
    '''

    '''
def sortList(myList):
    print("A litte birdie told me you needed some sorted data!")
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input('Wanna see your new list?   Y/N' + "\n -- ")
    if showMe.lower() == 'y':
        print(unique_list)
#-----------
    '''

    '''
def sortListNoDis(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
#----------
    '''

    '''
def randomSearch():
    print("RaNdOm SeArCh?!?")
    print(myList[random.randint(0, len(myList)-1)])
#----------
    '''

    '''
def linearSearch():
    print("We're gonna check out each ietm ona at a time in your list! This sucks.")
    searchItem = input("What you lookin for, pardner?" + "\n -- ")
    for x in range (len(myList)):
        if myList[x] == int(searchItem):
            print (f"Your item is at index position {x}")
#----------
    '''

    '''
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            print("Your number is at index position" + f" {mid}")
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here! Have you sorted your list?")
#----------
    '''

    '''
def iterativeBinarySearch (unique_list, x):
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
    '''

    '''
def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or unsrted?" + "\n -- ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)
#----------
    '''

    '''
def delFromMyList(myList):
    itemToDelete = input("What number do you want to delete?" + "\n -- ")
    for x in range(len(myList)):
        if myList[x] == int(itemToDelete):
            myList.pop(x)
    print(f"{itemToDelete} has been deleted from myList")
#----------
    '''

    '''
def deleteListItem(myList, unique_list, delFromMyList):
    if len(unique_list) == 0:
        delFromMyList()
    else:
        print("I hear you want to delete an item from a list aye.")
        listToDeleteFrom = input("Which list would you like to delete a number from? myList or unique_list" + "\n -- ")
        if listToDeleteFrom.lower() == "mylist":
            delFromMyList()
        else:
            itemToDelete = input("What number do you want to delete?" + "\n -- ")
            for x in range(len(unique_list)):
                if unique_list[x] == int(itemToDelete):
                    unique_list.pop(x)
            print(f"{itemToDelete} has been deleted from unique_list.")
#----------
    '''

    '''
def clearList(myList, unique_list):
    if len(unique_list) == 0:
        print("It seems that you want to clear myList.")
        confermation = input("Are you sure you want to clear myList? Y/N" + "\n -- ")
        if confermation.lower() == "y":
            list.clear(myList)
            print("myList has been cleared.")
        else:
            pass
    else:
        print("It seems that you wnt to clear a list.")
        listToClear = input("Which list would you like to clear? myList or unique_list" + "\n -- ")
        if listToClear.lower() == "mylist":
            confermation = input("Are you sure you want to clear myList? Y/N" + "\n -- ")
            if confermation.lower() == "y":
                list.clear(myList)
                print("myList has been cleared.")
            else:
                pass
        elif listToClear.lower() == "unique_list":
            confermation = input("Are you sure you want to clear unique_list? Y/N" + "\n -- ")
            if confermation.lower() == "y":
                list.clear(unique_list)
                print("unique_list has been cleared.")
            else:
                pass
        else:
            print("That is not a valid list")
#----------
    '''

    '''
if __name__ == "__main__":
    mainProgram()
