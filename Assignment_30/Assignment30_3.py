# Q3) Display File Line by Line

# Problem Statement:
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.

# Input:
# Demo.txt

# Expected Output:
# Display each line of Demo.txt one by one.

import sys
import os

def DisplayFile(Filename):
    ret = os.path.exists(Filename)
    if ret == False:
        return "File does not exist"

    with open(Filename, "r") as fobj:
        for line in fobj:
            print(line, end='') 

def main():
    DisplayFile(sys.argv[1])

if __name__ == "__main__":
    main()
