# Q2) Display File Contents

# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

# Input:
# Demo.txt

# Expected Output:
# Display contents of Demo.txt on console.

import sys
import os

def DisplayFileContent(FileName):
    Ret = os.path.exists(FileName)
     
    if (Ret == False):
        print("file does not exist in the current directory")
    else:
        print("file does exist in current directory")

    fobj = open(FileName,"r")
    print("file gets successfully opened")
    data = fobj.read()
    print("Data from file   : ",data)





def main():
    if len(sys.argv)<2:
        return
    
    DisplayFileContent(sys.argv[1])



if __name__ == "__main__":
    main()


