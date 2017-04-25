# Pok On Cheng and Nhu Tuyet Huynh. Lab Section 1 Project #1

import shutil, os

def Search_files_by_path(path: str) -> None:
    ''' This method is to search the file with the path.
    '''
    if os.path.isdir(path):
        print("Directory found! LOL")
    else:
        print("The directory does not exist... Orz Please try another one!")

while True:
    file = input("What is the path of file?")
    Search_files_by_path(file)
    myString = input("Do you want to search again?(Yes/No)")
    myString = myString.upper()
    if myString == "NO":
        break
    

def Search_by_name(file: str) -> None:
    Search_files_by_path(file)
    files = "You are interested in "
    files += file
    print(files)

##while True:
##    files = []
##    file = input("What is the file?")
##    Search_by_name(file)
##    files.append(file)
##    myString = input("Do you want to search again?(Yes/No)")
##    myString = myString.upper()
##    if myString == "NO":
##        print("You are interested in ", files)
##        break


def Search_by_name_ending(ending: str) -> None:
    new_list = []
    new_string = ""
    for files in os.listdir("."):
        if files.endswith(ending):
            new_list.append(files)
    for a in new_list:
        if a != new_list[-1]:
            new_string = new_string + a + ", "
        else:
            new_string = new_string + a + "."
    if new_string != "":
        print("You are interested in", new_string)
    else:
        print("File type not match!")

##while True:
##    file = input("What is the ending of the files?")
##    Search_by_name_ending(file)
##    break

def Search_by_size(size: float) -> None:
    new_list = []
    new_string = ""
    for files in os.listdir("."):
        file_size = 0
        file_size = os.path.getsize(files)
        if size < file_size:
            new_list.append(files)
    for a in new_list:
        if a != new_list[-1]:
            new_string = new_string + a + ", "
        else:
            new_string = new_string + a + "."
    if new_string != "":
        print("You are interested in", new_string)
    else:
        print("No match!")

##while True:
##    file = float(input("What is the size of the files?"))
##    Search_by_size(file)
##    break




        

def print_path_only(file: str) -> None:
    print(os.path.abspath(file))

##print_path_only('Lab1.txt')

def print_first_of_text(file: str) -> None:
    
    infile = open(file,'r')
    new_list = [ ]
    for first_line in infile:
        new_list.append(first_line.strip())
    print(new_list[0])
    infile.close()

##print_first_of_text('Lab1.txt')

def Copy_File(file: str) -> None:
    files = ""
    files = file + '.dup'
    shutil.copy2(file, files)

##Copy_File('Lab1.txt')

import time

def Touch_File(file: str) -> None:
    os.utime(file, (time.time(), time.time()))

##Touch_File('Lab1.txt')

MENU = """
Menu --- Choose one?!
sbn: Search file by name
sne: Search of file's name ending
sbs: Search file by size
"""

def Menu():
    while True:
        response = input(MENU)
        response = response.lower()
        if response == "sbn":
            file = input("\nWhich file do you want to use?")
            Search_by_name(file)
        elif response == "sne":
            ending = input("\nWhat is the ending of the files?")
            Search_by_name_ending(ending)
        elif response == "sbs":
            size = float(input("\nWhat is the size of the files?"))
            Search_by_size(size)
        ex = input("\nDo you want to do it again? (Yes/No)")
        ex = ex.upper()
        if ex == "NO":
            break

Menu()

MENU_1 = """
Menu --- Choose one.
ppo: Print Path Only
pft: Print the first line of text
cof: Copy the file and rename it
tof: Change the timestamp
"""

def Menu_1():
    while True:
        response = input(MENU_1)
        response = response.lower()
        if response == "ppo":
            file = input("\nWhich file do you want to use?")
            print_path_only(file)
        elif response == "pft":
            file = input("\nWhich file do you want to use?")
            print_first_of_text(file)
        elif response == "cof":
            file = input("\nWhich file do you want to use?")
            Copy_File(file)
        elif response == "tof":
            file = input("\nWhich file do you want to use?")
            Touch_File(file)
        ex = input("\nDo you want to do it again? (Yes/No)")
        ex = ex.upper()
        if ex == "NO":
            break

Menu_1()

