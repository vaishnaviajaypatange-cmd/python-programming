import hashlib
import os

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()
    Buffer = fobj.read(1024)
    
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
        fobj.close()

        return hobj.hexdigest()
    
def FindDuplicate(DirectoryName):
    Ret = os.path.exists(DirectoryName)
    if (Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    Duplicate = {}

    for FolderName, SubFolderName, Filename in os.walk(DirectoryName):
        for fname in Filename:
            fname = os.path.join(FolderName,fname)
            Checksum = CalculateChecksum(fname)

            









def main():


if __name__ == "__main__":
    main()

