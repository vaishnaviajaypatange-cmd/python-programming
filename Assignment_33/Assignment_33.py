import psutil
import sys
import os
import time
import schedule


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def ThreadMonitoring():

    ThreadList = []

    for proc in psutil.process_iter(['pid','name']):
        try:
            Threads = proc.num_threads()

            info = {
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "threads": Threads
            }

            ThreadList.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return ThreadList

def OpenFilesMonitoring():

    FileList = []

    for proc in psutil.process_iter(['pid','name']):
        try:
            files = proc.open_files()
            count = len(files)

            info = {
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "open_files": count
            }

            FileList.append(info)

        except psutil.AccessDenied:

            info = {
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "open_files": "Access Denied"
            }

            FileList.append(info)

        except (psutil.NoSuchProcess, psutil.ZombieProcess):
            pass

    return FileList

def MemoryMonitoring():

    MemList = []

    for proc in psutil.process_iter(['pid','name']):
        try:
            meminfo = proc.memory_info()

            info = {
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "rss": meminfo.rss / (1024*1024),
                "vms": meminfo.vms / (1024*1024),
                "percent": proc.memory_percent()
            }

            MemList.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    MemList.sort(key=lambda x: x['percent'], reverse=True)

    return MemList[:10]

def SendEmail(LogFile, ReceiverMail):

    SenderMail = "vaishnaviajaypatange22@gmail.com"
    AppPassword = "jrdl owvh icaf nsfg"

    msg = MIMEMultipart()
    msg['From'] = SenderMail
    msg['To'] = ReceiverMail
    msg['Subject'] = "System Surveillance Report"

    body = "Please find attached system log report."
    msg.attach(MIMEText(body,'plain'))

    attachment = open(LogFile,"rb")

    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)

    part.add_header(
        'Content-Disposition',
        "attachment; filename= %s" % LogFile
    )

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(SenderMail,AppPassword)

    text = msg.as_string()
    server.sendmail(SenderMail,ReceiverMail,text)
    server.quit()



def CreateLog(FolderName):

    Border = "-"*50

    if(os.path.exists(FolderName) == False):
        os.mkdir(FolderName)
        print("Directory created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("---- Marvellous Platform Surveillance System -----\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("----------------- System Report ------------------\n")

    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    fobj.write("RAM usage : %s %%\n" %mem.percent)
    fobj.write(Border+"\n")


    Data = ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name %s\n" %info.get("name"))
        fobj.write("Username %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("Start time : %s\n" %info.get("create_time"))
        fobj.write("CPU %% : %.2f\n" %info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
        fobj.write(Border+"\n")



    fobj.write("\nThread Monitoring Report\n")
    fobj.write(Border+"\n")

    for tinfo in ThreadMonitoring():
        fobj.write("PID : %s\n" %tinfo["pid"])
        fobj.write("Name : %s\n" %tinfo["name"])
        fobj.write("Thread Count : %s\n" %tinfo["threads"])
        fobj.write(Border+"\n")


    fobj.write("\nOpen Files Report\n")
    fobj.write(Border+"\n")

    for finfo in OpenFilesMonitoring():
        fobj.write("PID : %s\n" %finfo["pid"])
        fobj.write("Name : %s\n" %finfo["name"])
        fobj.write("Open Files : %s\n" %finfo["open_files"])
        fobj.write(Border+"\n")


   
    fobj.write("\nTop 10 Memory Consuming Processes\n")
    fobj.write(Border+"\n")

    for minfo in MemoryMonitoring():
        fobj.write("PID : %s\n" %minfo["pid"])
        fobj.write("Name : %s\n" %minfo["name"])
        fobj.write("RSS : %.2f MB\n" %minfo["rss"])
        fobj.write("VMS : %.2f MB\n" %minfo["vms"])
        fobj.write("Memory %% : %.2f\n" %minfo["percent"])
        fobj.write(Border+"\n")


    fobj.write(Border+"\n")
    fobj.write("----------------- End of Log File ----------------\n")
    fobj.write(Border+"\n")

    fobj.close()

    return FileName



def ProcessScan():

    listprocess = []

    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(
                attrs=["pid","name","username","status","create_time"]
            )

            info["create_time"] = time.strftime(
                "%Y-%m-%d %H:%M:%S",
                time.localtime(info["create_time"])
            )

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()

            listprocess.append(info)

        except:
            pass

    return listprocess



def main():

    Border = "-"*50
    print(Border)
    print("---- Marvellous Platform Surveillance System -----")
    print(Border)

  
    if(len(sys.argv) == 4):

        Folder = sys.argv[1]
        Receiver = sys.argv[2]
        Interval = int(sys.argv[3])

        def Job():
            logfile = CreateLog(Folder)
            SendEmail(logfile, Receiver)

        schedule.every(Interval).minutes.do(Job)

        print("System started successfully")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid arguments")


if __name__ == "__main__":
    main()
