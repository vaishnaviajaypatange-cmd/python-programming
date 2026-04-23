# 1. Design automation script which accept directory name and file extension from user. Display all files with that extension.

# Usage : DirectoryFileSearch.py “Demo” “.txt”

# Demo is name of directory and .txt is the extension that we want to search.

import sys
import os
import time



def WriteLog(Data):

    fobj = open("DirectoryFileSearch.log", "a")
    fobj.write(Data + "\n")
    fobj.close()


def ValidateInputs(DirName, Extension):

    if(os.path.isdir(DirName) == False):
        WriteLog("Directory not found")
        return False

    if(Extension.startswith(".") == False):
        WriteLog("Invalid extension")
        return False

    return True



def DirectoryFileSearch(DirName, Extension):

    try:
        Flag = False
        FileCount = 0
        MatchCount = 0

        for FolderName, SubFolders, FileNames in os.walk(DirName):

            for File in FileNames:

                FileCount += 1  
                if(File.endswith(Extension)):
                    FilePath = os.path.join(FolderName, File)
                    WriteLog("FOUND : " + FilePath)
                    MatchCount += 1
                    Flag = True

        if(Flag == False):
            WriteLog("No files found")

        Border = "-" * 50
        timestamp = time.ctime()

        fobj = open("DirectoryFileSearch.log", "a")

        fobj.write(Border + "\n")
        fobj.write("Total Files Scanned : " + str(FileCount) + "\n")
        fobj.write("Total Matching Files Found : " + str(MatchCount) + "\n")
        fobj.write("This log file is created at : " + timestamp + "\n")
        fobj.write(Border + "\n")

        fobj.close()
    except Exception:
        WriteLog("Searching failed")


def ProcessDirectorySearch():
    Border = "-" * 50

    fobj = open("DirectoryFileSearch.log", "a")

    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory File Search Script\n")
    fobj.write(Border + "\n")

    fobj.close()

    try:
        if(len(sys.argv) != 3):
            WriteLog("Invalid arguments")
            return

        DirName = sys.argv[1]
        Extension = sys.argv[2]

        Ret = ValidateInputs(DirName, Extension)

        if(Ret == True):
            DirectoryFileSearch(DirName, Extension)

    except Exception:
        WriteLog("Unexpected error")

def main():
    Border = "-"*50
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)

    ProcessDirectorySearch()


if __name__ == "__main__":
    main()
