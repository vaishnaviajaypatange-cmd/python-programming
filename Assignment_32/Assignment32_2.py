import hashlib
import os
import sys
import time



def WriteLog(Data):

    fobj = open("Duplicate.log","a")
    fobj.write(Data+"\n")
    fobj.close()


def CreateHeader():

    Border = "-"*50

    fobj = open("Duplicate.log","a")
    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("Script Name : Duplicate Finder\n")
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



def FindDuplicate(DirectoryName):

    Duplicate = {}
    FileCount = 0
    DupCount = 0

    if not os.path.isdir(DirectoryName):
        WriteLog("Directory not found")
        return

    for FolderName,SubFolder,FileName in os.walk(DirectoryName):

        for fname in FileName:

            fname = os.path.join(FolderName,fname)
            FileCount += 1

            Checksum = CalculateChecksum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    Result = list(filter(lambda x:len(x)>1,Duplicate.values()))

    for value in Result:

        WriteLog("Duplicate Files :")

        for subvalue in value:
            WriteLog(subvalue)
            DupCount += 1

        WriteLog("-"*40)

    CreateFooter(FileCount,DupCount)



def CreateFooter(FileCount,DupCount):

    Border = "-"*50
    timestamp = time.ctime()

    fobj = open("Duplicate.log","a")
    fobj.write(Border+"\n")
    fobj.write("Total Files Scanned : "+str(FileCount)+"\n")
    fobj.write("Total Duplicate Files : "+str(DupCount)+"\n")
    fobj.write("Log created at : "+timestamp+"\n")
    fobj.write(Border+"\n")
    fobj.close()



def main():

    if(len(sys.argv) != 2):
        WriteLog("Invalid arguments")
        return

    CreateHeader()

    DirectoryName = sys.argv[1]

    FindDuplicate(DirectoryName)



if __name__ == "__main__":
    main()
