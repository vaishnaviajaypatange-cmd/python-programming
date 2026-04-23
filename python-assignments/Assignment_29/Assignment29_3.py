# Q3) Copy File Contents into a New File (Command Line)
# Problem Statement:

# Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.

# Input (Command Line):
# ABC.txt

# Expected Output:

# Create Demo.txt and copy contents of ABC.txt into Demo.txt.
import sys
import os

def CopyFile(FileName):
    
    Ret = os.path.exists(FileName)
     
    if (Ret == False):
        print("file does not exist in the current directory")
        return
    else:
        print("file does exist in current directory")

    fobj = open(FileName,"r")
    print("file gets successfully opened")
    data = fobj.read()
    fobj2 = open("Demo.txt","w")
    fobj2.write(data)
    print("Demo.txt created successfully and data copied!")

    fobj.close()
    fobj2.close()

    

def main():
    if len(sys.argv)<2:
        return
    
    CopyFile(sys.argv[1])


if __name__ == "__main__":
    main()