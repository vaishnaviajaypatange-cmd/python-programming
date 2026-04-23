# Q5) Frequency of a String in File
# Problem Statement:

# Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.

# Input:
# Demo.txt  Marvellous

# Expected Output:

# Count how many times "Marvellous" appears in Demo.txt.
import sys
import os


def FrequencyOfString(Filename,value):
    Ret = os.path.exists(Filename)
    if Ret == False:
        return "file does not exist"
    
    fobj = open(Filename,"r")
    content = fobj.read()
    count = content.count(value)
    fobj.close()
    
    return count 

def main():
    if len(sys.argv)<3:
        return
    ret = FrequencyOfString(sys.argv[1],sys.argv[2])
    print(ret)

if __name__ == "__main__":
    main()