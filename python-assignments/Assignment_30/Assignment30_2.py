# Q2) Count Words in a File

# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.

# Input:
# Demo.txt

# Expected Output:
# Total number of words in Demo.txt.

import sys
import os

def CountWords(Filename):
    Ret = os.path.exists(Filename)
    if Ret == False:
        return "file does not exist"

    total_words = 0
    fobj = open(Filename, "r")
    for line in fobj:
        words = line.split() 
        total_words += len(words)

    return total_words

def main():
    Ret = CountWords(sys.argv[1])
    print(Ret)

if __name__ == "__main__":
    main()
