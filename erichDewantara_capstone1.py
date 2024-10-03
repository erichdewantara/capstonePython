from tabulate import tabulate

# master data
employeesData = [
    ["EmpID", "Given Name", "Surname", "Age", "Gender", "Job Title", "Status"],
    ["RB0001", "Jordan", "Peterson", 34, "Male", "Retail Banking", "Active"],
    ["CB0001", "Samantha", "Cole", 29, "Female", "Corporate Banking", "Active"],
    ["MC0001", "Avery", "Clark", 27, "Male", "Marketing And Communication", "On Leave"],
    ["IB0001", "Alex", "Martinez", 42, "Male", "Investment Banking", "Active"],
    ["CR0001", "Riley", "Thompson", 37, "Female", "Credit Risk", "Active"],
    ["MC0002", "Drew", "Sullivan", 39, "Male",  "Marketing And Communication", "Active"],
    ["RB0002", "Taylor", "Nguyen", 31, "Male", "Retail Banking", "Non Active"],
    ["CR0002", "Morgan", "Lee", 45, "Female", "Credit Risk", "Active"],
    ["IT0001", "Casey", "Patel", 33, "Female", "Information Technology", "On Leave"],
    ["MC0003", "Jamie", "Brooks", 28, "Male", "Marketing And Communication", "Active"]
]

dictGender = {
    1: "Male",
    2: "Female"
}

dictJobTitle = {
    1: "Retail Banking",
    2: "Corporate Banking",
    3: "Marketing And Communication",
    4: "Investment Banking",
    5: "Credit Risk",
    6: "Information Technology" 
}

dictStatus = {
    1: "Active",
    2: "Non Active",
    3: "On Leave"
}

dictColumnName = {
    1: "EmpID",
    2: "Given Name",
    3: "Surname",
    4: "Age",
    5: "Gender",
    6: "Job Title",
    7: "Status"
}

# EID format checker
def EID_checker(inputEID):
    code = inputEID[:2]
    number = inputEID[2:]
    if not code.isalpha() or len(code) != 2 or not number.isdigit() or len(number) != 4:
        print("Invalid Employee ID format!")
        return False
    return True

# EID existence checker
def EID_exist(inputEID):
    for employee in employeesData:  # check if EID exist
        if inputEID == employee[0]:
            print("Employee ID already exist!")
            return False
    return True

# EID not exist checker
def EID_notExist(inputEID):
    for employee in employeesData:  # check if EID exist
        if inputEID == employee[0]:
            return True
    print("Employee not exist!")
    return False

# func R
def readMenu():
    while True:
        try:
            print("Options:\n1. View All Records\n2. Browse Employee\n3. Back to Home")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                readSubMenu_listAllEmployee()
            elif choice == 2:
                readSubMenu_searchEmployee()
            elif choice == 3:
                startProgram()
            else:
                print("No menu chosen!")
        except ValueError:
            print("Enter number only!")

# sub func R1
def readSubMenu_listAllEmployee():
    if len(employeesData) > 1:   # data exist
        table = tabulate(employeesData[1:], headers = employeesData[0], tablefmt = "pipe")
        print(table)
        
        # sorting
        def sortEmployee(sortbyColumn, sortbyOrder):
            global employeesData
            
            # ascending
            if sortbyOrder == 1:
                for key, val in dictColumnName.items():
                    if sortbyColumn == key:
                        sortbyColumn = val

                header = employeesData[0]
                data = employeesData[1:]

                columnIndex = employeesData[0].index(sortbyColumn)  # get index
    
                data.sort(key = lambda x: x[columnIndex])
                employeesData = [header] + data

            # descending
            elif sortbyOrder == 2:
                for key, val in dictColumnName.items():
                    if sortbyColumn == key:
                        sortbyColumn = val

                header = employeesData[0]
                data = employeesData[1:]

                columnIndex = employeesData[0].index(sortbyColumn)            
    
                data.sort(key = lambda x: x[columnIndex], reverse = True)
                employeesData = [header] + data

        while True:
            try:
                print("Options:\n1. Sort Records\n2. Back")
                choice = int(input("Enter your choice: "))
                if choice == 2:
                    readMenu()
                elif choice == 1:
                    while True:
                        try:
                            print("Sort by:\n1. Employee ID\t\t5. Gender\n2. Given Name\t\t6. Job Title\n3. Surname\t\t7. Status\n4. Age\t\t\t8. Back")
                            sortbyColumn = int(input("Enter your choice: "))
                            if sortbyColumn == 8:
                                readSubMenu_listAllEmployee()
                            elif sortbyColumn >= 9:
                                print("No menu chosen!")
                            else:
                                while True:
                                    try:
                                        print("Order by?\n1. Ascending\n2. Descending")
                                        sortbyOrder = int(input("Enter number: "))
                                        if sortbyOrder == 1 or sortbyOrder == 2:
                                            sortEmployee(sortbyColumn, sortbyOrder)
                                            readSubMenu_listAllEmployee()
                                        else:
                                            print("No menu chosen!")
                                    except ValueError:
                                        print("Enter number only!")
                        except ValueError:
                            print("Enter number only!")
                else:
                    print("No menu chosen!")
            except ValueError:
                print("Enter number only!")

    elif len(employeesData) == 1:
        print("Records does not exist!")
    
    readMenu()

