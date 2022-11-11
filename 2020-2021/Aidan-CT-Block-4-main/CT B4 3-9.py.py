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
'''
    mainProgram()
    We start with a while True statement so that the whole code runs until stopped.
    Next we have a try and except statement which we uses as a simple error messaging system. 
    Then we give an input that gives a list of all the options for doing things with their list.
    Then we have an if statement, a bunch of elif statements, and an else statement that detects what this input is and runs the corresponding code. 
    The else statement is there so that if any number that is not detected by the if or elif statements make it stop the code.
    '''
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
    addToList() 
    Here we give an input and then take that input and make it an integer and add it to myList.
    '''
def addToList():
    print ("Adding to a list! Great choice!")
    newItem = input ("Type an integer here!" + "\n -- ")
    myList.append(int(newItem))
#----------
'''
    addABunch() 
    Here we give the user two input’s: numToAdd and numRange. 
    We then use numToAdd to determine the number of new items to add to the list. 
    Then we use the random liberty with numRange to add random numbers between 0 and numRage.
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
    addAFew()
    First, we have a while true statement which makes the code inside of it run until told to stop.
    Then we give an input that like addToList adds the input to myList but because of the while loop, it will continue to let you add numbers. 
    Next, we have an if statement that checks to see if the input is stop and if it is it will end the while loop if not it will just continue.

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
    indexValues()
    Here we give an input then convert it into an integer and then find and display that index position in myList.
    '''
def indexValues():
    print ("Ohhh! I eard you need a particular piece of data")
    indexPos = input("What index position are you curious about?" + "\n -- ")
    print(myList[int(indexPos)])
#----------
'''
    sortList()
    First, we have a for loop which looks at each item in myList.
    Then there is an if statement that says if the number that is being looked at is not already in uique_list add it to it.
    It goes through every item in the list then it sorts the list in numerical order.
    Next, we have an input that asks if you want to see the list and if you type Y it will show it to you if it is anything else it will take it as an N.
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
    sortListNoDis()
    This is very similar to sortList in the way that it goes through myList and adds items to unique_list if they are not already in there. 
    The difference is that it does not display anything and it is just used along with other functions, not on its own.
    '''
def sortListNoDis(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
#----------
'''
    randomSearch()
    Here we use the random liberty to get a random value and show that index postion. 
    The way we do that is by taking the length of mylist and subtract 1 then we finding a random number between the length and 0 and print that index position.
    '''
def randomSearch():
    print("RaNdOm SeArCh?!?")
    print(myList[random.randint(0, len(myList)-1)])
#----------
'''
    linearSearch()
    First, we give an input to determine the number that is being looked for. 
    Then we have a for loop which makes it so that it will check every item in the list. 
    Then using x as our variable we go through the list and if x is equal to the imputed number it prints a message that gives you the index position of that number.
    '''
def linearSearch():
    print("We're gonna check out each ietm ona at a time in your list! This sucks.")
    searchItem = input("What you lookin for, pardner?" + "\n -- ")
    for x in range (len(myList)):
        if myList[x] == int(searchItem):
            print (f"Your item is at index position {x}")
#----------
'''
    recursiveBinarySearch()
    This function uses sortListNoDis to make sure that the list is sorted before it runs because if it is not sorted it does not work.
    We start with an if statement that checks to make sure that the highest value is greater than or equal to the lowest value.
    Then it finds the middle value by adding the highest value and the lowest value then dividing them by 2.
    Then it checks to see if the middle value is equal to x which is an input that is initiated in mainProgram. 
    If the middle value is equal to x then it prints a message that tells you that index position.
    If it is not the middle value it checks to see if mid is greater than x if it is then it makes mid - 1 the new high value.
    If not then means that mid is less than x and it makes mid + 1 the new low value and it contim=nues until mid = x.
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
    iterativeBinarySearch()
    This function uses sortListNoDis to make sure that the list is sorted before it runs because if it is not sorted it does not work.
    First, it sets low and mid values to 0 and high value to the length of unique_list - 1.
    Then it has a while loop which makes the code run until stopped and it stops when low is not less than or equal to high.
    Then similarly to recursiveBinarySearch, it goes through and changes the value of mid depending on if mid is less than or greater than x.
    Then once low is not less than or equal to high it returns -1 which triggers code to run in mainProgram. 
    What that does is it prints out the index location of where it stopped which is the index position of x.
    '''
def iterativeBinarySearch(unique_list, x):
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
    printLists()
    Here we start with an if statement that checks to see if there are any items in uniqu_list.
    If there are none it prints myList.
    If there are items in unique_list it will give an input that asks which list you want to print. 
    Then based on the input we will either print myList or unique_list.
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
    delFromMyList()
    This function is not used on its own it is used in other functions to make the code smaller.
    First, it starts by giving an input that asks what number you want to delete.
    Then very similar to linearSearch it goes through every item in the list and determining if it matches the input but in this case, if it matches the input it will be deleted from the list.
    '''
def delFromMyList(myList):
    itemToDelete = input("What number do you want to delete?" + "\n -- ")
    for x in range(len(myList)):
        if myList[x] == int(itemToDelete):
            myList.pop(x)
    print(f"{itemToDelete} has been deleted from myList")
#----------
'''
    deleteListItem()
    We start with an if statement that checks if there are items in unique_list if there are not any it runs delFromMyList.
    If there are items in unique_list it gives an input that lest you chose which list to delete from.
    If you chose myList it runs delFromMyList if you choose unique_list it runs basically the same code as delFromMyList except that it affects unique_list.
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
    clearList()
    This function has a very similar format to deleteListItem.
    The differences between them are that this one does not use any other functions to work. 
    Also, it gives inputs to double-check that the user wants to clear the list and that instead of deleting an item it clears the list.
    Also because it is clearing the list it does not have to go through each item in the list checking if it is the needed one.

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
if __name__ == "__main__":
    mainProgram()
