# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Drew Cochran, 10FEB2023, Created starter code from Randall Root's example
# Drew Cochran, 11FEB2023, Debugging; corrected errors to menu as function would not operate properly, exit was not
#                          correctly, Remove task was not working while testing; currently thinking of way to not have
#                           'Task' and 'Priority' printed as a header each time file is opened. Believe if statement
#                           will work best, both in the initial reading of file and while writing tasks. Also changed
#                           menu to reflect tasks rather than items like Assignment 04.
# Drew Cochran, 13FEB2023, Stopped trying to make the program write 'task' and 'priority' to .txt file
#
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile_ToDoList = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


def ReadFile():

    # Function to read the file ToDoList.txt into memory for manipulation and display later in the program
    # Try for seeing if file is in home dictionary of program
    try:
        objFile_ToDoList = open("ToDoList.txt", "r")
        for row in objFile_ToDoList:
            lstRow = row.split(",")
            #if lstRow[0] == 'Task':
            #    next()
            #else:
            dicRow = {"Task" : lstRow[0], "Priority" : lstRow[1].strip()}
            lstTable.append(dicRow)
            # print(lstTable)
        objFile_ToDoList.close()

    # Print error statement prompting user to locate file needed to run program
    except:
        print("File not found. Locate ToDoList.txt and ensure file is in the same directory as program.")

#def UserMenu():

    # Menu function to display user choices
#    print("""
#    Menu of Options
#    1) Show current data
#    2) Add a new item.
#    3) Remove an existing item.
#    4) Save Data to File
#    5) Exit Program
#    """)
#    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
#    print()  # adding a new line for looks


# -- Processing -- #
# Step 1 - When the program starts, load any data available from the text file have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# Used a function to read the file in case of future need and calling upon reading the file

ReadFile()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):

    # Calls function UserMenu to display menu of user options
    # UserMenu()
    # Menu function to display user choices
    print("""
    Menu of Options
    1) Show current data
    2) Add a new task.
    3) Remove an existing task.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':

        # Prints the current contents of lstTable after reading in the data from the existing file immediately upon
        # opening program and/or after user has added information to be added to the file. For loop with newline after
        # each task and priority for easier readability.
        for row in lstTable:
            print(row, sep='\n', end='\n')

        # Describing to user what they are seeing, a list with dictionary objects
        print("List with Dictionary objects")
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':

        # Prompts user to add in the task name (one word only) and the priority level (low, medium, high, urgent) to be
        # accomplished. Prompts user to type in exit to return to main menu

        # while loop prompting user to return to main menu by typing exit
        while(True):
            print("Type exit at any prompt to exit to main menu.")
            strTask = input("Task? (what needs to be done, one word only) ")

            if strTask.lower() == "exit":
                break

            strPriority = input("Priority? (low, medium, high, urgent) ")

            if strPriority.lower() == "exit":
                break

            # Appends to lstTable
            lstTable.append({"Task" : strTask, "Priority" : strPriority})

        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        # Prompts user to enter task to remove or exit to quit.
        strRemove = input("Enter the task you would like to remove. Type exit to quit. ")

        # Loop to allow user to remove multiple items if desired. "Exit" quits to main menu. CHECK THIS.
        while (True):
            # If check to determine if user typed "exit"
            if strRemove.lower() == "exit":
                break

            # Else performs user desired action of removing item from list, if the item is found.
            else:
                # Pulls in data from lstTable to prepare for check
                for row in lstTable:
                    # If check to determine if task is found.
                    if row["Task"].lower() == strRemove.lower():
                        lstTable.remove(row)
                        print("Task removed.")
                    # Else statement when item not found. Should go back to main menu. CHECK THIS.
                    else:
                        print("Task not found. Please check the data using Option 1 from the Main Menu.")
                break
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        # Opens and writes to ToDoList.txt, then closes the file.

        # Open ToDoList.txt
        objFile_ToDoList = open("ToDoList.txt", "w")
        # objFile_ToDoList.write("Task, Priority" + '\n')

        # Iterate through lstTable list to write each item to the file. Overwrites existing file data
        for row in lstTable:
            objFile_ToDoList.write(str(row["Task"]) + ', ' + str(row["Priority"]) + '\n')

        # closes file
        objFile_ToDoList.close()
        print("Items saved succesfully!")

        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        # Exits the program. Chose exit rather than break to try since the user is wanting to exit, not just break out
        # of the while loop
        break  # and Exit the program
        # exit()

    # Option if user enters anything other than 1 - 5
    else:
        print("Please choose only option 1 - 5.")
