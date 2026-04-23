# Q1) Check File Exists in Current Directory

# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

# Input:
# Demo.txt

# Expected Output:
# Display whether Demo.txt exists or not.
import sys
import os

def CheckDirectory(FileName):
    Ret = os.path.exists(FileName)
     
    if (Ret == False):
        print("file does not exist in the current directory")
    else:
        print("file does exist in current directory")




def main():
    if len(sys.argv)<2:
        return
    
    CheckDirectory(sys.argv[1])



if __name__ == "__main__":
    main()



