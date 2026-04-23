# Design automation script which accept two directory names and one file extension. Copy all files with the specified extension from first directory into second directory. Second directory should be created at run time.

# Usage :
# DirectoryCopyExt.py “Demo” “Temp” “.exe”

import sys
import os
import shutil
import time



def WriteLog(Data):

    fobj = open("DirectoryCopyExt.log", "a")
    fobj.write(Data + "\n")
    fobj.close()


def CreateLogHeader():

    Border = "-" * 50

    fobj = open("DirectoryCopyExt.log", "a")

    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory Copy By Extension Script\n")
    fobj.write(Border + "\n")

    fobj.close()



def CopyFilesByExt(Source, Dest, Extension):

    if(not os.path.exists(Dest)):
        os.mkdir(Dest)
        WriteLog("Destination directory created")

    FileCount = 0
    CopyCount = 0

    for File in os.listdir(Source):

        SrcPath = os.path.join(Source, File)

        if(os.path.isfile(SrcPath)):
            FileCount += 1

            if(File.endswith(Extension)):

                DestPath = os.path.join(Dest, File)
                shutil.copy(SrcPath, DestPath)

                WriteLog("COPIED : " + SrcPath)
                CopyCount += 1

    
    Border = "-" * 50
    timestamp = time.ctime()

    fobj = open("DirectoryCopyExt.log", "a")

    fobj.write(Border + "\n")
    fobj.write("Total Files Scanned : " + str(FileCount) + "\n")
    fobj.write("Total Files Copied : " + str(CopyCount) + "\n")
    fobj.write("Log created at : " + timestamp + "\n")
    fobj.write(Border + "\n")

    fobj.close()



def Process():

    CreateLogHeader()

    if(len(sys.argv) != 4):
        WriteLog("Invalid arguments")
        return

    Source = sys.argv[1]
    Dest = sys.argv[2]
    Extension = sys.argv[3]

    if(os.path.isdir(Source)):
        CopyFilesByExt(Source, Dest, Extension)
    else:
        WriteLog("Source directory not found")



def main():
    Process()

if __name__ == "__main__":
    main()
