import hashlib
import os
import sys
import time



def WriteLog(Data):

    fobj = open("DirectoryChecksum.log","a")
    fobj.write(Data+"\n")
    fobj.close()


def CreateHeader():

    Border = "-"*50

    fobj = open("DirectoryChecksum.log","a")
    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("Script Name : Directory Checksum\n")
    fobj.write(Border+"\n")
    fobj.close()


def CalculateChecksum(Filename):

    fobj = open(Filename,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()



def DirectoryChecksum(DirectoryName):

    FileCount = 0

    if not os.path.isdir(DirectoryName):
        WriteLog("Directory not found")
        return

    for FolderName,SubFolder,FileName in os.walk(DirectoryName):

        for fname in FileName:

            fname = os.path.join(FolderName,fname)

            try:
                Checksum = CalculateChecksum(fname)

                WriteLog("File : "+fname)
                WriteLog("Checksum : "+Checksum)
                WriteLog("-"*40)

                FileCount += 1

            except Exception:
                WriteLog("Unable to process : "+fname)

    CreateFooter(FileCount)



def CreateFooter(FileCount):

    Border = "-"*50
    timestamp = time.ctime()

    fobj = open("DirectoryChecksum.log","a")
    fobj.write(Border+"\n")
    fobj.write("Total Files Scanned : "+str(FileCount)+"\n")
    fobj.write("Log created at : "+timestamp+"\n")
    fobj.write(Border+"\n")
    fobj.close()


def main():

    if(len(sys.argv) != 2):
        WriteLog("Invalid arguments")
        return

    CreateHeader()

    DirectoryName = sys.argv[1]

    DirectoryChecksum(DirectoryName)



if __name__ == "__main__":
    main()
