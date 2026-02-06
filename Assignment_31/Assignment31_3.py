# Design automation script which accept two directory names. Copy all files from first directory into second directory. Second directory should be created at run time.

# Usage :
# DirectoryCopy.py “Demo” “Temp”

import sys
import os
import shutil
import time


def WriteLog(Data):

    fobj = open("DirectoryCopy.log", "a")
    fobj.write(Data + "\n")
    fobj.close()



def CreateLogHeader():

    Border = "-" * 50

    fobj = open("DirectoryCopy.log", "a")

    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory Copy Script\n")
    fobj.write(Border + "\n")

    fobj.close()


def CopyFiles(Source, Dest):

    if(not os.path.exists(Dest)):
        os.mkdir(Dest)
        WriteLog("Destination directory created")

    FileCount = 0

    for File in os.listdir(Source):

        SrcPath = os.path.join(Source, File)
        DestPath = os.path.join(Dest, File)

        if(os.path.isfile(SrcPath)):
            shutil.copy(SrcPath, DestPath)
            WriteLog("COPIED : " + SrcPath)
            FileCount += 1

    
    Border = "-" * 50
    timestamp = time.ctime()

    fobj = open("DirectoryCopy.log", "a")

    fobj.write(Border + "\n")
    fobj.write("Total Files Copied : " + str(FileCount) + "\n")
    fobj.write("Log created at : " + timestamp + "\n")
    fobj.write(Border + "\n")

    fobj.close()


def Process():

    CreateLogHeader()

    if(len(sys.argv) != 3):
        WriteLog("Invalid arguments")
        return

    Source = sys.argv[1]
    Dest = sys.argv[2]

    if(os.path.isdir(Source)):
        CopyFiles(Source, Dest)
    else:
        WriteLog("Source directory not found")


def main():
    Process()

if __name__ == "__main__":
    main()