# sub func R2
def readSubMenu_searchEmployee():
    while True:
        try:
            print("Search by:\n1. Employee ID\t\t5. Gender\n2. Given Name\t\t6. Job Title\n3. Surname\t\t7. Status\n4. Age\t\t\t8. Back")
            choice = int(input("Enter your choice: "))

            def searchEmployee(searchBy):
                while True:
                    if searchBy == "Gender":
                        print("List of Gender:\n1. Male\n2. Female")
                    elif searchBy == "Job Title":
                        print("List of Job Title:\n1. Retail Banking\t\t4. Investment Banking\n2. Corporate Banking\t\t5. Credit Risk\n3. Marketing And Communication\t6. Information Technology")
                    elif searchBy == "Status":
                        print("List of Status:\n1. Active\n2. Non Active\n3. On Leave")
                    
                    userInput = input(f"Enter {searchBy} (N to back): ")
                    if userInput.upper() == "N":
                        readSubMenu_searchEmployee()
                    else:
                        matchingEmployee = []   # store the data, so there'll be more than 1 output
                        for employee in employeesData[1:]:
                            if searchBy == "EmpID" and employee[0] == userInput.upper():
                                matchingEmployee.append(employee)
                            elif searchBy == "Given Name" and employee[1] == userInput.capitalize():
                                matchingEmployee.append(employee)
                            elif searchBy == "Surname" and employee[2] == userInput.capitalize():
                                matchingEmployee.append(employee)
                            elif searchBy == "Age" and employee[3] == int(userInput):
                                matchingEmployee.append(employee)
                            elif searchBy == "Gender":
                                statement = ""
                                for key, val in dictGender.items():
                                    if key == int(userInput):
                                        statement += val
                                if employee[4] == statement:
                                    matchingEmployee.append(employee)
                            elif searchBy == "Job Title":
                                statement = ""
                                for key, val in dictJobTitle.items():
                                    if key == int(userInput):
                                        statement += val
                                if employee[5] == statement:
                                    matchingEmployee.append(employee)
                            elif searchBy == "Status":
                                statement = ""
                                for key, val in dictStatus.items():
                                    if key == int(userInput):
                                        statement += val
                                if employee[6] == statement:
                                    matchingEmployee.append(employee)
                        
                        if matchingEmployee:
                            table = tabulate(matchingEmployee[0:], headers = employeesData[0], tablefmt = "pipe")
                            print(table)

                            readMenu()

                        else:
                            print("Employee not found!")
                            readMenu()

            if choice in dictColumnName:
                searchEmployee(dictColumnName[choice])
            elif choice == 8:
                readMenu()
            else:
                print("No input chosen")
        
        except ValueError:
            print("Enter number only!")

# func C
def createMenu():
    while True:
        try:
            print("Options:\n1. Add New Employee Information\n2. Back to Home")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                createSubMenu_newEmployee()
            elif choice == 2:
                startProgram()
            else:
                print("No menu chosen!")
        except ValueError:
            print("Enter number only!")

# sub func C1
def createSubMenu_newEmployee():
    table = tabulate(employeesData[1:], headers = employeesData[0], tablefmt = "pipe")
    print(table)
    
    while True:
        inputEID = input("Enter Employee ID (N to back): ").upper()
        if inputEID == "N":
            createMenu()
        
        # check EID format
        if not EID_checker(inputEID):
            continue    # if falsy, back to input

        # check if EID exist
        if not EID_exist(inputEID):
            continue    # if falsy, back to input
    
        else:
            newGivenName = input("Given Name: ").capitalize()
            newSurname = input("Surname: ").capitalize()   
        
            while True:
                try:
                    newAge = int(input("Age: "))
                    break
                except ValueError:
                    print("Enter number only!")

            while True:
                try:
                    print("1. Male\n2. Female")
                    newGender = int(input("Gender: "))
                    break
                except ValueError:
                    print("Enternumber only!")

            while True:
                try:
                    print("List of Job Title:\n1. Retail Banking\t\t4. Investment Banking\n2. Corporate Banking\t\t5. Credit Risk\n3. Marketing And Communication\t6. Information Technology")
                    newJobTitle = int(input("Job Title: "))
                    break
                except ValueError:
                    print("Enter number only!")

            while True:
                try:
                    print("List of Status:\n1. Active\n2. Non Active\n3. On Leave")
                    newStatus = int(input("Status: "))
                    break
                except ValueError:
                    print("Enter number only!")
            
            # append to list
            while True:
                choice = input("Save record (Y/N)? ").upper()
                if choice == "N":
                    createMenu()
                elif choice == "Y":
                    for key, val in dictGender.items():
                        if key == newGender:
                            newGender = val
                    for key, val in dictJobTitle.items():
                        if key == newJobTitle:
                            newJobTitle = val
                    for key, val in dictStatus.items():
                        if key == newStatus:
                            newStatus = val
                    
                    employeesData.append([inputEID, newGivenName, newSurname, newAge, newGender, newJobTitle, newStatus])
                    print("Employee added successfully!")
                    createMenu()
                else:
                    print("Enter Y/N only!")

