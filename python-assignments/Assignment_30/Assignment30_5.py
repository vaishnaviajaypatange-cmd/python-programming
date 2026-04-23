# Q5) Search a Word in File

# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

# Input:
# Demo.txt Marvellous

# Expected Output:
# Display whether the word Marvellous is found in Demo.txt or not.

import sys
import os

def SearchWord(Filename, Word):
    Ret = os.path.exists(Filename)
    if Ret == False:
        return "file does not exist"

    found = False
    fobj = open(Filename, "r")
    for line in fobj:
        words = line.split()
        if Word in words:
            found = True
            break
    fobj.close()

    if found:
        return f"Word '{Word}' found in {Filename}."
    else:
        return f"Word '{Word}' not found in {Filename}."

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py Filename WordToSearch")
        return

    Ret = SearchWord(sys.argv[1], sys.argv[2])
    print(Ret)

if __name__ == "__main__":
    main()
