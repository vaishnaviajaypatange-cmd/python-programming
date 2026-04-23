# Q4) Compare Two Files (Command Line)
# Problem Statement:

# Write a program which accepts two file names through command line arguments and compares the contents of both files.

# If both files contain the same contents, display Success

# Otherwise display Failure

# Input (Command Line):
# Demo.txt  Hello.txt

# Expected Output:
# Success OR Failure


import sys
import os
import hashlib

def CalculateChecksum(FileName1,FileName2):
    fobj1 = open(FileName1,"rb")
    fobj2 = open(FileName2,"rb")

    hobj1 = hashlib.md5()
    hobj2 = hashlib.md5()

    Buffer = fobj1.read(1024)
    while (len(Buffer)>0):
        hobj1.update(Buffer)
        Buffer = fobj1.read(1024)


    Buffer = fobj2.read(1024)
    while (len(Buffer)>0):
        hobj2.update(Buffer)
        Buffer = fobj2.read(1024)

    checksum1 = hobj1.hexdigest()
    checksum2 = hobj2.hexdigest()
    
    fobj1.close()
    fobj2.close()

    return checksum1,checksum2


def CompareFileContent(FileName1,FileName2):
    Ret = os.path.exists(FileName1)
    if Ret == False:
        return "file 1 does not exist"
    Ret = os.path.exists(FileName2)
    if Ret == False:
        return "file 2 does not exist"
    
    Ret = CalculateChecksum(FileName1,FileName2)
    if Ret[0] == Ret[1]:
        return "Success"
    else:
        return "Failure"


def main():
    if len(sys.argv)<3:
        return
    
    Result = CompareFileContent(sys.argv[1],sys.argv[2])
    print(Result)

if __name__ == "__main__":
    main()



    ####here we have to use hashlib to get checknum using md5 so that we can compare the content#####

        


    # with open(FileName1, "r") as fobj1, open(FileName2, "r") as fobj2:
    #     if fobj1.read() == fobj2.read():
    #         return "Success"
    #     else:
    #         return "Failure"
