INSTRUCTIONS 
	How to use
		First once the code is running you have 13 options of what to do
		The only functions that will work at first are the first three because the rest need items in a list for them to function.
		Those options are
			Add to a list
				Once you type 1 you will get a message that asks you to type a new integer. Once you type that number and hit enter it will be added to myList.
			Add a bunch of numbers
				Once you type 2 you will get a message that asks you how many new integers you want to add. The number you type will be how many new numbers it adds. Then it will 
				ask how high you want to numbers to go. This is the range the number you type makes it so that any number added cant be higher than that number. Once you hit enter 
				it will add the number of numbers you put for the first input and those are all random between 0 and the second inputted number.
			Add a few
				Once you type 3 you will get a message that says that you can add as many numbers to the list as you like and when you are done to type stop.
			Return the value at an index position
				Once you type 4 you will get a message that asks you what index position you are curious about. For this, you just type the index position you want to look at and 
				it will show you what number is at that position.
			Sort list
				Once you type 5 you will get a message that asks you if you want to see your new list. If you do type y if you don’t type n.
			Random Search 
				Once you type 6 you will get a message that says RaNdOm SeArCh?!? And then a random number in your list.
			Linear Search  
				Once you type 7 you will get a message asking you what number you were looking for.  Once you type in the number you were looking for and hit Enter it will 
				search myList for the number you inputted and give you the positions of that number in that list.
			Recursive Binary Search
				Once you type 8 you will get a message asking you what number you were looking for. Once you type in the number you were looking for and hit Enter it will tell 
				you the position of the item in unique_list.
			Iterative Binary Search
				Once you type 9 you will get a message asking you what number you were looking for. Once you type in the number you were looking for and hit Enter it will tell 
				you the position of the item in unique_list.
			Print lists
				Once you type 10 you will get a message asking you which list you want to print. 
					If you type sorted it will print unique_list
					If you type unsorted it will print myList
			Delete a number from a list
				Once you type 11 you will get a message asking you which list you would like to delete a number from, myList or unique_list. Then it will ask you what number you 
				want to delete (from the list you previously selected).  Once you hit Enter, it will delete the number from the list you selected.
			Clear List
				Once you type 12 you will get a message asking you which list you would like to clear, myList or unique_list. Once you choose one, it will ask you if you are sure 
				you want to clear the list.
					If you type Y, it will clear the list
					If you type N, it will quit and not clear the list
			Quit
				Once you type 13, it will quit the program.
	Notes
		Creating lists
			The purpose of creating the initial list, myList, is so that we actually have a place to store the items.
			The purpose of the secondary list, unique_list, is to work with the data from myList without changing that original data.
		Sorting lists
			In order for recursive and linear binary search to function, lists must be sorted. (See Binary Search section)
			The way we sort the data is by taking data from myList and moving it to unique_list and sorting it numerically.




BINARY SEARCH

	In a binary search, the number list is cut in half, making it into two lists by determining the middle value of the entire list. We do this by taking the lowest number and the highest number 
	in the list, adding them together, then dividing them by two to find the midpoint. Once you have the middle number, it checks to see if the inputted number is greater than or less than the 
	middle number. If it is greater than, it makes the middle point the new low point and keeps the highest number the high point, essentially cutting the list in half. The opposite is true if 
	the number is less than the middle point, with the middle number becoming the high point and keeping the lowest number the low point. The limitation and requirement for this binary search 
	are that the list has to be numerically sorted in order for it to work. One of the advantages is that, if the list is sorted, it is very efficient and quick at finding the desired item.

	A recursive binary search algorithm works by calling itself, but when calling itself, changes the value of the midpoint so that when it runs again, the list is halved. For example, in our 
	recursive binary search algorithm, we use a series of if, elif, and else statements to check the relationship between the inputted value x and the midpoint. First, it checks to see if they 
	are equal to each other and, if they are, sending that index position. If it is not, it passes it by and moves on to the elif statement, which checks to see if the midpoint is greater than 
	x. If it is greater than x, it reruns the function with the old midpoint as the new highpoint. The opposite is true of the next statement - the else statement - which means the midpoint is 
	less than x and it makes the midpoint the new low point. It continues this process until the midpoint is equal to x. This process is recursive because it is calling itself inside of itself.  

	A linear binary search algorithm works by using a loop in which the length is determined by the values in the list. For example, in our linear binary search algorithm, we use a while loop 
	that stops when the low value is greater than the high value. Inside of the while loop it iterates through similarly to the recursive binary search algorithm by using if, elif, and else 
	statements. However, the major difference is that in this search, because it is a while loop, it does not call itself inside of itself. Additionally, the order of the greater than, less 
	than, and equal to is different. Once the low point is greater than the high point, it returns the index position. The reason this is a linear search is because, instead of calling itself 
	inside of itself, it uses loops to repeat the code.






CHANGES YOU MADE/WANT TO MAKE

	One of the major improvements that could be made to the code is determining where any errors show up and fixing them so it does not produce errors anymore. An example of this is in addAFew 
	when you type stop, it gives you an error because it is not an integer. A way I can fix this is by adding in more conditional statements, such as if and elif, to make more checks before it 
	would be checked as an integer.  

	Another example is in deleteListItem. If you select that you want to delete an item from myList, it gives you an error. It would take some troubleshooting to determine where the error is 
	coming from, but because of the similarity between this code and the code in clearList, the clearList code could be used to help fix this error, which would speed up the process.
