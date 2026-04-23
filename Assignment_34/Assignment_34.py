import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile


import smtplib
from email.message import EmailMessage


EXCLUDE_EXT = [".tmp", ".log", ".exe"]



def WriteLog(LogFolder, LogData):

    os.makedirs(LogFolder, exist_ok=True)

    LogFile = os.path.join(LogFolder, "BackupLog.txt")

    with open(LogFile, "a") as fobj:
        fobj.write(LogData + "\n")



def SendEmail(LogFile, ZipFile):

    EMAIL = "vaishnaviajaypatange22@gmail.com"
    PASSWORD = "jrdl owvh icaf nsfh"
    RECEIVER = "vaishnaviajaypatange@gmail.com"

    msg = EmailMessage()
    msg['Subject'] = "Backup Completed"
    msg['From'] = EMAIL
    msg['To'] = RECEIVER

    msg.set_content("Backup completed successfully.\nLog and Zip attached.")

    # Attach Log
    with open(LogFile, "rb") as f:
        msg.add_attachment(f.read(),
                           maintype='application',
                           subtype='octet-stream',
                           filename=os.path.basename(LogFile))

    # Attach Zip
    with open(ZipFile, "rb") as f:
        msg.add_attachment(f.read(),
                           maintype='application',
                           subtype='zip',
                           filename=os.path.basename(ZipFile))

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    server.quit()



def RestoreBackup(ZipFile, Destination):

    print("Restoring backup...")

    with zipfile.ZipFile(ZipFile, 'r') as zobj:
        zobj.extractall(Destination)

    print("Backup restored successfully at :", Destination)



def UpdateHistory(FilesCount, ZipName):

    HistoryFile = "BackupHistory.txt"
    Date = time.ctime()
    Size = os.path.getsize(ZipName)

    Data = f"{Date} | Files : {FilesCount} | Size : {Size} bytes\n"

    with open(HistoryFile, "a") as fobj:
        fobj.write(Data)



def make_zip(folder):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    zobj = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:

            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, folder)

            zobj.write(full_path, relative)

    zobj.close()

    return zip_name


def calculate_hash(path):

    hobj = hashlib.md5()
    fobj = open(path, "rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()


def BackupFiles(Source, Destination):

    copied_files = []

    print("Createing the Bckup folder for backup process")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:

            # -------- EXCLUDE FEATURE ADDED --------
            if any(file.endswith(ext) for ext in EXCLUDE_EXT):
                continue
            # --------------------------------------

            src_path = os.path.join(root, file)

            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            if ((not os.path.exists(dest_path)) or
               (calculate_hash(src_path) != calculate_hash(dest_path))):

                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files



def MarvellousDataShieldStart(Source="Data"):

    Border = "-" * 50
    BackupName = "MarvellousBackup"

    # -------- LOGGING START TIME --------
    LogFolder = "Logs"
    StartTime = time.ctime()
  

    print(Border)
    print("Backup Process Started succesfully at : ", StartTime)
    print(Border)

    files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)

  
    UpdateHistory(len(files), zip_file)


    print(Border)
    print("Backup completed succesfully")
    print("Files copied : ", len(files))
    print("Zip file gets creatd : ", zip_file)
    print(Border)


    LogData = f"""
Backup Time : {StartTime}
Files Copied : {len(files)}
Zip File : {zip_file}
Errors : None
"""
    WriteLog(LogFolder, LogData)
 
    LogFilePath = os.path.join(LogFolder, "BackupLog.txt")
    SendEmail(LogFilePath, zip_file)




def main():

    Border = "-" * 50
    print(Border)
    print("--------- Marvellous Data Shield System ----------")
    print(Border)

    if(len(sys.argv) == 2 and sys.argv[1] == "--history"):

        if os.path.exists("BackupHistory.txt"):
            with open("BackupHistory.txt", "r") as fobj:
                print(fobj.read())
        else:
            print("No backup history found.")
  
    elif(len(sys.argv) == 4 and sys.argv[1] == "--restore"):

        ZipFile = sys.argv[2]
        Destination = sys.argv[3]

        RestoreBackup(ZipFile, Destination)
 

    elif(len(sys.argv) == 2):

        if(sys.argv[1] in ["--h", "--H"]):
            print("This scipt is used to : ")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")

        elif(sys.argv[1] in ["--u", "--U"]):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")

        else:
            print("Invalid option")

    elif(len(sys.argv) == 3):

        schedule.every(int(sys.argv[1])).minutes.do(
            MarvellousDataShieldStart,
            sys.argv[2]
        )

        print("Data Sheild System started succesfully")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)


if __name__ == "__main__":
    main()
