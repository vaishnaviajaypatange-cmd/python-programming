import hashlib
import os
import sys
import time



def WriteLog(Data):

    fobj = open("DuplicateRemoval.log","a")
    fobj.write(Data+"\n")
    fobj.close()


def CreateHeader():

    Border = "-"*50

    fobj = open("DuplicateRemoval.log","a")
    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("Script Name : Duplicate Removal\n")
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

def DeleteDuplicate(DirectoryName):

    Duplicate = {}
    FileCount = 0
    DeleteCount = 0

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

        Count = 0

        for subvalue in value:

            Count += 1

            if Count > 1:
                os.remove(subvalue)
                WriteLog("Deleted File : "+subvalue)
                DeleteCount += 1

    CreateFooter(FileCount,DeleteCount)



def CreateFooter(FileCount,DeleteCount):

    Border = "-"*50
    timestamp = time.ctime()

    fobj = open("DuplicateRemoval.log","a")
    fobj.write(Border+"\n")
    fobj.write("Total Files Scanned : "+str(FileCount)+"\n")
    fobj.write("Total Files Deleted : "+str(DeleteCount)+"\n")
    fobj.write("Log created at : "+timestamp+"\n")
    fobj.write(Border+"\n")
    fobj.close()



def main():

    if(len(sys.argv) != 2):
        WriteLog("Invalid arguments")
        return

    CreateHeader()

    DirectoryName = sys.argv[1]

    DeleteDuplicate(DirectoryName)

if __name__ == "__main__":
    main()
