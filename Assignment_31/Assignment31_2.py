# Design automation script which accept directory name and two file extensions from user. Rename all files with first file extension with the second file extension.

# Usage :
# DirectoryRename.py “Demo” “.txt” “.doc”

import sys
import os
import time


def WriteLog(Data):

    fobj = open("DirectoryRename.log", "a")
    fobj.write(Data + "\n")
    fobj.close()



def CreateLogHeader():

    Border = "-" * 50

    fobj = open("DirectoryRename.log", "a")

    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory Rename Script\n")
    fobj.write(Border + "\n")

    fobj.close()


def ValidateInputs(DirName, Ext1, Ext2):

    if(os.path.isdir(DirName) == False):
        WriteLog("Directory not found")
        return False

    if(not Ext1.startswith(".") or not Ext2.startswith(".")):
        WriteLog("Invalid extension format")
        return False

    return True


def RenameFiles(DirName, Ext1, Ext2):

    FileCount = 0
    RenameCount = 0

    for FolderName, SubFolders, FileNames in os.walk(DirName):

        for File in FileNames:

            FileCount += 1

            if(File.endswith(Ext1)):

                OldPath = os.path.join(FolderName, File)
                NewName = File.replace(Ext1, Ext2)
                NewPath = os.path.join(FolderName, NewName)

                os.rename(OldPath, NewPath)

                WriteLog("RENAMED : " + OldPath + " -> " + NewPath)
                RenameCount += 1

    Border = "-" * 50
    timestamp = time.ctime()

    fobj = open("DirectoryRename.log", "a")

    fobj.write(Border + "\n")
    fobj.write("Total Files Scanned : " + str(FileCount) + "\n")
    fobj.write("Total Files Renamed : " + str(RenameCount) + "\n")
    fobj.write("Log created at : " + timestamp + "\n")
    fobj.write(Border + "\n")

    fobj.close()


def Process():

    CreateLogHeader()

    if(len(sys.argv) != 4):
        WriteLog("Invalid arguments")
        return

    DirName = sys.argv[1]
    Ext1 = sys.argv[2]
    Ext2 = sys.argv[3]

    if(ValidateInputs(DirName, Ext1, Ext2)):
        RenameFiles(DirName, Ext1, Ext2)



def main():
    Process()

if __name__ == "__main__":
    main()