# func U
def updateMenu():
    while True:
        try:
            print("Options:\n1. Update Employee Information\n2. Back to Home")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                updateSubMenu_updateInfo()
            elif choice == 2:
                startProgram()
            else:
                print("No menu chosen!")
        except ValueError:
            print("Enter number only!")

# sub func U1
def updateSubMenu_updateInfo():
    table = tabulate(employeesData[1:], headers = employeesData[0], tablefmt = "pipe")
    print(table)

    while True:
        inputEID = input("Enter Employee ID to update (N to back): ").upper()
        if inputEID == "N":
            updateMenu()
        
        # EID format checker
        if not EID_checker(inputEID):
            continue    # if falsy; back to input

        # EID exist checker
        if not EID_notExist(inputEID):
            continue
        
        # storing the appointed EID
        inputResult = [["EmpID", "Given Name", "Surname", "Age", "Gender", "Job Title", "Status"]]
        for employee in employeesData:
            if employee[0] == inputEID:
                inputResult.append(employee)
        
        table = tabulate(inputResult[1:], headers = employeesData[0], tablefmt = "pipe")
        print(table)
        
        while True:
            confirmation = input("Continue update (Y/N)? ").upper()
            if confirmation == "N":
                updateMenu()
            
            elif confirmation == "Y":
                def updateInformation(employeesData, inputEID, inputColumn, inputNewValue):
                    header = employeesData[0]
                    columnIndex = header.index(inputColumn)

                    for row in employeesData[1:]:
                        if row[0] == inputEID:
                            row[columnIndex] = inputNewValue
                            break
                
                # appoint column
                while True:
                    try:
                        print("List of Column:\n1. EmpID\t\t5. Gender\n2. Given Name\t\t6. Job Title\n3. Surname\t\t7. Status\n4. Age")
                        choiceColumn = int(input("Enter number of designated column to update: "))
                        inputColumn = ""
                        for key, val in dictColumnName.items():
                            if key == choiceColumn:
                                inputColumn += val
                    except ValueError:
                        print("Enter number only!")

                    # personalize each input
                    if inputColumn == "EmpID":
                        inputNewValue = input("Enter new value: ").upper()
                        if not EID_checker(inputNewValue):
                            continue
                        if not EID_exist(inputNewValue):
                            continue
                    elif inputColumn == "Age":
                        while True:
                            try:
                                inputNewValue = int(input("Enter new value: "))
                                break
                            except ValueError:
                                print("Enter number only!")
                    elif inputColumn == "Gender":
                        while True:
                            try:
                                print("1. Male\n2. Female")
                                inputNewValue = int(input("Enter number for new value: "))
                                for key, val in dictGender.items():
                                    if key == inputNewValue:
                                        inputNewValue = val
                                break
                            except ValueError:
                                print("Enter number only!")
                    elif inputColumn == "Status":
                        while True:
                            try:
                                print("List of Status:\n1. Active\n2. Non Active\n3. On Leave")
                                inputNewValue = int(input("Enter number for new value: "))
                                for key, val in dictStatus.items():
                                    if key == inputNewValue:
                                        inputNewValue = val
                                break
                            except ValueError:
                                print("Enter number only!")
                    else:
                        inputNewValue = input("Enter new value: ").title()
                    break

                while True:
                    reconfirmation = input("Save changes (Y/N)? ").upper()
                    if reconfirmation == "N":
                        print("Undo changes..")
                        updateMenu()
                    elif reconfirmation == "Y":
                        updateInformation(employeesData, inputEID, inputColumn, inputNewValue)
                        print("Save success!")
                        updateMenu()
                    else:
                        print("Enter Y/N only!")
            else:
                print("Enter Y/N only!")

# func D
def deleteMenu():
    while True:
        try:
            print("Options:\n1. Remove Record\n2. Clear All Records\n3. Back to Home")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                deleteSubMenu_removeRecord()
            elif choice == 2:
                deleteSubMenu_clearRecord()
            elif choice == 3:
                startProgram()
            else:
                print("No menu chosen!")
        except ValueError:
            print("Enter number only!")

