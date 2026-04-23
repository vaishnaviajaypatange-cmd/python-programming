# Q1) Count Lines in a File

# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.

# Input:
# Demo.txt

# Expected Output:
# Total number of lines in Demo.txt.

import sys
import os

def CountLines(Filename):
    Ret = os.path.exists(Filename)
    if Ret == False:
        return "file does not exist"
    fobj = open(Filename,"r")
    count = 0
    for i in fobj:
        count += 1
    return count


def main():
    Ret = CountLines(sys.argv[1])
    print(Ret)


if __name__ == "__main__":
    main()