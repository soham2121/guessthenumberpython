import time
import os
import shutil

path = input("Enter the path: ")
days = 30
seconds = time.time() - (days*24*60*60)

if(os.path.exists(path)):
    for mainfolder, folders, files in os.walk(path):
        if seconds >= os.stat(mainfolder).st_ctime:
            shutil.rmtree(mainfolder)
        else:
            for folder in folders:
                newpath = os.path.join(mainfolder, folder)
                if seconds >= os.stat(newpath).st_ctime:
                    shutil.rmtree(newpath)           
            for file in files:
                newpath = os.path.join(mainfolder, file)
                if seconds >= os.stat(newpath).st_ctime:
                    os.remove(newpath)                  
else: print('File not found')