# sub func D1
def deleteSubMenu_removeRecord():
    while True:
        try:
            print("Search record by:\n1. Employee ID\t\t5. Gender\n2. Given Name\t\t6. Job Title\n3. Surname\t\t7. Status\n4. Age\t\t\t8. Back")
            choice = int(input("Enter your choice: "))

            def deleteRecord(searchBy):
                while True:
                    if searchBy == "Gender":
                        print("List of Gender:\n1. Male\n2. Female")
                    elif searchBy == "Job Title":
                        print("List of Job Title:\n1. Retail Banking\t\t4. Investment Banking\n2. Corporate Banking\t\t5. Credit Risk\n3. Marketing And Communication\t6. Information Technology")
                    elif searchBy == "Status":
                        print("List of Status:\n1. Active\n2. Non Active\n3. On Leave")

                    userInput = input(f"Enter {searchBy} (N to back): ")
                    if userInput.upper() == "N":
                        deleteSubMenu_removeRecord()
                    else:
                        matchingEmployee = []
                        for employee in employeesData[1:]:
                            if searchBy == "EmpID" and employee[0] == userInput.upper():
                                matchingEmployee.append(employee)
                            elif searchBy == "Given Name" and employee[1] == userInput.capitalize():
                                matchingEmployee.append(employee)
                            elif searchBy == "Surname" and employee[2] == userInput.capitalize():
                                matchingEmployee.append(employee)
                            elif searchBy == "Age" and employee[3] == int(userInput):
                                matchingEmployee.append(employee)
                            elif searchBy == "Gender":
                                statement = ""
                                for key, val in dictGender.items():
                                    if key == int(userInput):
                                        statement += val
                                if employee[4] == statement:
                                    matchingEmployee.append(employee)
                            elif searchBy == "Job Title":
                                statement = ""
                                for key, val in dictJobTitle.items():
                                    if key == int(userInput):
                                        statement += val
                                if employee[5] == statement:
                                    matchingEmployee.append(employee)
                            elif searchBy == "Status":
                                statement = ""
                                for key, val in dictStatus.items():
                                    if key == int(userInput):
                                        statement += val
                                if employee[6] == statement:
                                    matchingEmployee.append(employee)
                        
                        if matchingEmployee:
                            indexedTable = [["Index"] + employeesData[0]]
                            indexedTable += [[indexing + 1] + row for indexing, row in enumerate(matchingEmployee)]

                            table = tabulate(indexedTable[1:], headers = indexedTable[0], tablefmt = "pipe")
                            print(table)

                            def deleteMatchingRecord():
                                index = matchingEmployee[deleteChoice - 1]
                                for i, employee in enumerate(employeesData):
                                    if employee == index:
                                        del employeesData[i]
                                print("Record successfully deleted!")

                            while True:
                                deleteChoice = input("Enter the index to delete the record (N to Back): ")
                                if deleteChoice.upper() == "N":
                                    deleteRecord(searchBy)
                                elif not deleteChoice.isdigit():
                                    print("Enter number only!")
                                elif 0 < int(deleteChoice) <= len(matchingEmployee):    # set the range of input
                                    deleteChoice = int(deleteChoice)
                                    confirmation = input("Delete this record (Y/N)? ").upper()
                                    if confirmation == "Y":
                                        deleteMatchingRecord()
                                        deleteMenu()
                                    elif confirmation == "N":
                                        continue
                                    else:
                                        print("Enter Y/N only!")
                                else:
                                    print("Index out of range!")
                        else:
                            print("Employee not found!")

            if choice in dictColumnName:
                deleteRecord(dictColumnName[choice])
            elif choice == 8:
                deleteMenu()
            else:
                print("No input chosen")

        except ValueError:
            print("Enter number only!")

# sub func D2
def deleteSubMenu_clearRecord():
    while True:
        choice = input("Delete all record (Y/N)? ").upper()
        if choice == "Y":
            print("Deleting all records..")
            del employeesData[1:]
            deleteMenu()
        elif choice == "N":
            print("Undo changes..")
            deleteMenu()
        else:
            print("Enter Y/N only!")

# start
def startProgram():
    while True:
        try:
            print("--WELCOME TO PURWADHIKA BANK EMPLOYEES' DATABASE--\nHome:\n1. Explore Employee\n2. New Records\n3. Modify Records\n4. Delete Records\n5. Exit Program")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                readMenu()
            elif choice == 2:
                createMenu()
            elif choice == 3:
                updateMenu()
            elif choice == 4:
                deleteMenu()
            elif choice == 5:
                print("Bye~")
                exit()
            else:
                print("No menu chosen!")
        except ValueError:
            print("Enter number only!")

startProgram()
